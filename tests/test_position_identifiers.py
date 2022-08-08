"""Position identifier tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_token_position_identifiers(configuration):
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
            configuration, collection
        )
        result = test.execute()
        if expected_result:
            assert result.succeeded()
        else:
            assert result.succeeded() is False
