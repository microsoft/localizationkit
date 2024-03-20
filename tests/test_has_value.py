"""Has value tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_has_value(configuration):
    """Test that has value works"""
    bad_values = [None, ""]
    good_values = [" ", "1", "Two three four", "     "]

    for value in bad_values:
        for language in ["en", "fr"]:
            string = localizationkit.LocalizedString("Key", value, "Comment", language)
            collection = localizationkit.LocalizedCollection([string])
            has_value_test = localizationkit.tests.has_value.HasValue(configuration, collection)
            result = has_value_test.execute()
            assert result.succeeded() is False

    for value in good_values:
        for language in ["en", "fr"]:
            string = localizationkit.LocalizedString("Key", value, "Comment", language)
            collection = localizationkit.LocalizedCollection([string])
            has_value_test = localizationkit.tests.has_value.HasValue(configuration, collection)
            result = has_value_test.execute()
            assert result.succeeded(), str(result.violations)
