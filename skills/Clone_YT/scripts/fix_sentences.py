#!/usr/bin/env python3
"""
fix_sentences.py — Format .txt story files for Clone_YT skill.

Rules applied to each file:
  - Each sentence on its own line
  - No blank lines between sentences
  - chap-12.txt: the '---' separator between story and Bai Hoc is preserved

Usage:
    python .claude/skills/Clone_YT/scripts/fix_sentences.py <slug>

    slug is the story slug used in workspace/content/Clone_YT-<slug>/
    e.g.  python .claude/skills/Clone_YT/scripts/fix_sentences.py my-story
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SKIP_FILES = {"sum.txt", "prompts.txt"}


def split_sentences(text: str) -> list[str]:
    """Split text into individual sentences, one per line."""
    # Normalize whitespace
    text = re.sub(r"\r\n?", "\n", text)
    # Collapse multiple blank lines into single newline
    text = re.sub(r"\n{2,}", " ", text)
    # Collapse multiple spaces
    text = re.sub(r" {2,}", " ", text)
    text = text.strip()

    # Split on sentence-ending punctuation followed by whitespace
    # Handles: . ! ? followed by space or newline
    # Uses lookahead so the punctuation stays attached to the sentence
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p.strip() for p in parts if p.strip()]


def process_file(path: Path) -> None:
    content = path.read_text(encoding="utf-8")

    # chap-12.txt: preserve '---' separator between story body and Bai Hoc
    if path.name == "chap-12.txt" and "---" in content:
        sep_idx = content.index("---")
        story_part = content[:sep_idx]
        lesson_part = content[sep_idx + 3:]

        story_lines = split_sentences(story_part)
        lesson_lines = split_sentences(lesson_part)

        result_parts = ["\n".join(story_lines)]
        if lesson_lines:
            result_parts.append("---")
            result_parts.append("\n".join(lesson_lines))
        result = "\n".join(result_parts)
    else:
        sentences = split_sentences(content)
        result = "\n".join(sentences)

    path.write_text(result.rstrip() + "\n", encoding="utf-8")
    line_count = len(result.splitlines())
    print(f"  OK  {path.name} — {line_count} lines")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python fix_sentences.py <slug>\nExample: python fix_sentences.py ranger-lost-coast")

    slug = sys.argv[1].strip()
    story_dir = Path("workspace/content") / f"Clone_YT-{slug}"

    if not story_dir.exists():
        sys.exit(
            f"Directory not found: {story_dir}\n"
            f"Make sure you run this from the project root and the slug matches the output folder."
        )

    txt_files = sorted(story_dir.glob("*.txt"))
    to_process = [f for f in txt_files if f.name not in SKIP_FILES]

    if not to_process:
        print(f"No .txt files to process in {story_dir}")
        return

    print(f"Formatting sentences in {story_dir} ...")
    for f in to_process:
        process_file(f)

    print(f"\nDone. Processed {len(to_process)} file(s).")


if __name__ == "__main__":
    main()
