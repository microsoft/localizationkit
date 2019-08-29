"""Objective-C alternative token tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class ObjectivecAlternativeTokenTests(unittest.TestCase):
    """Objective-C alternative token tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_alternative_tokens(self):
        """Test that the Objective-C alternative token test works"""

        good_values = ["%@", "%1$@", "%%", "%%1"]

        bad_values = ["%1@", "%1@ %2@"]

        for value in good_values:
            string = localizationkit.LocalizedString("Key", value, "Comment", "en")
            collection = localizationkit.LocalizedCollection([string])
            test = localizationkit.tests.objectivec_alternative_tokens.ObjectivecAlternativeTokens(
                self.configuration, collection
            )
            result = test.execute()
            self.assertTrue(result.succeeded(), str(result.violations))

        for value in bad_values:
            string = localizationkit.LocalizedString("Key", value, "Comment", "en")
            collection = localizationkit.LocalizedCollection([string])
            test = localizationkit.tests.objectivec_alternative_tokens.ObjectivecAlternativeTokens(
                self.configuration, collection
            )
            result = test.execute()
            self.assertFalse(result.succeeded())
