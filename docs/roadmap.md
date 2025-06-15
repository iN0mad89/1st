# Roadmap and Next Steps

1. **Refine Rule-Based Patterns**
   - Convert `Критерії категорій.docx` to `criteria.yml` with regex patterns.
   - Extend test cases in `tests/` with gold standard labels for evaluation.

2. **Add Machine Learning / LLM Support**
   - Collect labeled data from rule-based classifier plus manual verification.
   - Train a traditional ML model (e.g., logistic regression, SVM) using scikit-learn.
   - Experiment with LLM embeddings to capture semantic signals.
   - Implement a hybrid approach that combines rule-based and ML predictions.

3. **Web/API Integration**
   - Wrap the classifier in a Flask/FastAPI service for integration with other systems.
   - Provide endpoints for uploading documents and retrieving classification results.
   - Add a simple web UI for manual review and feedback.

This project is intentionally modular to make these extensions straightforward.
