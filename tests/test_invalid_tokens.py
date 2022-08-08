"""Invalid token tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_invalid_tokens(configuration):
    """Test that invalid tokens works"""
    test_cases = [
        (
            False,
            localizationkit.LocalizedString(
                "Key", "This is a string with no tokens", "Some comment", "en"
            ),
        ),
        (False, localizationkit.LocalizedString("Key", "%", "Some comment", "en")),
        (False, localizationkit.LocalizedString("Key", "25%", "Some comment", "en")),
        (False, localizationkit.LocalizedString("Key", "This is 25%", "Some comment", "en")),
        (
            False,
            localizationkit.LocalizedString("Key", "This is 25% off", "Some comment", "en"),
        ),
        (True, localizationkit.LocalizedString("Key", "This is %* off", "Some comment", "en")),
        (True, localizationkit.LocalizedString("Key", "This is %! off", "Some comment", "en")),
        (True, localizationkit.LocalizedString("Key", "This is %() off", "Some comment", "en")),
        (False, localizationkit.LocalizedString("Key", "This is % off", "Some comment", "en")),
        (False, localizationkit.LocalizedString("Key", "This is %% off", "Some comment", "en")),
        (False, localizationkit.LocalizedString("Key", "This is %d off", "Some comment", "en")),
    ]

    for (has_invalid_tokens, string) in test_cases:
        collection = localizationkit.LocalizedCollection([string])
        test = localizationkit.tests.invalid_tokens.InvalidTokens(configuration, collection)
        result = test.execute()
        if has_invalid_tokens:
            assert result.succeeded() is False
        else:
            assert result.succeeded()
