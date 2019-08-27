#!/bin/bash

pushd "${VIRTUAL_ENV}" > /dev/null

python -m black -l 100 localizationkit/*.py localizationkit/tests/*.py tests/*.py

python -m pylint --rcfile=pylintrc localizationkit
python -m mypy --ignore-missing-imports localizationkit/

python -m pylint --rcfile=pylintrc tests
python -m mypy --ignore-missing-imports tests/

popd > /dev/null

