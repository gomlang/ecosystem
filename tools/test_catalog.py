import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest

import catalog


class CatalogTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.data = {
            "schema_version": 1,
            "libraries": [{"name": "parser", "scope": "Parsing", "coverage": "Module tests"}],
            "applications": [{"name": "explorer", "scope": "Terminal application"}],
        }
        self.save_data()
        self.write("split-manifest.tsv", "# Source commit: " + "a" * 40 + "\n"
                   + "parser\t" + "b" * 40 + "\t" + "c" * 40 + "\n")
        self.write("consumer-split-manifest.tsv", "name\tsplit_commit\nparser\t" + "d" * 40 + "\n")
        self.write("README.md", "# Catalog\n\n" + catalog.render(self.data) + "\n\nFooter.\n")
        self.write("ROADMAP.md", "# Roadmap\n\n## Remaining work\n")
        self.write("FINDINGS.md", "# Findings\n")

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def save_data(self):
        self.write("catalog.json", json.dumps(self.data))

    def run_check(self, *args):
        stderr, stdout = io.StringIO(), io.StringIO()
        with contextlib.redirect_stderr(stderr), contextlib.redirect_stdout(stdout):
            status = catalog.main(["--root", str(self.root), *args])
        return status, stderr.getvalue(), stdout.getvalue()

    def test_standalone_check_needs_no_sibling_checkout(self):
        status, error, output = self.run_check()
        self.assertEqual((status, error), (0, ""))
        self.assertIn("1 libraries, 1 applications", output)

    def test_generated_table_drift_fails_without_rewriting(self):
        self.data["libraries"][0]["scope"] = "Updated scope"
        self.save_data()
        before = (self.root / "README.md").read_bytes()
        status, error, _ = self.run_check()
        self.assertEqual(status, 1)
        self.assertIn("out of date", error)
        self.assertEqual((self.root / "README.md").read_bytes(), before)
        self.assertEqual(self.run_check("--write")[0], 0)
        updated = (self.root / "README.md").read_text()
        self.assertIn("Updated scope", updated)
        self.assertTrue(updated.startswith("# Catalog\n\n"))
        self.assertTrue(updated.endswith("\n\nFooter.\n"))
        self.assertEqual(self.run_check()[0], 0)
        self.assertEqual(self.run_check("--write")[0], 0)
        self.assertEqual((self.root / "README.md").read_text(), updated)

    def test_new_library_does_not_rewrite_historical_manifests(self):
        history = [(self.root / file).read_bytes() for file in
                   ("split-manifest.tsv", "consumer-split-manifest.tsv")]
        self.data["libraries"].append({"name": "uuid", "scope": "UUIDs", "coverage": "Vectors"})
        self.save_data()
        self.assertEqual(self.run_check("--write")[0], 0)
        self.assertEqual(history, [(self.root / file).read_bytes() for file in
                                  ("split-manifest.tsv", "consumer-split-manifest.tsv")])

    def test_renamed_library_preserves_history_and_requires_current_name(self):
        for file in ("split-manifest.tsv", "consumer-split-manifest.tsv"):
            path = self.root / file
            path.write_text(path.read_text().replace("parser\t", "logos\t"))
        history = [(self.root / file).read_bytes() for file in
                   ("split-manifest.tsv", "consumer-split-manifest.tsv")]
        self.data["libraries"][0]["name"] = "lexer"
        self.save_data()
        self.assertEqual(self.run_check("--write")[0], 0)
        self.assertEqual(history, [(self.root / file).read_bytes() for file in
                                  ("split-manifest.tsv", "consumer-split-manifest.tsv")])
        for name in ("logos", "unrelated"):
            self.data["libraries"][0]["name"] = name
            self.save_data()
            self.assertIn("historical libraries missing", self.run_check()[1])

    def test_invalid_catalog_records_fail_with_diagnostics(self):
        mutations = [
            lambda data: data.update(schema_version=True),
            lambda data: data.update(libraries={}),
            lambda data: data["libraries"][0].update(name="../parser"),
            lambda data: data["libraries"][0].update(scope=""),
            lambda data: data["libraries"][0].update(scope="two\nlines"),
            lambda data: data["libraries"][0].update(unknown="field"),
            lambda data: data["libraries"].append(dict(data["libraries"][0])),
            lambda data: data["applications"][0].update(name="parser"),
            lambda data: data["applications"][0].update(name="verification"),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                data = copy.deepcopy(self.data)
                mutate(data)
                self.write("catalog.json", json.dumps(data))
                status, error, _ = self.run_check()
                self.assertEqual(status, 1)
                self.assertIn("Catalog check failed:", error)

    def test_duplicate_json_keys_are_rejected(self):
        text = json.dumps(self.data).replace('"schema_version": 1', '"schema_version": 1, "schema_version": 1')
        self.write("catalog.json", text)
        self.assertIn("duplicate JSON key", self.run_check()[1])

    def test_history_requires_full_hashes_unique_names_and_matching_modules(self):
        original = (self.root / "split-manifest.tsv").read_text()
        corruptions = [
            original.replace("b" * 40, "b" * 7),
            original + original.splitlines()[-1] + "\n",
            original.replace("parser\t", "other\t"),
            original.replace("# Source commit: " + "a" * 40, "# no source commit"),
        ]
        for text in corruptions:
            with self.subTest(text=text):
                self.write("split-manifest.tsv", text)
                self.assertEqual(self.run_check()[0], 1)
        self.write("split-manifest.tsv", original)
        self.data["libraries"][0]["name"] = "replacement"
        self.save_data()
        self.assertIn("historical libraries missing", self.run_check()[1])

    def test_write_refuses_missing_duplicate_or_reversed_markers(self):
        for contents in ["# No table\n", catalog.START * 2 + catalog.END,
                         catalog.END + "\n" + catalog.START]:
            with self.subTest(contents=contents):
                self.write("README.md", contents)
                self.assertEqual(self.run_check("--write")[0], 1)
                self.assertEqual((self.root / "README.md").read_text(), contents)

    def test_pipe_and_backslash_in_scope_are_escaped(self):
        self.data["libraries"][0]["scope"] = "A | B \\ C"
        rendered = catalog.render(self.data)
        self.assertIn("A \\| B \\\\ C", rendered)

    def test_local_and_github_catalog_links_validate_files_and_fragments(self):
        valid = ["ROADMAP.md#remaining-work", "https://github.com/gomlang/ecosystem/blob/main/ROADMAP.md#remaining-work",
                 "catalog.json", "https://github.com/gomlang/parser/blob/main/README.md"]
        self.write("FINDINGS.md", "\n".join(f"[Link]({target})" for target in valid))
        self.assertEqual(self.run_check()[0], 0)
        for target in ["absent.md", "ROADMAP.md#absent", "../outside.md"]:
            with self.subTest(target=target):
                self.write("FINDINGS.md", f"[Broken]({target})")
                status, error, _ = self.run_check()
                self.assertEqual(status, 1)
                self.assertIn(target, error)

    def test_code_spans_require_matching_backtick_runs_without_joining_prose(self):
        for text in ["Use ``a ` [example](absent.md)`` after.",
                     "Use `a `` [example](absent.md)` after.",
                     "[label]`code`(absent.md)"]:
            with self.subTest(text=text):
                self.write("FINDINGS.md", text)
                status, error, _ = self.run_check()
                self.assertEqual((status, error), (0, ""))

    def test_escaped_or_unmatched_backticks_do_not_hide_real_links(self):
        for text in [r"\`[real](absent.md)`", "``before [real](absent.md)` after",
                     "before `literal\n\n[real](absent.md)`"]:
            with self.subTest(text=text):
                self.write("FINDINGS.md", text)
                status, error, _ = self.run_check()
                self.assertEqual(status, 1)
                self.assertIn("absent.md", error)

    def test_link_destinations_keep_literal_backticks(self):
        self.write("a`b`c.md", "# Backtick name\n")
        self.write("FINDINGS.md", "[real](a`b`c.md)")
        status, error, _ = self.run_check()
        self.assertEqual((status, error), (0, ""))
        self.write("FINDINGS.md", "[real](absent`file`.md)")
        status, error, _ = self.run_check()
        self.assertEqual(status, 1)
        self.assertIn("absent`file`.md", error)

    def test_optional_link_titles_do_not_hide_missing_files_or_fragments(self):
        for target in ["absent.md", "ROADMAP.md#absent", "<absent file.md>"]:
            for title in ['"description"', "'description'", '(description)', '"escaped \\"quote\\""']:
                with self.subTest(target=target, title=title):
                    self.write("FINDINGS.md", f"[Broken]({target} {title})")
                    status, error, _ = self.run_check()
                    self.assertEqual(status, 1)
                    self.assertIn("absent", error)

    def test_link_destinations_allow_angles_balanced_parentheses_and_escapes(self):
        self.write("Guide (v1).md", "# Guide\n## Details\n")
        self.write("Guide(v1).md", "# Guide\n")
        self.write("Guide(v1(nested(third))).md", "# Guide\n")
        self.write("A&B.md", "# Guide\n")
        targets = ["<ROADMAP.md#remaining-work>", "<Guide (v1).md#details>",
                   "Guide(v1).md", r"Guide\(v1\).md", "Guide(v1(nested(third))).md",
                   "A&amp;B.md", "<A&amp;B.md>"]
        for target in targets:
            for title in ["", ' "optional title"', " 'optional title'", " (optional title)"]:
                for before, after in [("", ""), (" \n", " ")]:
                    with self.subTest(target=target, title=title, padding=before):
                        self.write("FINDINGS.md", f"[Valid]({before}{target}{title}{after})")
                        status, error, _ = self.run_check()
                        self.assertEqual((status, error), (0, ""))

    def test_literal_brackets_and_malformed_destinations_are_not_links(self):
        for text in [r"\[literal](absent.md)", "](absent.md)",
                     "[literal](<absent.md>junk)", "[literal](<absent.md)",
                     '[literal](absent.md "unterminated)', "[literal](absent(unbalanced.md)"]:
            with self.subTest(text=text):
                self.write("FINDINGS.md", text)
                self.assertEqual(self.run_check()[0], 0)

    def test_empty_destinations_and_multiline_titles(self):
        cases = ["[Local]()", "[Local](<>)", '[Local]("a title")',
                 "[Local]('a title')", "[Local]((a title))",
                 '[Local](ROADMAP.md "a title\non two lines")']
        for text in cases:
            with self.subTest(text=text):
                self.write("FINDINGS.md", text)
                self.assertEqual(self.run_check()[0], 0)
        self.write("FINDINGS.md", '[Broken](absent.md\n "a title\non two lines")')
        self.assertIn("absent.md", self.run_check()[1])

    def test_entities_and_escapes_are_decoded_once_in_destinations(self):
        self.write("A&amp;B.md", "# Literal amp entity\n")
        self.write("A&B.md", "# Ampersand\n")
        targets = [r"A\&amp;B.md", "A&amp;amp;B.md", "A&#38;B.md", "A&#x26;B.md"]
        for target in targets:
            with self.subTest(target=target):
                self.write("FINDINGS.md", f"[Valid]({target})")
                self.assertEqual(self.run_check()[0], 0)
        self.write("FINDINGS.md", '[Broken](A&invalid;B.md "title")')
        self.assertIn("A&invalid;B.md", self.run_check()[1])
        self.assertEqual(catalog.decode_destination("A&amp;#38;B.md"), "A&#38;B.md")

    def test_nested_and_escaped_label_brackets_preserve_link_boundaries(self):
        for label in ["[nested] label", r"escaped \] label", r"escaped \[ label"]:
            with self.subTest(label=label):
                self.write("FINDINGS.md", f'[{label}](absent.md "title")')
                self.assertIn("absent.md", self.run_check()[1])
        self.write("FINDINGS.md", "[outer [inner](ROADMAP.md)](absent.md)")
        self.assertEqual(self.run_check()[0], 0)

    def test_markdown_examples_are_not_treated_as_links_or_headings(self):
        self.write("FINDINGS.md", "`[literal](absent.md)`\n```goml\n[literal](missing.md)\n```\n")
        self.assertEqual(self.run_check()[0], 0)
        self.assertEqual(catalog.anchors("## API `v1`\n## API `v1`\n```\n## Hidden\n```\n"),
                         {"api-v1", "api-v1-1"})

    def test_fence_character_length_and_indentation_control_code_boundaries(self):
        cases = [
            ("~~~text", "# Hidden\n[literal](absent.md)\n", "~~~"),
            ("   ```text", "# Hidden\n[literal](absent.md)\n", "  ```"),
            ("````text", "```\n# Hidden\n[literal](absent.md)\n```\n", "`````"),
            ("~~~text", "```\n# Hidden\n[literal](absent.md)\n", "~~~~"),
            ("```text", "``` trailing text\n# Hidden\n[literal](absent.md)\n", "```"),
        ]
        for opening, content, closing in cases:
            with self.subTest(opening=opening, content=content, closing=closing):
                text = f"# Before\n{opening}\n{content}{closing}\n# After\n"
                self.assertEqual(catalog.anchors(text), {"before", "after"})
                self.write("FINDINGS.md", text + "[valid](ROADMAP.md#remaining-work)\n")
                self.assertEqual(self.run_check()[0], 0)
                self.write("FINDINGS.md", text + "[broken](missing.md)\n")
                self.assertIn("missing.md", self.run_check()[1])

    def test_unclosed_fence_hides_examples_through_end_of_document(self):
        for opening in ["```", "~~~", "`````"]:
            with self.subTest(opening=opening):
                text = f"# Before\n{opening}\n# Hidden\n[literal](absent.md)\n"
                self.assertEqual(catalog.anchors(text), {"before"})
                self.write("FINDINGS.md", text)
                self.assertEqual(self.run_check()[0], 0)

    def test_backtick_in_fence_info_does_not_start_a_code_block(self):
        text = "```info`invalid\n# Visible\n"
        self.assertEqual(catalog.without_fences(text), text)
        self.assertEqual(catalog.anchors(text), {"visible"})

    def test_heading_suffixes_never_collide_with_existing_anchors(self):
        headings = "# Entry\n# Entry-1\n# Entry\n# Entry-1\n# Entry\n   ## Indented\n"
        expected = {"entry", "entry-1", "entry-2", "entry-1-1", "entry-3", "indented"}
        self.assertEqual(catalog.anchors(headings), expected)
        self.write("ROADMAP.md", headings)
        self.write("FINDINGS.md", "\n".join(f"[heading](ROADMAP.md#{slug})" for slug in expected))
        self.assertEqual(self.run_check()[0], 0)

    def inventory(self):
        return {"parser": {"kind": "library"}, "explorer": {"kind": "application"},
                "ecosystem": {"kind": "catalog"}}

    def test_inventory_checks_both_omissions_and_repository_roles(self):
        inventory = self.inventory()
        path = self.write("inventory.json", json.dumps(inventory))
        self.assertEqual(self.run_check("--inventory", str(path))[0], 0)
        for change in [lambda data: data.pop("parser"),
                       lambda data: data.update(unknown={"kind": "library"}),
                       lambda data: data["explorer"].update(kind="library")]:
            data = copy.deepcopy(inventory)
            change(data)
            self.write("inventory.json", json.dumps(data))
            self.assertEqual(self.run_check("--inventory", str(path))[0], 1)

    def test_sibling_check_verifies_real_module_coordinates(self):
        for name in ("parser", "explorer", "ecosystem"):
            self.write(f"siblings/{name}/README.md", f"# {name}\n")
        self.write("siblings/parser/goml.toml", '[module]\npath = "ecosystem::parser"\n')
        self.write("siblings/explorer/goml.toml", '[module]\npath = "example::explorer"\n')
        self.write("siblings/verification/ci/repositories.json", json.dumps(self.inventory()))
        args = ["--libraries", str(self.root / "siblings")]
        self.assertEqual(self.run_check(*args)[0], 0)
        self.write("siblings/parser/goml.toml", '[module]\npath = "ecosystem::wrong"\n')
        self.assertIn("incorrect module coordinate", self.run_check(*args)[1])
        (self.root / "siblings/parser/goml.toml").unlink()
        self.assertIn("missing module manifest", self.run_check(*args)[1])


if __name__ == "__main__":
    unittest.main()
