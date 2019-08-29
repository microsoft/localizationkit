"""Checks key length."""

from typing import Any, Dict, List

from localizationkit.tests.test_case import LocalizationTestCase


class KeyLength(LocalizationTestCase):
    """Check the length of the keys."""

    @classmethod
    def name(cls) -> str:
        return "key_length"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {"minimum": -1, "maximum": -1}

    def run_test(self) -> List[str]:

        minimum_length = self.get_setting("minimum")
        maximum_length = self.get_setting("maximum")

        violations: List[str] = []

        # Short circuit for the non-bound case
        if minimum_length < 0 and maximum_length < 0:
            return violations

        for string in self.collection.strings_for_language(self.configuration.default_language()):

            key = string.key

            if key is None:
                violations.append(f"Key was empty: {string}")
                continue

            if len(key) < minimum_length >= 0:
                violations.append(f"Key is shorter than minimum of {minimum_length}: {string}")

            if len(key) > maximum_length >= 0:
                violations.append(f"Key is longer than maximum of {maximum_length}: {string}")

        return violations
