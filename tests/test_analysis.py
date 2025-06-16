import csv
from pathlib import Path

from src.analysis import count_categories


def test_count_categories(tmp_path: Path) -> None:
    csv_path = tmp_path / "results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["document", "Нечинний", "Інститут", "comment"])
        writer.writerow(["d1", "1", "", ""])
        writer.writerow(["d2", "", "1", ""])
        writer.writerow(["d3", "1", "1", ""])

    counts = count_categories(csv_path)
    assert counts == {"Нечинний": 2, "Інститут": 2}
