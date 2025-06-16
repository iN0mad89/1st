from dataclasses import dataclass, field
from typing import List

@dataclass
class Explanation:
    category: str
    matches: List[str] = field(default_factory=list)
    patterns: List[str] = field(default_factory=list)

    def add_match(self, pattern: str, text: str) -> None:
        self.matches.append(text)
        self.patterns.append(pattern)

    def as_text(self) -> str:
        pairs = [f"{p} -> {m}" for p, m in zip(self.patterns, self.matches)]
        return '; '.join(pairs)
