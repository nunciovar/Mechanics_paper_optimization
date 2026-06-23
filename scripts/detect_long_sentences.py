#!/usr/bin/env python3
"""Report sentences that exceed a configurable word-count threshold."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
LATEX_COMMAND_RE = re.compile(r"\\[A-Za-z@]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?")


def strip_tex(text: str) -> str:
    text = re.sub(r"(?<!\\)%.*", "", text)
    text = LATEX_COMMAND_RE.sub(" ", text)
    text = text.replace("{", " ").replace("}", " ")
    return re.sub(r"\s+", " ", text)


def sentence_records(text: str) -> list[tuple[int, int, str]]:
    lines = text.splitlines()
    records: list[tuple[int, int, str]] = []
    for line_no, raw_line in enumerate(lines, start=1):
        cleaned = strip_tex(raw_line).strip()
        if not cleaned:
            continue
        for sentence in SENTENCE_SPLIT_RE.split(cleaned):
            sentence = sentence.strip()
            if sentence:
                records.append((line_no, len(WORD_RE.findall(sentence)), sentence))
    return records


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report sentences that exceed a word threshold."
    )
    parser.add_argument("paths", nargs="+", help="Text or .tex files to scan")
    parser.add_argument("--threshold", type=int, default=35, help="Maximum preferred word count")
    args = parser.parse_args()

    findings = 0
    for raw_path in args.paths:
        path = Path(raw_path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_no, word_count, sentence in sentence_records(text):
            if word_count > args.threshold:
                findings += 1
                snippet = sentence[:180]
                print(f"{path}:{line_no} words={word_count} :: {snippet}")

    if findings == 0:
        print("No long sentences found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
