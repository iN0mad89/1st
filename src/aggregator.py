from pathlib import Path
from typing import List, Tuple


def gather_documents(input_dir: Path) -> List[Tuple[str, str]]:
    """Return list of ``(doc_name, text)`` combining files with the same stem.

    Files are expected to be UTF-8 encoded. If a file fails to decode with
    UTF-8, the function will retry using common Windows encodings such as
    ``cp1251``. As a last resort the file is read in binary mode and decoded
    using ``errors='replace'`` so decoding never raises ``UnicodeDecodeError``.
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
