"""Swift interpolation tests."""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class SwiftInterpolationTests(unittest.TestCase):
    """Swift interpolation tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_alternative_tokens(self):
        """Test that the Swift interpolation test works"""

        good_values = [
            "This is a string",
            "This is another string with (parentheses)",
            "This string has \\( but no closing parenthesis",
        ]

        bad_values = [
            "This string \\(has) interpolation",
            "This string has interpolation at the \\(end)",
            "\\(This) string has interpolation at the \\(start)",
            "\\(This) string has interpolation at both \\(ends)",
        ]

        for value in good_values:
            string = localizationkit.LocalizedString("Key", value, "Comment", "en")
            collection = localizationkit.LocalizedCollection([string])
            test = localizationkit.tests.swift_interpolation.SwiftInterpolation(
                self.configuration, collection
            )
            result = test.execute()
            self.assertTrue(result.succeeded(), str(result.violations))

        for value in bad_values:
            string = localizationkit.LocalizedString("Key", value, "Comment", "en")
            collection = localizationkit.LocalizedCollection([string])
            test = localizationkit.tests.swift_interpolation.SwiftInterpolation(
                self.configuration, collection
            )
            result = test.execute()
            self.assertFalse(result.succeeded())
