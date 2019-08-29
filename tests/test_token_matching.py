"""Token matching tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class TokenMatchingTests(unittest.TestCase):
    """Token matching tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_token_matching(self):
        """Test that token matching works"""
        test_cases = [
            (
                True,
                [
                    localizationkit.LocalizedString(
                        "Key", "This is a string with no tokens", "Some comment", "en"
                    ),
                    localizationkit.LocalizedString(
                        "Key", "This is a string with no tokens", "Some comment", "fr"
                    ),
                ],
            ),
            (
                True,
                [
                    localizationkit.LocalizedString(
                        "Key", "This is a string with a token: %@", "Some comment", "en"
                    ),
                    localizationkit.LocalizedString(
                        "Key", "This is a string with a token: %@", "Some comment", "fr"
                    ),
                ],
            ),
            (
                True,
                [
                    localizationkit.LocalizedString(
                        "Key",
                        "This is a string with multiple tokens: %1$d, %2$s, %3$@",
                        "Some comment",
                        "en",
                    ),
                    localizationkit.LocalizedString(
                        "Key",
                        "This is a string with multiple tokens: %1$d, %2$s, %3$@",
                        "Some comment",
                        "fr",
                    ),
                ],
            ),
            (
                False,
                [
                    localizationkit.LocalizedString(
                        "Key",
                        "This is a string with multiple tokens: %1$d, %2$s, %3$@, %4$@",
                        "Some comment",
                        "en",
                    ),
                    localizationkit.LocalizedString(
                        "Key",
                        "This is a string with multiple tokens: %1$d, %2$s, %3$@",
                        "Some comment",
                        "fr",
                    ),
                ],
            ),
        ]

        for (expected_result, strings) in test_cases:
            collection = localizationkit.LocalizedCollection(strings)
            test = localizationkit.tests.token_matching.TokenMatching(
                self.configuration, collection
            )
            result = test.execute()
            if expected_result:
                self.assertTrue(result.succeeded())
            else:
                self.assertFalse(result.succeeded())
