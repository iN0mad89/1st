"""Rule-based classification of text documents."""

import re
from typing import Dict, List
from pathlib import Path

from .categories import CATEGORY_PRIORITY
from .criteria import CriteriaLoader
from .explanation import Explanation


class RuleBasedClassifier:
    """Classify text using regular expression rules for each category."""

    def __init__(self, criteria_path: Path):
        """Initialize the classifier with the path to a criteria file."""
        self.loader = CriteriaLoader(criteria_path)

    def classify(self, text: str) -> Dict[str, Explanation]:
        """Return explanations for categories matched in ``text``."""
        results: Dict[str, Explanation] = {}
        for category in CATEGORY_PRIORITY:
            patterns = self.loader.patterns_for(category)
            for pattern in patterns:
                m = re.search(pattern, text)
                if m:
                    if category not in results:
                        results[category] = Explanation(category)
                    results[category].add_match(pattern, m.group(0))
        return results
