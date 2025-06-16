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


def test_stable_document_order():
    """Documents should be returned in alphabetical order regardless of creation order."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)

        # Create files in reverse alphabetical order to simulate unpredictable filesystem ordering
        (path / 'doc2_part2.txt').write_text('two_part2')
        (path / 'doc2_part1.txt').write_text('two_part1')
        (path / 'doc1_part2.txt').write_text('one_part2')
        (path / 'doc1_part1.txt').write_text('one_part1')

        docs = gather_documents(path)

        assert docs == [
            ('doc1', 'one_part1\none_part2'),
            ('doc2', 'two_part1\ntwo_part2'),
        ]
