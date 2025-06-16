from collections import Counter
import csv
from pathlib import Path
from typing import Dict, Optional


def count_categories(csv_path: Path) -> Dict[str, int]:
    """Return document counts per category from a classification CSV."""
    with csv_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        categories = header[1:-1]
        counter: Counter[str] = Counter()
        for row in reader:
            for cat, value in zip(categories, row[1:-1]):
                if value.strip():
                    counter[cat] += 1
    return dict(counter)


def plot_counts(counts: Dict[str, int], output_path: Optional[Path] = None) -> None:
    """Plot a bar chart of ``counts`` using matplotlib if available."""
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("matplotlib is required for plot_counts()") from e

    categories = list(counts.keys())
    values = [counts[c] for c in categories]
    plt.bar(categories, values)
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    plt.close()
