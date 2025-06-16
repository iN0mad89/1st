"""Data structure describing why a document was assigned to a category."""

from dataclasses import dataclass, field
from typing import List

@dataclass
class Explanation:
    """Collection of matches that justify a category."""

    category: str
    matches: List[str] = field(default_factory=list)
    patterns: List[str] = field(default_factory=list)
    snippets: List[str] = field(default_factory=list)

    def add_match(self, pattern: str, text: str, snippet: str) -> None:
        """Record a ``pattern`` that matched ``text`` with surrounding ``snippet``."""
        self.matches.append(text)
        self.patterns.append(pattern)
        self.snippets.append(snippet)

    def as_text(self) -> str:
        """Return a semicolon-separated summary of matches using snippets."""
        pairs = [f"{p} -> {s}" for p, s in zip(self.patterns, self.snippets)]
        return '; '.join(pairs)
