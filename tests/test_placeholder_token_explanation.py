"""Placeholder token explanation tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class PlaceholderTokenExplanationTests(unittest.TestCase):
    """Placeholder token explanation tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_placeholder_token_explanation(self):
        """Test that all placeholder token explanations exists in comments"""
        test_cases = [
            (
                True,
                localizationkit.LocalizedString(
                    "Key", "This is a string with no tokens", "Some comment", "en"
                ),
            ),
            (
                True,
                localizationkit.LocalizedString(
                    "Key",
                    "This is a string with one token: %@",
                    "Some comment %@ token explanation",
                    "en",
                ),
            ),
            (
                True,
                localizationkit.LocalizedString(
                    "Key",
                    "This is a string with two tokens: %1$@ %2$@",
                    "Some comment %1$@ token explanantion %2$@ token explanantion",
                    "en",
                ),
            ),
            (
                False,
                localizationkit.LocalizedString(
                    "Key",
                    "This is a string with two tokens: %1$@ %2$@",
                    "Some comment missing all token explanation",
                    "en",
                ),
            ),
            (
                False,
                localizationkit.LocalizedString(
                    "Key",
                    "This is a string with two tokens: %1$@ %2$@",
                    "Some comment %@ token explanation missing some token explanantion",
                    "en",
                ),
            ),
            (
                False,
                localizationkit.LocalizedString(
                    "Key", "This is a string", "Some comment %@ extra token explanation", "en"
                ),
            ),
        ]

        for expected_result, string in test_cases:
            collection = localizationkit.LocalizedCollection([string])
            test = localizationkit.tests.placeholder_token_explanation.PlaceholderTokenExplanation(
                self.configuration, collection
            )
            result = test.execute()
            self.assertEqual(expected_result, result.succeeded())
