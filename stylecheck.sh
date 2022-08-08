#!/bin/bash

python -m black -l 100 localizationkit localizationkit/tests tests
python -m pylint --rcfile=pylintrc localizationkit tests
python -m mypy --ignore-missing-imports localizationkit/ tests/
