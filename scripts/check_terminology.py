#!/usr/bin/env python3
"""Check terminology drift, acronym first use, and banned phrases."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


LATEX_COMMAND_RE = re.compile(r"\\[A-Za-z@]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?")


def parse_terminology(path: Path) -> tuple[dict[str, list[str]], list[str]]:
    """Parse the repository's small terminology.yml subset.

    The parser intentionally supports only the structure used in style/terminology.yml:

    preferred_terms:
      term:
        canonical: ...
        variants:
          - ...
    acronym_first_use:
      - CNT
    """
    preferred: dict[str, list[str]] = {}
    acronyms: list[str] = []
    section: str | None = None
    current_term: str | None = None
    in_variants = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = len(line) - len(line.lstrip(" "))

        if indent == 0 and stripped.endswith(":"):
            section = stripped[:-1]
            current_term = None
            in_variants = False
            continue

        if section == "preferred_terms":
            if indent == 2 and stripped.endswith(":"):
                current_term = stripped[:-1]
                preferred.setdefault(current_term, [])
                in_variants = False
                continue
            if current_term and indent == 4 and stripped.startswith("canonical:"):
                canonical = stripped.split(":", 1)[1].strip()
                if canonical and canonical not in preferred[current_term]:
                    preferred[current_term].insert(0, canonical)
                continue
            if current_term and indent == 4 and stripped == "variants:":
                in_variants = True
                continue
            if current_term and in_variants and indent >= 6 and stripped.startswith("-"):
                variant = stripped.split("-", 1)[1].strip()
                if variant and variant not in preferred[current_term]:
                    preferred[current_term].append(variant)
                continue

        if section == "acronym_first_use" and indent >= 2 and stripped.startswith("-"):
            acronym = stripped.split("-", 1)[1].strip()
            if acronym:
                acronyms.append(acronym)

    return preferred, acronyms


def load_list(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def strip_tex(text: str) -> str:
    text = re.sub(r"(?<!\\)%.*", "", text)
    text = LATEX_COMMAND_RE.sub(" ", text)
    text = text.replace("{", " ").replace("}", " ")
    return re.sub(r"\s+", " ", text)


def contains_phrase(text: str, phrase: str) -> bool:
    pattern = re.compile(
        rf"(?<![A-Za-z0-9_-]){re.escape(phrase)}(?![A-Za-z0-9_-])",
        re.IGNORECASE,
    )
    return bool(pattern.search(text))


def count_phrase(text: str, phrase: str) -> int:
    pattern = re.compile(
        rf"(?<![A-Za-z0-9_-]){re.escape(phrase)}(?![A-Za-z0-9_-])",
        re.IGNORECASE,
    )
    return len(pattern.findall(text))


def first_phrase_index(text: str, phrase: str) -> int:
    pattern = re.compile(
        rf"(?<![A-Za-z0-9_-]){re.escape(phrase)}(?![A-Za-z0-9_-])",
        re.IGNORECASE,
    )
    match = pattern.search(text)
    return -1 if match is None else match.start()


def report_variant_usage(path: Path, text: str, preferred: dict[str, list[str]]) -> bool:
    findings = False
    for canonical, variants in preferred.items():
        used = [variant for variant in variants if contains_phrase(text, variant)]
        if len(set(item.lower() for item in used)) > 1:
            findings = True
            print(f"{path} :: mixed variants for '{canonical}' -> {', '.join(used)}")
    return findings


def report_banned_phrases(path: Path, text: str, banned_phrases: list[str]) -> bool:
    findings = False
    for phrase in banned_phrases:
        count = count_phrase(text, phrase)
        if count:
            findings = True
            print(f"{path} :: banned phrase '{phrase}' found {count} time(s)")
    return findings


def report_acronym_first_use(
    path: Path,
    text: str,
    acronyms: list[str],
    preferred: dict[str, list[str]],
) -> bool:
    findings = False
    lowered = text.lower()
    for acronym in acronyms:
        variants = preferred.get(acronym, [])
        long_forms = [
            variant
            for variant in variants
            if acronym.lower() not in variant.lower()
        ]
        acronym_index = first_phrase_index(lowered, acronym.lower())
        if acronym_index == -1 or not long_forms:
            continue
        earlier = lowered[:acronym_index]
        if not any(contains_phrase(earlier, form) for form in long_forms):
            findings = True
            print(f"{path} :: acronym '{acronym}' appears before any listed long form")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check terminology drift and banned phrases."
    )
    parser.add_argument("paths", nargs="+", help="Files to scan")
    parser.add_argument(
        "--terminology",
        default="style/terminology.yml",
        help="Terminology YAML file",
    )
    parser.add_argument(
        "--banned",
        default="style/banned_phrases.txt",
        help="Banned phrase file",
    )
    args = parser.parse_args()

    preferred, acronym_first_use = parse_terminology(Path(args.terminology))
    banned_phrases = load_list(Path(args.banned))

    findings = False
    for raw_path in args.paths:
        path = Path(raw_path)
        text = strip_tex(path.read_text(encoding="utf-8", errors="ignore"))
        findings |= report_variant_usage(path, text, preferred)
        findings |= report_banned_phrases(path, text, banned_phrases)
        findings |= report_acronym_first_use(path, text, acronym_first_use, preferred)

    if not findings:
        print("No terminology or phrase issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
