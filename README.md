# Ukrainian Legislative Act Classifier

This project provides a modular system for rule-based classification of Ukrainian legislative texts. The system supports multi-file acts, configurable categories, and produces CSV/XLSX reports. It is designed to be extensible for future ML/LLM approaches or web/API integration.

## Project structure

- `src/` – core modules for classification
- `data/` – example input texts
- `output/` – generated reports
- `docs/` – design documents and guidelines
- `tests/` – placeholder for test cases

## Quick start

```bash
python -m src.main --input data --output output/results.csv
```

This runs the rule-based classifier on all text files under `data/` and writes the classification results to `output/results.csv`.

The CSV file contains a `comment` column that lists each matched pattern along
with a short snippet of the surrounding text (about 450 characters around the
match). Newlines inside these snippets are escaped as ``\n`` so each row stays
on a single line. This provides context for why a category was assigned.

See `docs/architecture.md` for an overview of the modules and `docs/roadmap.md` for ideas on next steps.
