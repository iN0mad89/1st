"""Data structure describing why a document was assigned to a category."""

from dataclasses import dataclass, field
from typing import List

@dataclass
class Explanation:
    """Collection of matches that justify a category."""

    category: str
    matches: List[str] = field(default_factory=list)
    patterns: List[str] = field(default_factory=list)

    def add_match(self, pattern: str, text: str) -> None:
        """Record a ``pattern`` that matched the provided text fragment."""
        self.matches.append(text)
        self.patterns.append(pattern)

    def as_text(self) -> str:
        """Return a semicolon-separated summary of matches."""
        pairs = [f"{p} -> {m}" for p, m in zip(self.patterns, self.matches)]
        return '; '.join(pairs)
