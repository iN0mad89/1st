# Architecture Overview

The classifier is organized as a set of small modules under `src/`.

```
src/
├── __init__.py
├── categories.py      # category definitions and priority
├── criteria.py        # load patterns from a YAML/JSON file
├── aggregator.py      # handle multi-file acts
├── classifier.py      # rule-based classification logic
├── explanation.py     # generate explanation for assigned categories
├── reporting.py       # output results to CSV/XLSX
└── main.py            # command line entry point
```

- **categories.py** – defines available categories and their priority.
- **criteria.py** – parses `criteria.yml` (derived from `Критерії категорій.docx`) to obtain regex patterns and keywords.
- **aggregator.py** – groups multiple text files that belong to a single act.
- **classifier.py** – applies rule-based matching to identify categories. Supports multi-category assignment respecting the priority order.
- **explanation.py** – collects matched patterns and features to justify the classification.
- **reporting.py** – writes results in CSV or XLSX format.
- **main.py** – provides a CLI interface and orchestrates the entire pipeline.

Additional directories:

- `data/` – place raw `.txt` files. Multi-file acts should share a common prefix.
- `output/` – generated classification reports.
- `tests/` – unit tests or gold standard evaluation data.

This layout allows updating `criteria.yml` without touching the Python code and simplifies future expansion (e.g., adding ML classifiers or a web service).
