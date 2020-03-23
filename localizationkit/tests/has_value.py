"""Checks that the value is set."""

from typing import Any, Dict, List

from localizationkit.tests.test_case import LocalizationTestCase


class HasValue(LocalizationTestCase):
    """Check the length of the values."""

    @classmethod
    def name(cls) -> str:
        return "has_value"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {"default_language_only": False}

    def run_test(self) -> List[str]:

        violations: List[str] = []

        if self.get_setting("default_language_only"):
            test_collection = self.collection.strings_for_language(self.configuration.default_language())
        else:
            test_collection = self.collection.localized_strings

        for string in test_collection:
            if string.value is None or len(string.value) == 0:
                violations.append(f"Value was empty: {string}")
                continue

        return violations
