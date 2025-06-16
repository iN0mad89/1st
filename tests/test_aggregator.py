import tempfile
from pathlib import Path

from src.aggregator import gather_documents


def test_cp1251_file_reading():
    text = 'Привет мир'
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        file = path / 'doc1_part1.txt'
        file.write_bytes(text.encode('cp1251'))

        docs = gather_documents(path)
        assert docs == [('doc1', text)]
