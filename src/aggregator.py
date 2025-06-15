from pathlib import Path
from typing import List, Tuple


def gather_documents(input_dir: Path) -> List[Tuple[str, str]]:
    """Return list of (doc_name, text) combining files with the same stem."""
    groups = {}
    for path in input_dir.glob('*.txt'):
        stem = path.stem.split('_')[0]  # assumes `act1_part1.txt` pattern
        groups.setdefault(stem, []).append(path)

    documents = []
    for stem, files in groups.items():
        contents = []
        for file in sorted(files):
            contents.append(file.read_text(encoding='utf-8'))
        documents.append((stem, '\n'.join(contents)))
    return documents
