"""Duplicate key tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class DuplicateKeyTests(unittest.TestCase):
    """Duplicate key tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_duplicate_keys(self):
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
            test = localizationkit.tests.duplicate_keys.DuplicateKeys(
                self.configuration, collection
            )
            result = test.execute()
            self.assertTrue(result.succeeded(), str(result.violations))

        for strings in bad_checks:
            collection = localizationkit.LocalizedCollection(strings)
            test = localizationkit.tests.duplicate_keys.DuplicateKeys(
                self.configuration, collection
            )
            result = test.execute()
            self.assertFalse(result.succeeded())
