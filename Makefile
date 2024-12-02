
PYTHON = python3


install:
	uv --version
	pre-commit --version
	pre-commit install
	pre-commit autoupdate
	uv tool install ruff
	uv tool install mypy
	uv sync --no-dev

run:
	uv sync --no-dev
	uv run python -m app

check: chaos-check app-check

build: chaos-build app-build

lint:
	ruff format
	# ruff check

clean:
	rm -rf .venv/
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf dist/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	rm -f .coverage
	rm -rf coverage/
	rm -rf .pytest_cache/

bootstrap:
	rm -rf .venv/
	$(PYTHON) -m venv .venv/
	.venv/bin/pip install pipx
	.venv/bin/pipx install pre-commit || true
	.venv/bin/pipx install uv || true
	rm -rf .venv/

.PHONY: install clean bootstrap


# neural chaos

chaos-check:
	uv run pytest packages/neural_chaos/tests/ --cov=packages/neural_chaos/src/ --cov-report=xml:coverage/neural_chaos.xml --cov-report=term

chaos-build:
	uv build --directory packages/neural_chaos/


# application

app-check:
	uv sync --dev
	uv run pytest tests/ --cov=src/ --cov-report=xml:coverage/app.xml --cov-report=term

app-build:
	uv build
