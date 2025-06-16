import argparse
from pathlib import Path

from .aggregator import gather_documents
from .categorizer import Categorizer
from .reporting import write_csv


def parse_args():
    p = argparse.ArgumentParser(description='Ukrainian legislative act classifier')
    p.add_argument('--input', type=Path, required=True, help='Directory with txt files')
    p.add_argument('--output', type=Path, required=True, help='Path to output CSV')
    p.add_argument('--criteria', type=Path, default=Path('criteria.yml'), help='Path to criteria YAML')
    return p.parse_args()


def main():
    args = parse_args()
    docs = gather_documents(args.input)
    categorizer = Categorizer.from_yaml(args.criteria)

    results = {}
    for name, text in docs:
        results[name] = categorizer.categorize(text)

    write_csv(results, args.output)
    print(f'Results written to {args.output}')


if __name__ == '__main__':
    main()
