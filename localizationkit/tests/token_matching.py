"""Token matching."""

from typing import Any, Dict, List

from localizationkit.tests.test_case import LocalizationTestCase


class TokenMatching(LocalizationTestCase):
    """Check the tokens in strings match between languages."""

    @classmethod
    def name(cls) -> str:
        return "token_matching"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {"allow_missing_defaults": False}

    def run_test(self) -> List[str]:

        violations = []

        allow_missing_defaults = self.get_setting("allow_missing_defaults")

        default_token_map = {}

        for string in self.collection.strings_for_language(self.configuration.default_language()):
            default_token_map[string.key] = sorted(string.tokens())

        for language_code in self.collection.languages():

            if language_code == self.configuration.default_language():
                continue

            for string in self.collection.strings_for_language(language_code):

                default_tokens = default_token_map.get(string.key, None)

                # Sometimes a string can be removed from the default language
                # before it is removed from other languages (due to automation)
                # If the setting is set, we can allow it to be removed,
                # otherwise, it's an error
                if default_tokens is None and allow_missing_defaults:
                    continue

                translation_tokens = sorted(string.tokens())
                if default_tokens != translation_tokens:
                    violations.append(
                        f"The tokens for {language_code} do not match the default language: {string.key}"
                    )

        return violations
