"""Render and validate the ecosystem catalog using only the Python standard library."""

import argparse
from bisect import bisect_right
import html
from html.entities import html5
import json
from pathlib import Path
import re
import string
import sys
import tomllib
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- catalog:start -->"
END = "<!-- catalog:end -->"
NAME = re.compile(r"[a-z][a-z0-9_]*")
SHA = re.compile(r"[0-9a-f]{40}")
# Preserve the original split manifests while resolving renamed libraries.
HISTORICAL_RENAMES = {"logos": "lexer"}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def load_catalog(root):
    data = read_json(root / "catalog.json")
    if not isinstance(data, dict) or set(data) != {"schema_version", "libraries", "applications"}:
        raise ValueError("catalog.json requires schema_version, libraries and applications")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValueError("unsupported catalog schema_version (expected 1)")
    names = {"ecosystem", "verification"}
    for kind in ("libraries", "applications"):
        entries = data[kind]
        if not isinstance(entries, list) or not entries:
            raise ValueError(f"{kind} must be a nonempty array")
        fields = {"name", "scope", "coverage"} if kind == "libraries" else {"name", "scope"}
        for entry in entries:
            if not isinstance(entry, dict) or set(entry) != fields:
                raise ValueError(f"{kind} entries require {', '.join(sorted(fields))}")
            for field, value in entry.items():
                if (not isinstance(value, str) or not value.strip()
                        or any(ord(char) < 32 or ord(char) == 127 for char in value)):
                    raise ValueError(f"{kind}.{field} must be nonempty text on one line")
            name = entry["name"]
            if not NAME.fullmatch(name):
                raise ValueError(f"invalid repository name: {name}")
            if name in names:
                raise ValueError(f"duplicate or reserved repository name: {name}")
            names.add(name)
    return data


def read_manifest(path, columns, header=None):
    lines = path.read_text(encoding="utf-8").splitlines()
    if header is not None:
        if not lines or lines[0] != header:
            raise ValueError(f"{path.name}: incorrect TSV header")
        lines = lines[1:]
    names = set()
    for line in lines:
        if not line or line.startswith("#"):
            continue
        fields = line.split("\t")
        if (len(fields) != columns or not NAME.fullmatch(fields[0])
                or not all(SHA.fullmatch(value) for value in fields[1:])):
            raise ValueError(f"{path.name}: invalid manifest row: {line}")
        if fields[0] in names:
            raise ValueError(f"{path.name}: duplicate module: {fields[0]}")
        names.add(fields[0])
    if not names:
        raise ValueError(f"{path.name}: manifest is empty")
    return names


def check_history(root, data):
    source = (root / "split-manifest.tsv").read_text(encoding="utf-8").splitlines()
    if not source or not re.fullmatch(r"# Source commit: [0-9a-f]{40}", source[0]):
        raise ValueError("split-manifest.tsv: missing full source commit")
    split = read_manifest(root / "split-manifest.tsv", 3)
    consumers = read_manifest(root / "consumer-split-manifest.tsv", 2, "name\tsplit_commit")
    if split != consumers:
        raise ValueError(f"historical manifest modules differ: {sorted(split ^ consumers)}")
    current_names = {entry["name"] for entry in data["libraries"]}
    missing = {name for name in split
               if HISTORICAL_RENAMES.get(name, name) not in current_names}
    if missing:
        raise ValueError(f"historical libraries missing from catalog: {sorted(missing)}")


def repository_kinds(data):
    result = {entry["name"]: "library" for entry in data["libraries"]}
    result.update({entry["name"]: "application" for entry in data["applications"]})
    result["ecosystem"] = "catalog"
    return result


def check_inventory(path, data):
    inventory = read_json(path)
    if not isinstance(inventory, dict):
        raise ValueError("verification inventory must be an object")
    expected = repository_kinds(data)
    if set(inventory) != set(expected):
        raise ValueError(f"verification inventory/catalog mismatch: {sorted(set(inventory) ^ set(expected))}")
    for name, kind in expected.items():
        record = inventory[name]
        if not isinstance(record, dict) or record.get("kind") != kind:
            raise ValueError(f"verification inventory has incorrect kind for {name}: expected {kind}")


