"""Position identifier tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class PositionIdentifierTests(unittest.TestCase):
    """Position identifier tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_token_position_identifiers(self):
        """Test that token position identifiers works"""
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
                    "Key", "This is a string with one token: %@", "Some comment", "en"
                ),
            ),
            (
                True,
                localizationkit.LocalizedString(
                    "Key", "This is a string with two tokens: %1$@ %2$@", "Some comment", "en"
                ),
            ),
            (
                False,
                localizationkit.LocalizedString(
                    "Key",
                    "This is a string with two non-positional tokens: %@ %@",
                    "Some comment",
                    "en",
                ),
            ),
            (
                False,
                localizationkit.LocalizedString(
                    "Key", "This is a string with a skipped index: %1$@ %3$@", "Some comment", "en"
                ),
            ),
        ]

        for (expected_result, string) in test_cases:
            collection = localizationkit.LocalizedCollection([string])
            test = localizationkit.tests.token_position_identifiers.TokenPositionIdentifiers(
                self.configuration, collection
            )
            result = test.execute()
            if expected_result:
                self.assertTrue(result.succeeded())
            else:
                self.assertFalse(result.succeeded())
