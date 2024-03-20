"""Token matching tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_token_matching(configuration):
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

    for expected_result, strings in test_cases:
        collection = localizationkit.LocalizedCollection(strings)
        test = localizationkit.tests.token_matching.TokenMatching(configuration, collection)
        result = test.execute()
        if expected_result:
            assert result.succeeded()
        else:
            assert result.succeeded() is False