def check_libraries(root, data):
    for name, kind in repository_kinds(data).items():
        directory = root / name
        if not (directory / "README.md").is_file():
            raise ValueError(f"missing repository README: {directory / 'README.md'}")
        if kind == "catalog":
            continue
        manifest = directory / "goml.toml"
        if not manifest.is_file():
            raise ValueError(f"missing module manifest: {manifest}")
        value = tomllib.loads(manifest.read_text(encoding="utf-8"))
        module = value.get("module", {})
        coordinate = module.get("path") if isinstance(module, dict) else None
        if not isinstance(coordinate, str) or not coordinate:
            raise ValueError(f"missing module coordinate: {manifest}")
        if kind == "library" and coordinate != f"ecosystem::{name}":
            raise ValueError(f"incorrect module coordinate in {manifest}: {coordinate}")
    check_inventory(root / "verification/ci/repositories.json", data)


def cell(value):
    return value.replace("\\", "\\\\").replace("|", "\\|")


def link(name):
    return f"[{name}](https://github.com/gomlang/{name}/blob/main/README.md)"


def render(data):
    lines = [START, "", f"The catalog contains **{len(data['libraries'])} libraries**.", "",
             "| Module | Implemented scope | Verification coverage |", "| --- | --- | --- |"]
    for entry in sorted(data["libraries"], key=lambda entry: entry["name"]):
        lines.append(f"| {link(entry['name'])} | {cell(entry['scope'])} | {cell(entry['coverage'])} |")
    lines += ["", "Applications are listed separately from importable libraries:", "",
              "| Application | Purpose |", "| --- | --- |"]
    for entry in sorted(data["applications"], key=lambda entry: entry["name"]):
        lines.append(f"| {link(entry['name'])} | {cell(entry['scope'])} |")
    return "\n".join([*lines, "", END])


def replace_catalog(readme, data):
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README.md must contain exactly one catalog marker pair")
    before, remainder = readme.split(START)
    if END not in remainder:
        raise ValueError("README.md catalog markers are reversed")
    _, after = remainder.split(END)
    return before + render(data) + after


def without_fences(text):
    # CommonMark fences use matching characters, with a closing run at least as
    # long as the opening run: https://spec.commonmark.org/0.31.2/#fenced-code-blocks
    output, fence = [], None
    for line in text.splitlines(keepends=True):
        marker = re.fullmatch(r" {0,3}(`{3,}|~{3,})(.*)", line.rstrip("\r\n"))
        if fence is not None:
            if (marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence)
                    and not marker[2].strip(" \t")):
                fence = None
        elif marker and (marker[1][0] == "~" or "`" not in marker[2]):
            fence = marker[1]
        else:
            output.append(line)
            continue
        # Preserve block boundaries so prose on opposite sides cannot combine.
        output.append("\n")
    return "".join(output)


def prose(text):
    # Inline code is skipped by the link scanner, which must retain backticks
    # inside destinations and must not join text on either side of a code span.
    return without_fences(text)


def anchors(text):
    counts = {}
    result = set()
    for heading in re.findall(r"(?m)^ {0,3}#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", without_fences(text)):
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        base = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = counts.get(base, 0)
        candidate = f"{base}-{count}" if count else base
        while candidate in result:
            count += 1
            candidate = f"{base}-{count}"
        result.add(candidate)
        counts[base] = count + 1
    return result


def escaped(text, index):
    return (text[index] == "\\" and index + 1 < len(text)
            and text[index + 1] in string.punctuation)


def link_space(text, index):
    start = index
    while index < len(text) and text[index] in " \t\n":
        index += 1
    return index if text[start:index].count("\n") <= 1 else None


def link_title_end(text, index):
    if index >= len(text) or text[index] not in "\"'(":
        return None
    closing = ")" if text[index] == "(" else text[index]
    start = index + 1
    index = start
    while index < len(text):
        if escaped(text, index):
            index += 2
            continue
        if text[index] == closing:
            if re.search(r"\n[ \t]*\n", text[start:index]):
                return None
            return index + 1
        if closing == ")" and text[index] == "(":
            return None
        index += 1
    return None


def link_destination(text, index):
    """Parse the destination/title after ](, returning None for literal text."""
    start = link_space(text, index)
    if start is None or start == len(text):
        return None
    index = start
    depth = 0
    if text[index] == "<":
        index += 1
        while index < len(text) and text[index] != ">":
            if text[index] in "<\n":
                return None
            index += 2 if escaped(text, index) else 1
        if index == len(text):
            return None
        target = text[start + 1:index]
        index += 1
    else:
        while index < len(text):
            char = text[index]
            if escaped(text, index):
                index += 2
                continue
            if char == ")":
                if depth == 0:
                    break
                depth -= 1
            elif char == "(":
                depth += 1
            elif ord(char) <= 32 or ord(char) == 127:
                break
            index += 1
        target = text[start:index]

    end = link_space(text, index) if not depth else None
    if end is not None and end < len(text) and text[end] == ")":
        return target, end + 1
    # A title must be separated from a destination. If the destination parse
    # failed, an omitted destination followed by a title is also valid.
    title = link_title_end(text, end) if end is not None and end > index else None
    if title is None:
        target = ""
        title = link_title_end(text, start)
    if title is not None:
        end = link_space(text, title)
        if end is not None and end < len(text) and text[end] == ")":
            return target, end + 1
    return None


