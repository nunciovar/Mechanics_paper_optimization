#!/usr/bin/env python3
"""Scan manuscript text for repeated openers and repeated n-grams."""

from __future__ import annotations

import argparse
import collections
import re
from pathlib import Path


WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
LATEX_COMMAND_RE = re.compile(r"\\[A-Za-z@]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?")


def normalize_text(text: str) -> str:
    text = re.sub(r"(?<!\\)%.*", "", text)
    text = LATEX_COMMAND_RE.sub(" ", text)
    text = text.replace("{", " ").replace("}", " ")
    return re.sub(r"\s+", " ", text).lower()


def paragraph_openers(text: str, opener_words: int) -> collections.Counter[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    counter: collections.Counter[str] = collections.Counter()
    for paragraph in paragraphs:
        words = WORD_RE.findall(normalize_text(paragraph))
        if len(words) >= opener_words:
            counter[" ".join(words[:opener_words])] += 1
    return counter


def ngrams(text: str, size: int) -> collections.Counter[str]:
    words = WORD_RE.findall(normalize_text(text))
    counter: collections.Counter[str] = collections.Counter()
    for index in range(len(words) - size + 1):
        counter[" ".join(words[index : index + size])] += 1
    return counter


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan for repeated openers and n-grams.")
    parser.add_argument("paths", nargs="+", help="Files to scan")
    parser.add_argument(
        "--opener-words",
        type=int,
        default=5,
        help="Words to compare at paragraph starts",
    )
    parser.add_argument("--ngram-size", type=int, default=4, help="N-gram size")
    parser.add_argument("--min-count", type=int, default=3, help="Minimum repeat count to report")
    parser.add_argument("--top", type=int, default=15, help="Maximum rows per report")
    args = parser.parse_args()

    combined_text = []
    for raw_path in args.paths:
        path = Path(raw_path)
        combined_text.append(path.read_text(encoding="utf-8", errors="ignore"))

    text = "\n".join(combined_text)
    opener_hits = paragraph_openers(text, args.opener_words)
    ngram_hits = ngrams(text, args.ngram_size)

    reported = False

    print("Paragraph opener repeats:")
    for phrase, count in opener_hits.most_common(args.top):
        if count >= args.min_count:
            print(f"  {count}x :: {phrase}")
            reported = True

    print("\nN-gram repeats:")
    for phrase, count in ngram_hits.most_common(args.top):
        if count >= args.min_count:
            print(f"  {count}x :: {phrase}")
            reported = True

    if not reported:
        print("  No repetition hotspots above the threshold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
