#!/usr/bin/env python3
"""Validate the local capability survey and render its standalone report."""
import argparse
import hashlib
import html
import json
from pathlib import Path


def build(directory, workspace):
    inventory = json.loads((directory / "inventory.json").read_text())
    expected = {item["package"] for item in inventory["packages"]}
    actual = {path.parent.name for path in workspace.glob("*/goml.toml")}
    exclusions = inventory.get("excluded_packages", {})
    if not isinstance(exclusions, dict) or any(not isinstance(reason, str) or not reason.strip() for reason in exclusions.values()):
        raise ValueError("excluded packages require explicit reasons")
    if expected & set(exclusions) or expected | set(exclusions) != actual:
        raise ValueError(f"module inventory mismatch: unaccounted={actual - expected - set(exclusions)}, absent={(expected | set(exclusions)) - actual}")
    records = []
    for shard in sorted(directory.glob("survey-*.json")):
        records.extend(json.loads(shard.read_text()))
    names = [item["package"] for item in records]
    if len(names) != len(set(names)) or set(names) != expected:
        raise ValueError(f"coverage mismatch: missing={expected - set(names)}, extra={set(names) - expected}")
    for item in records:
        for field in ("current_capability", "candidate", "rationale"):
            if not isinstance(item[field], str) or not item[field].strip():
                raise ValueError(f"{item['package']}: missing {field}")
        if item["status"] not in ("candidate", "scope_boundary", "implemented"):
            raise ValueError("invalid status")
        if item["status"] == "implemented" and not item.get("validation"):
            raise ValueError("implemented feature requires validation evidence")
        if item["priority"] not in ("P1", "P2", "P3") or item["effort"] not in ("S", "M", "L"):
            raise ValueError("invalid priority or effort")
        if len(item["evidence"]) < 2 or not item["acceptance"]:
            raise ValueError(f"{item['package']}: insufficient evidence or acceptance criteria")
        for evidence in item["evidence"]:
            path = (workspace / evidence["path"]).resolve()
            if not path.is_relative_to(workspace) or not path.is_file():
                raise ValueError(f"invalid evidence path: {path}")
            data = path.read_bytes()
            if not 1 <= evidence["line"] <= len(data.decode().splitlines()):
                raise ValueError(f"invalid evidence line: {path}:{evidence['line']}")
            if not evidence["observation"].strip():
                raise ValueError("empty evidence observation")
            evidence["sha256"] = hashlib.sha256(data).hexdigest()
        for reference in item["references"]:
            if not reference["url"].startswith("https://") or not reference["feature"].strip():
                raise ValueError("invalid reference")
    for item in inventory["packages"]:
        current = hashlib.sha256((workspace / item["package"] / "README.md").read_bytes()).hexdigest()
        if current != item["readme_sha256"]:
            raise ValueError(f"README changed during review: {item['package']}")
    records.sort(key=lambda item: (item["priority"], item["status"] != "candidate", item["package"]))
    result = {
        "schema_version": 1,
        "review_date": directory.name,
        "scope": inventory["scope"],
        "excluded_packages": exclusions,
        "method": "Current README, relevant public APIs and focused test sources inspected per module; selected candidates compared with official upstream documentation. Runtime validation is reported only for entries explicitly marked implemented; other entries are source reviews, not runtime certification.",
        "priority_legend": {"P1": "优先设计与实现", "P2": "后续候选", "P3": "长期方向或范围边界"},
        "effort_legend": {"S": "局部接口或实现", "M": "跨文件或子模块", "L": "架构、协议或运行时扩展"},
        "packages": records,
    }
    return json.dumps(result, ensure_ascii=False, indent=2) + "\n", render(result)