def decode_destination(target):
    def decode(match):
        value = match[0]
        if value.startswith("\\"):
            return value[1:]
        if value.startswith("&#") or value[1:] in html5:
            return html.unescape(value)
        return value

    # Decode together so an escaped ampersand does not start an entity.
    return re.sub(r"\\[" + re.escape(string.punctuation)
                  + r"]|&(?:#[0-9]{1,7}|#[xX][0-9a-fA-F]{1,6}|[A-Za-z][A-Za-z0-9]*);",
                  decode, target)


def inline_targets(text):
    # Inline links allow angle destinations, balanced parentheses and optional
    # titles: https://spec.commonmark.org/0.31.2/#links
    backticks = {}
    for run in re.finditer(r"`+", text):
        backticks.setdefault(run.end() - run.start(), []).append(run.start())
    paragraphs = [match.start() for match in re.finditer(r"\n[ \t]*\n", text)]
    paragraphs.append(len(text))
    brackets = []
    index = 0
    while index < len(text):
        if escaped(text, index):
            index += 2
            continue
        if text[index] == "`":
            end = index + 1
            while end < len(text) and text[end] == "`":
                end += 1
            width = end - index
            positions = backticks.get(width, [])
            following = bisect_right(positions, index)
            boundary = paragraphs[bisect_right(paragraphs, index)]
            if following < len(positions) and positions[following] < boundary:
                index = positions[following] + width
            else:
                index = end
            continue
        if text.startswith("![", index):
            brackets.append([True, True])
            index += 2
            continue
        if text[index] == "[":
            brackets.append([False, True])
        elif text[index] == "]" and brackets:
            image, active = brackets.pop()
            if active and text.startswith("(", index + 1):
                link = link_destination(text, index + 2)
                if link is not None:
                    target, index = link
                    yield decode_destination(target)
                    if not image:
                        for bracket in brackets:
                            if not bracket[0]:
                                bracket[1] = False
                    continue
        index += 1


def check_links(root, readme):
    documents = {"README.md": readme}
    for name in ("ROADMAP.md", "FINDINGS.md"):
        documents[name] = (root / name).read_text(encoding="utf-8")
    for name, text in documents.items():
        for target in inline_targets(prose(text)):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                prefix = "/gomlang/ecosystem/blob/main/"
                if url.netloc != "github.com" or not url.path.startswith(prefix):
                    continue
                file = unquote(url.path[len(prefix):])
            else:
                file = unquote(url.path) or name
            path = (root / file).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file():
                raise ValueError(f"{name}: missing catalog link target: {target}")
            if url.fragment and path.suffix == ".md":
                contents = documents.get(file)
                if contents is None:
                    contents = path.read_text(encoding="utf-8")
                if unquote(url.fragment) not in anchors(contents):
                    raise ValueError(f"{name}: missing heading for link: {target}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="check without writing (default)")
    mode.add_argument("--write", action="store_true", help="regenerate the README catalog tables")
    parser.add_argument("--root", type=Path, default=ROOT, help="catalog checkout directory")
    parser.add_argument("--inventory", type=Path, help="verification/ci/repositories.json to compare")
    parser.add_argument("--libraries", type=Path, help="check sibling READMEs, module coordinates and inventory")
    args = parser.parse_args(argv)
    try:
        data = load_catalog(args.root)
        check_history(args.root, data)
        if args.inventory:
            check_inventory(args.inventory, data)
        if args.libraries:
            check_libraries(args.libraries, data)
        path = args.root / "README.md"
        old = path.read_text(encoding="utf-8")
        new = replace_catalog(old, data)
        check_links(args.root, new)
        if args.write:
            if old != new:
                path.write_text(new, encoding="utf-8")
        elif old != new:
            raise ValueError("README catalog is out of date; run python3 tools/catalog.py --write")
    except (ValueError, OSError) as error:
        print(f"Catalog check failed: {error}", file=sys.stderr)
        return 1
    print(f"Catalog OK: {len(data['libraries'])} libraries, {len(data['applications'])} applications")
    return 0


if __name__ == "__main__":
    sys.exit(main())
