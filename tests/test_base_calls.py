"""Base call tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_base_call(configuration):
    """Test run_tests."""
    strings = localizationkit.LocalizedString("Key", "Value", "Comment", "en")
    collection = localizationkit.LocalizedCollection([strings])
    results = localizationkit.run_tests(configuration, collection)
    assert len(results) > 0