def render(result):
    esc = html.escape
    cards = []
    for item in result["packages"]:
        evidence = "".join(
            f'<li><a href="../../../{esc(e["path"], quote=True)}">{esc(e["path"])}:{e["line"]}</a> — {esc(e["observation"])}</li>'
            for e in item["evidence"]
        )
        references = "".join(
            f'<li><a href="{esc(r["url"], quote=True)}" rel="noopener">{esc(r["feature"])}</a></li>'
            for r in item["references"]
        ) or "<li>本项依据本地实现审查，未补充外部对照。</li>"
        acceptance = "".join(f"<li>{esc(value)}</li>" for value in item["acceptance"])
        status = {"candidate": "功能候选", "scope_boundary": "范围边界", "implemented": "本轮已实现"}[item["status"]]
        validation = "".join(f"<li>{esc(value)}</li>" for value in item.get("validation", []))
        validation = f"<h4>本轮验证</h4><ul>{validation}</ul>" if validation else ""
        cards.append(f'''<article data-priority="{item['priority']}" data-status="{item['status']}">
<h2>{esc(item['package'])} <small>{item['priority']} · {item['effort']} · {status}</small></h2>
<p class="capability">现有能力：{esc(item['current_capability'])}</p>
<h3>{esc(item['candidate'])}</h3><p>{esc(item['rationale'])}</p>
<details><summary>源码证据、参考与验收条件</summary>
<h4>本地证据</h4><ul>{evidence}</ul><h4>开源参考</h4><ul>{references}</ul>
<h4>验收条件或边界</h4><ul>{acceptance}</ul>{validation}</details></article>''')
    exclusions = "".join(f"<li>{esc(name)}: {esc(reason)}</li>" for name, reason in sorted(result["excluded_packages"].items()))
    exclusion_note = f"<p>本次审查范围外的工作区项目：</p><ul>{exclusions}</ul>" if exclusions else ""
    return '''<!doctype html>
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>GoML 当前工作区能力审查 · 2026-10-22</title>
<style>
body{font:16px/1.65 system-ui,sans-serif;background:#f5f7fa;color:#172335;margin:0}
main{max-width:1080px;margin:auto;padding:28px}h1{font-size:28px}h2{font-size:21px;margin:0}h3{font-size:18px}
small{font-size:13px;font-weight:normal;color:#46546a;margin-left:12px}a{color:#164ead}article{background:white;border:1px solid #d8e0ea;border-radius:10px;padding:20px;margin:16px 0}
input,select{font:inherit;padding:8px;border:1px solid #8c9bad;border-radius:5px;max-width:100%;box-sizing:border-box}
nav{display:flex;gap:12px;flex-wrap:wrap;position:sticky;top:0;background:#f5f7fa;padding:12px 0;align-items:center}
input{min-width:240px;flex:1}summary{cursor:pointer;color:#164ead}.capability{color:#46546a}[hidden]{display:none}
ul{padding-left:24px}li{margin-bottom:6px;overflow-wrap:anywhere}.note{border-left:4px solid #4f7099;padding-left:16px}
</style><main><h1>GoML 当前工作区能力审查</h1>
<p class="note">覆盖当前目录的 76 个 GoML 模块，包含未提交的实现。依据当前 README、相关公开接口与测试源码核实候选；外部对照用于重点条目。本报告不代表运行时测试通过，也不承诺完整兼容参考项目。</p>
<p>P1：优先设计与实现；P2：后续候选；P3：长期方向或范围边界。S/M/L 为相对改动范围，并非工时估算。仅标记“本轮已实现”的条目包含实现与验证结果，其他条目是后续工作或职责边界。提交前已整合本次获取的 origin/main；各条目记录对应验证阶段。</p>
<p><a href="proposals.json">完整结构化数据与证据文件哈希</a> · <a href="inventory.json">76 个模块的工作区快照</a></p>
<nav aria-label="筛选"><input id="query" aria-label="搜索包或功能" placeholder="搜索包、功能、证据…">
<select id="priority" aria-label="优先级"><option value="">全部优先级</option><option>P1</option><option>P2</option><option>P3</option></select>
<select id="status" aria-label="类别"><option value="">全部类别</option><option value="candidate">功能候选</option><option value="scope_boundary">范围边界</option><option value="implemented">本轮已实现</option></select><output id="count" aria-live="polite"></output></nav>
''' + exclusion_note + "\n".join(cards) + '''
<script>
const cards=[...document.querySelectorAll('article')];
const query=document.querySelector('#query'),priority=document.querySelector('#priority'),status=document.querySelector('#status');
function filter(){let shown=0;const text=query.value.trim().toLowerCase();for(const card of cards){card.hidden=Boolean((priority.value&&card.dataset.priority!==priority.value)||(status.value&&card.dataset.status!==status.value)||(text&&!card.textContent.toLowerCase().includes(text)));if(!card.hidden)shown++}document.querySelector('#count').textContent=`显示 ${shown} / ${cards.length}`}
for(const input of [query,priority,status])input.addEventListener('input',filter);filter();
</script></main></html>
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--workspace", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data, page = build(args.directory.resolve(), args.workspace.resolve())
    for name, content in (("proposals.json", data), ("index.html", page)):
        path = args.directory / name
        if args.check:
            if path.read_text() != content:
                raise ValueError(f"out of date: {path}")
        else:
            path.write_text(content)
    print("Review coverage, evidence anchors, README snapshots and report consistency verified")


if __name__ == "__main__":
    main()
