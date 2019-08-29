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
        return {}

    def run_test(self) -> List[str]:

        violations: List[str] = []

        for string in self.collection.strings_for_language(self.configuration.default_language()):

            if string.value is None or len(string.value) == 0:
                violations.append(f"Value was empty: {string}")
                continue

        return violations
