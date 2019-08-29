"""Has value tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class HasValueTests(unittest.TestCase):
    """Has value tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_has_value(self):
        """Test that has value works"""
        bad_values = [None, ""]
        good_values = [" ", "1", "Two three four", "     "]

        for value in bad_values:
            string = localizationkit.LocalizedString("Key", value, "Comment", "en")
            collection = localizationkit.LocalizedCollection([string])
            has_value_test = localizationkit.tests.has_value.HasValue(
                self.configuration, collection
            )
            result = has_value_test.execute()
            self.assertFalse(result.succeeded())

        for value in good_values:
            string = localizationkit.LocalizedString("Key", value, "Comment", "en")
            collection = localizationkit.LocalizedCollection([string])
            has_value_test = localizationkit.tests.has_value.HasValue(
                self.configuration, collection
            )
            result = has_value_test.execute()
            self.assertTrue(result.succeeded(), str(result.violations))
