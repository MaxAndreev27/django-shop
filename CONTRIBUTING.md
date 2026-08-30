# Contributing to django-shop

Thank you for contributing. This project welcomes bug reports, documentation improvements, tests, and focused feature proposals.

## Before You Start

- Read the [Code of Conduct](CODE_OF_CONDUCT.md).
- Search existing issues and pull requests to avoid duplicate work.
- For a substantial change, open an issue first so the approach can be discussed.

## Development Setup

Follow the local setup steps in the [README](README.md). Use a virtual environment, install `requirements.txt`, and start Redis before running Celery tasks.

## Making Changes

1. Create a branch from `main` with a descriptive name.
2. Keep changes focused on one concern.
3. Add or update tests when behavior changes.
4. Run the checks below before opening a pull request.

## Checks

```bash
python manage.py check
python manage.py test
```

If your change affects translations, update the relevant message files and verify both supported languages.

## Pull Requests

Use the pull request template and explain the problem, solution, and testing performed. Do not include credentials, Stripe keys, tokens, or personal data. A maintainer may request changes before merging.

## Reporting Security Issues

Do not report suspected vulnerabilities in public issues. Use the process described in [SECURITY.md](SECURITY.md).
