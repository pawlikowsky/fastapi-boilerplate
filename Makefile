PATH  := $(PATH)
SHELL := /bin/bash


run-dev:
	python main.py --reload --config development

run-prod:
	python main.py --config production

linter-check:
	ruff check

linter-format:
	ruff format

run-test:
	pytest

run-test-cov:
	pytest --cov