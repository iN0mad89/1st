import csv
from pathlib import Path
from typing import Dict

from .categories import CATEGORY_PRIORITY
from .explanation import Explanation


def write_csv(results: Dict[str, Dict[str, Explanation]], output_path: Path) -> None:
    with output_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        header = ['document'] + CATEGORY_PRIORITY + ['comment']
        writer.writerow(header)
        for doc_name, categories in results.items():
            row = [doc_name]
            for cat in CATEGORY_PRIORITY:
                if cat in categories:
                    row.append('1')
                else:
                    row.append('')
            explanations = [categories[cat].as_text() for cat in categories]
            row.append(' | '.join(explanations))
            writer.writerow(row)
