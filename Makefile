RUFF_FORMAT=grouped
.DEFAULT_GOAL := all

ruff:
	poetry run ruff check . --format=$(RUFF_FORMAT)
black:
	poetry run black . --check
mypy:
	poetry run mypy --install-types --non-interactive .
bandit:
	poetry run bandit -r . -x ./tests,./test
test:
	poetry run pytest tests/

lint: ruff black mypy
audit: bandit
tests: test
all: lint audit tests
