"""Objective-C alternative token tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_alternative_tokens(configuration):
    """Test that the Objective-C alternative token test works"""

    good_values = ["%@", "%1$@", "%%", "%%1"]

    bad_values = ["%1@", "%1@ %2@"]

    for value in good_values:
        string = localizationkit.LocalizedString("Key", value, "Comment", "en")
        collection = localizationkit.LocalizedCollection([string])
        test = localizationkit.tests.objectivec_alternative_tokens.ObjectivecAlternativeTokens(
            configuration, collection
        )
        result = test.execute()
        assert result.succeeded(), str(result.violations)

    for value in bad_values:
        string = localizationkit.LocalizedString("Key", value, "Comment", "en")
        collection = localizationkit.LocalizedCollection([string])
        test = localizationkit.tests.objectivec_alternative_tokens.ObjectivecAlternativeTokens(
            configuration, collection
        )
        result = test.execute()
        assert result.succeeded() is False
