from pathlib import Path
from typing import Dict, List


class CriteriaLoader:
    def __init__(self, path: Path):
        self.path = path
        self.criteria = self._load()

    def _load(self) -> Dict[str, Dict[str, List[str]]]:
        data: Dict[str, Dict[str, List[str]]] = {}
        current = None
        for line in self.path.read_text(encoding='utf-8').splitlines():
            line = line.rstrip()
            if not line or line.startswith('#'):
                continue
            if not line.startswith(' '):
                current = line.strip(':')
                data[current] = {'patterns': []}
            elif line.strip().startswith('-') and current:
                pattern = line.split('-', 1)[1].strip().strip("'\"")
                data[current]['patterns'].append(pattern)
        return data

    def patterns_for(self, category: str) -> List[str]:
        return self.criteria.get(category, {}).get('patterns', [])
