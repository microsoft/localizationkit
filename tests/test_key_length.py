"""Key length tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class KeyLengthTests(unittest.TestCase):
    """Key length tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_key_length(self):
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
            key_length_test = localizationkit.tests.key_length.KeyLength(
                self.configuration, collection
            )
            result = key_length_test.execute()
            self.assertTrue(result.succeeded(), str(result.violations))

        for string in bad_strings:
            collection = localizationkit.LocalizedCollection([string])
            key_length_test = localizationkit.tests.key_length.KeyLength(
                self.configuration, collection
            )
            result = key_length_test.execute()
            self.assertFalse(result.succeeded())
