import pathlib

from src.classifier import RuleBasedClassifier


def test_snippet_length():
    text = "a" * 300 + "інститут" + "b" * 300
    clf = RuleBasedClassifier(pathlib.Path('criteria.yml'))
    results = clf.classify(text)
    exp = results['Інститут']
    snippet = exp.snippets[0]
    assert 450 <= len(snippet) <= 460


def test_snippet_escapes_newlines():
    text = "start\nінститут\nend"
    clf = RuleBasedClassifier(pathlib.Path('criteria.yml'))
    results = clf.classify(text)
    snippet = results['Інститут'].snippets[0]
    assert "\\n" in snippet
    assert "\n" not in snippet
