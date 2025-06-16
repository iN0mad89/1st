# -*- coding: utf-8 -*-
"""Simple categorizer with built-in patterns derived from `Критерії категорій.docx`.

This module provides a :class:`Categorizer` that applies regular expression
patterns to a text and returns the matched categories with explanations.

The base patterns are intentionally minimal and can be extended externally.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Iterable

from .categories import CATEGORY_PRIORITY
from .explanation import Explanation

# Basic regex patterns. These approximate the guidance from
# ``Критерії категорій.docx`` and can be refined by editing this map or by
# providing a custom patterns dictionary when creating ``Categorizer``.
BASE_PATTERNS: Dict[str, List[str]] = {
    "Нечинний": [
        r"(?i)втратив\s+чинність",
        r"(?i)втратив\s+силу",
        r"(?i)не\s+чинний",
    ],
    "Бюджет": [
        r"(?i)державн.?\s+бюджет",
        r"(?i)розподіл\s+коштів",
    ],
    "Науковець": [
        r"(?i)науков(?:ець|ці|ців)",
        r"(?i)дослідницьк",
        r"(?i)вчений",
    ],
    "Інститут": [
        r"(?i)інститут",
        r"(?i)академі",
    ],
    "базис ННТД": [
        r"(?i)науково[-\s]технічн",
        r"(?i)технологічн",
    ],
    "Регулювання": [
        r"(?i)порядок",
        r"(?i)регулює",
        r"(?i)визначає",
    ],
    "Статус": [
        r"(?i)статус",
        r"(?i)правов(?:ий|ого)\s+статусу",
    ],
    "Омонім": [
        r"(?i)надвірний",
        r"(?i)фізика",
    ],
}


class Categorizer:
    """Rule-based text categorizer."""

    def __init__(self, patterns: Dict[str, List[str]] | None = None) -> None:
        self.patterns = patterns or BASE_PATTERNS

    def categorize(self, text: str) -> Dict[str, Explanation]:
        """Return categories matched in ``text`` along with explanations."""
        results: Dict[str, Explanation] = {}
        for cat in CATEGORY_PRIORITY:
            for pattern in self.patterns.get(cat, []):
                m = re.search(pattern, text)
                if m:
                    if cat not in results:
                        results[cat] = Explanation(cat)
                    results[cat].add_match(pattern, m.group(0))
        return results

    def categorize_documents(
        self, docs: Iterable[tuple[str, str]]
    ) -> Dict[str, Dict[str, Explanation]]:
        """Categorize multiple documents given as ``(name, text)`` tuples."""
        out: Dict[str, Dict[str, Explanation]] = {}
        for name, text in docs:
            out[name] = self.categorize(text)
        return out

    @classmethod
    def from_yaml(cls, path: Path) -> "Categorizer":
        """Create categorizer using patterns loaded from a YAML file."""
        from .criteria import CriteriaLoader

        loader = CriteriaLoader(path)
        patterns = {
            cat: loader.patterns_for(cat) for cat in CATEGORY_PRIORITY
        }
        return cls(patterns)
