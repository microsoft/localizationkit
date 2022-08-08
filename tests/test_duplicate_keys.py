"""Duplicate key tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_duplicate_keys(configuration):
    """Test that comment similarity works"""
    good_checks = [
        [
            localizationkit.LocalizedString("Key", "Value", "Comment", "en"),
            localizationkit.LocalizedString("Key", "Value", "Comment", "fr"),
        ],
        [
            localizationkit.LocalizedString("Key", "Value", "Comment", "en"),
            localizationkit.LocalizedString("Keys", "Value", "Comment", "en"),
        ],
    ]

    bad_checks = [
        [
            localizationkit.LocalizedString("Key", "Value", "Comment", "en"),
            localizationkit.LocalizedString("Key", "Value", "Comment", "en"),
        ],
        [
            localizationkit.LocalizedString("", "Value", "Comment", "en"),
            localizationkit.LocalizedString("", "Value", "Comment", "en"),
        ],
    ]

    for strings in good_checks:
        collection = localizationkit.LocalizedCollection(strings)
        test = localizationkit.tests.duplicate_keys.DuplicateKeys(configuration, collection)
        result = test.execute()
        assert result.succeeded(), str(result.violations)

    for strings in bad_checks:
        collection = localizationkit.LocalizedCollection(strings)
        test = localizationkit.tests.duplicate_keys.DuplicateKeys(configuration, collection)
        result = test.execute()
        assert result.succeeded() is not True
