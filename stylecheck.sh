#!/bin/bash

set -e

uv run ruff check localizationkit tests
uv run ruff format --check localizationkit tests
uv run mypy localizationkit/ tests/
