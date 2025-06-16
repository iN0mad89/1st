from pathlib import Path
from typing import List, Tuple


def gather_documents(input_dir: Path) -> List[Tuple[str, str]]:
    """Return list of ``(doc_name, text)`` combining files with the same stem.

    Each file is decoded as UTF-8 first. On ``UnicodeDecodeError`` the
    function attempts ``cp1251``. If decoding still fails the file is read in
    binary mode and decoded with ``errors='replace'`` so an exception is never
    raised.
    """
    groups = {}
    for path in input_dir.glob('*.txt'):
        stem = path.stem.split('_')[0]  # assumes `act1_part1.txt` pattern
        groups.setdefault(stem, []).append(path)

    documents = []
    for stem, files in groups.items():
        contents = []
        for file in sorted(files):
            try:
                contents.append(file.read_text(encoding='utf-8'))
            except UnicodeDecodeError:
                try:
                    contents.append(file.read_text(encoding='cp1251'))
                except UnicodeDecodeError:
                    with file.open('rb') as fh:
                        data = fh.read()
                    contents.append(data.decode('utf-8', errors='replace'))
        documents.append((stem, '\n'.join(contents)))
    return documents
