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


def test_utf8_multi_file_assembly():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        part1 = path / 'doc1_part1.txt'
        part2 = path / 'doc1_part2.txt'
        part1.write_text('hello')
        part2.write_text('world')

        docs = gather_documents(path)
        assert docs == [('doc1', 'hello\nworld')]
