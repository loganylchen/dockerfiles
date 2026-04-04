#!/usr/bin/env python3
"""
Auto-generate the top-level README.md by scanning tools/ directory.

Reads tool metadata from generate_readme.py (TOOL_INFO, CATEGORIES),
versions from tools/<name>/versions.txt, and tool type from Dockerfiles.
"""

from pathlib import Path
from generate_readme import TOOL_INFO, CATEGORIES, detect_tool_type

DOCKER_HUB_USER = "btrspg"


def get_versions(tool_dir):
    """Read versions from versions.txt."""
    vf = tool_dir / "versions.txt"
    if vf.exists():
        return [l.strip() for l in vf.read_text().splitlines()
                if l.strip() and not l.startswith("#")]
    return ["latest"]


def get_tool_type_label(tool_dir):
    """Return a human-readable type label."""
    df = tool_dir / "Dockerfile"
    if not df.exists():
        return ""
    t = detect_tool_type(df)
    return {"r": "R/Bioc", "python": "Python", "java": "Java", "compiled": "Compiled"}.get(t, t)


def build_tool_rows(tools_dir):
    """Build table rows grouped by category."""
    categorized = {}  # category -> list of (name, info, versions, type_label)

    for tool_dir in sorted(tools_dir.iterdir()):
        if not tool_dir.is_dir() or not (tool_dir / "Dockerfile").exists():
            continue
        name = tool_dir.name
        info = TOOL_INFO.get(name, {})
        cat = info.get("category", "other")
        versions = get_versions(tool_dir)
        type_label = get_tool_type_label(tool_dir)
        categorized.setdefault(cat, []).append((name, info, versions, type_label))

    return categorized


def format_versions_badges(name, versions):
    """Format version badges."""
    return " ".join(
        f"![{v}](https://img.shields.io/badge/{name}-{v}-blue)"
        for v in versions
    )


def format_reference(info):
    """Format first reference as a link if available."""
    refs = info.get("references", [])
    if not refs:
        return ""
    r = refs[0]
    if r.startswith("http"):
        return f"[Link]({r})"
    return r


def generate_readme(categorized):
    """Generate the full README content."""
    # Count totals
    total = sum(len(tools) for tools in categorized.values())

    lines = []
    lines.append("# Dockerfiles for Bioinformatics Tools")
    lines.append("")
    lines.append(f"A collection of **{total}** Dockerfiles for bioinformatics tools, "
                 f"maintained by [Yuelong CHEN](mailto:yuelong.chen.btr@gmail.com).")
    lines.append("")
    lines.append("## Quick Start")
    lines.append("")
    lines.append("```bash")
    lines.append(f"# Pull an image")
    lines.append(f"docker pull {DOCKER_HUB_USER}/<tool>:<version>")
    lines.append("")
    lines.append(f"# Build locally")
    lines.append(f"cd tools/<tool>")
    lines.append(f"docker build --build-arg VERSION=<version> -t <tool>:<version> .")
    lines.append("```")
    lines.append("")

    # Category order
    cat_order = [
        "alignment", "quantification", "rna_seq", "splicing", "diff_expr",
        "nanopore", "variant", "genomic_utils", "qc", "annotation",
        "python_bio", "pangenome", "download", "utility", "other",
    ]

    lines.append("## Tools by Category")
    lines.append("")

    for cat in cat_order:
        tools = categorized.get(cat)
        if not tools:
            continue
        cat_info = CATEGORIES.get(cat, {"cn": cat, "en": cat.replace("_", " ").title()})
        lines.append(f"### {cat_info['en']} ({cat_info['cn']})")
        lines.append("")
        lines.append("| Tool | Type | Versions | Reference |")
        lines.append("|------|------|----------|-----------|")
        for name, info, versions, type_label in tools:
            desc = info.get("en_desc", "")
            ref = format_reference(info)
            ver_str = ", ".join(f"`{v}`" for v in versions)
            lines.append(f"| [{name}](tools/{name}/) | {type_label} | {ver_str} | {ref} |")
        lines.append("")

    # Uncategorized
    shown_cats = set(cat_order)
    for cat, tools in categorized.items():
        if cat in shown_cats:
            continue
        cat_info = CATEGORIES.get(cat, {"cn": cat, "en": cat.replace("_", " ").title()})
        lines.append(f"### {cat_info['en']}")
        lines.append("")
        lines.append("| Tool | Type | Versions | Reference |")
        lines.append("|------|------|----------|-----------|")
        for name, info, versions, type_label in tools:
            ref = format_reference(info)
            ver_str = ", ".join(f"`{v}`" for v in versions)
            lines.append(f"| [{name}](tools/{name}/) | {type_label} | {ver_str} | {ref} |")
        lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append(f"- Docker Hub: [`{DOCKER_HUB_USER}`](https://hub.docker.com/u/{DOCKER_HUB_USER})")
    lines.append("- All images include label: `maintainer=Yuelong CHEN <yuelong.chen.btr@gmail.com>`")
    lines.append("- Images are built and pushed via GitHub Actions")
    lines.append("- For detailed usage, check `README.md` in each tool's directory")
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append("If you find any issues or want to add new tools, please open an issue or submit a pull request.")
    lines.append("")

    return "\n".join(lines)


def main():
    tools_dir = Path("tools")
    categorized = build_tool_rows(tools_dir)
    content = generate_readme(categorized)
    Path("README.md").write_text(content)
    total = sum(len(t) for t in categorized.values())
    print(f"README.md updated with {total} tools across {len(categorized)} categories")


if __name__ == "__main__":
    main()
