"""Duplicate keys."""

from typing import Any, Dict, List, Set

from localizationkit.tests.test_case import LocalizationTestCase


class DuplicateKeys(LocalizationTestCase):
    """Check for duplicate keys."""

    @classmethod
    def name(cls) -> str:
        return "duplicate_keys"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {"all_languages": False}

    def run_test(self) -> List[str]:

        violations = []

        all_languages = self.get_setting("all_languages")

        if all_languages:
            languages_to_check = self.collection.languages()
        else:
            languages_to_check = [self.configuration.default_language()]

        for language in languages_to_check:

            keys: Set[str] = set()

            for string in self.collection.strings_for_language(language):

                if string.key in keys:
                    violations.append(
                        f"The key '{string.key}' appears for multiple strings. e.g. {string}"
                    )
                    continue

                keys.add(string.key)

        return violations
