"""Key length tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_key_length(configuration):
    """Test run_tests."""
    good_strings = [
        localizationkit.LocalizedString("Key", "Value", "Comment", "en"),
        localizationkit.LocalizedString("Longer key", "Value", "Comment", "en"),
        localizationkit.LocalizedString(
            "This is a decently long key to run tests on", "Value", "Comment", "en"
        ),
    ]

    bad_strings = [
        localizationkit.LocalizedString(None, "Value", "Comment", "en"),
        localizationkit.LocalizedString("", "Value", "Comment", "en"),
        localizationkit.LocalizedString("a", "Value", "Comment", "en"),
        localizationkit.LocalizedString("ab", "Value", "Comment", "en"),
    ]

    for string in good_strings:
        collection = localizationkit.LocalizedCollection([string])
        key_length_test = localizationkit.tests.key_length.KeyLength(configuration, collection)
        result = key_length_test.execute()
        assert result.succeeded(), str(result.violations)

    for string in bad_strings:
        collection = localizationkit.LocalizedCollection([string])
        key_length_test = localizationkit.tests.key_length.KeyLength(configuration, collection)
        result = key_length_test.execute()
        assert result.succeeded() is False
