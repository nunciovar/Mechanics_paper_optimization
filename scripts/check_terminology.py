#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


LINE_RE = re.compile(r"^(?P<indent>\s*)(?P<body>.*)$")


def parse_terminology(path: Path) -> tuple[dict[str, list[str]], list[str]]:
    preferred: dict[str, list[str]] = {}
    acronym_first_use: list[str] = []
    section = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        match = LINE_RE.match(line)
        assert match
        indent = len(match.group("indent"))
        body = match.group("body")

        if indent == 0 and body.endswith(":"):
            section = body[:-1]
            continue

        if section == "preferred" and indent >= 2 and ":" in body:
            canonical, variants = body.split(":", 1)
            preferred[canonical.strip()] = [item.strip() for item in variants.split("|") if item.strip()]
        elif section == "acronym_first_use" and indent >= 2 and body.strip().startswith("-"):
            acronym_first_use.append(body.split("-", 1)[1].strip())

    return preferred, acronym_first_use


def load_list(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")]


def strip_tex(text: str) -> str:
    text = re.sub(r"(?<!\\)%.*", "", text)
    text = re.sub(r"\\[A-Za-z@]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?", " ", text)
    text = text.replace("{", " ").replace("}", " ")
    return re.sub(r"\s+", " ", text)


def report_variant_usage(path: Path, text: str, preferred: dict[str, list[str]]) -> bool:
    lowered = text.lower()
    findings = False
    for canonical, variants in preferred.items():
        used = [variant for variant in variants if variant.lower() in lowered]
        if len(used) > 1:
            findings = True
            print(f"{path} :: mixed variants for '{canonical}' -> {', '.join(used)}")
    return findings


def report_banned_phrases(path: Path, text: str, banned_phrases: list[str]) -> bool:
    lowered = text.lower()
    findings = False
    for phrase in banned_phrases:
        count = lowered.count(phrase.lower())
        if count:
            findings = True
            print(f"{path} :: banned phrase '{phrase}' found {count} time(s)")
    return findings


def report_acronym_first_use(path: Path, text: str, acronyms: list[str], preferred: dict[str, list[str]]) -> bool:
    findings = False
    lowered = text.lower()
    for acronym in acronyms:
        canonical_variants = preferred.get(acronym, [])
        long_forms = [v for v in canonical_variants if v.upper() != acronym.upper()]
        acronym_index = lowered.find(acronym.lower())
        if acronym_index == -1 or not long_forms:
            continue
        earlier = lowered[:acronym_index]
        if not any(form.lower() in earlier for form in long_forms):
            findings = True
            print(f"{path} :: acronym '{acronym}' appears before any listed long form")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check terminology drift and phrase bans.")
    parser.add_argument("paths", nargs="+", help="Files to scan")
    parser.add_argument("--terminology", default="style/terminology.yml", help="Terminology file")
    parser.add_argument("--banned", default="style/banned_phrases.txt", help="Banned phrase file")
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
