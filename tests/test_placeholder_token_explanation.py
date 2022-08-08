"""Placeholder token explanation tests."""


import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_placeholder_token_explanation(configuration):
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
            configuration, collection
        )
        result = test.execute()
        assert expected_result == result.succeeded()
