#!/bin/bash

set -e

uv run pytest tests --cov=localizationkit --cov-report html --cov-report xml --doctest-modules --junitxml=junit/test-results.xml
