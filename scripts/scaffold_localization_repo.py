#!/usr/bin/env python3
"""Create the standard website-localization repository layout safely."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create origin/, zh/, docs/, and missing process-document templates."
    )
    parser.add_argument("project_root", type=Path, help="Target project directory")
    args = parser.parse_args()

    root = args.project_root.expanduser().resolve()
    template_dir = Path(__file__).resolve().parent.parent / "assets" / "project-docs"
    if not template_dir.is_dir():
        parser.error(f"template directory is missing: {template_dir}")

    created: list[Path] = []
    skipped: list[Path] = []
    for directory in (root / "origin", root / "zh", root / "docs", root / "docs" / "progress"):
        if directory.exists():
            skipped.append(directory)
        else:
            directory.mkdir(parents=True)
            created.append(directory)

    for template in sorted(template_dir.glob("*.md")):
        destination = root / "docs" / template.name
        if destination.exists():
            skipped.append(destination)
            continue
        shutil.copyfile(template, destination)
        created.append(destination)

    print(f"project_root={root}")
    for path in created:
        print(f"created={path.relative_to(root)}")
    for path in skipped:
        print(f"kept={path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
