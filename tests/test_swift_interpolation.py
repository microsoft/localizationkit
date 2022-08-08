"""Swift interpolation tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_alternative_tokens(configuration):
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
            configuration, collection
        )
        result = test.execute()
        assert result.succeeded(), str(result.violations)

    for value in bad_values:
        string = localizationkit.LocalizedString("Key", value, "Comment", "en")
        collection = localizationkit.LocalizedCollection([string])
        test = localizationkit.tests.swift_interpolation.SwiftInterpolation(
            configuration, collection
        )
        result = test.execute()
        assert result.succeeded() is False
