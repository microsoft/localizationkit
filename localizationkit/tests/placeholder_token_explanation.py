"""Placeholder token explanation."""

from typing import Any

from localizationkit.tests.test_case import LocalizationTestCase


class PlaceholderTokenExplanation(LocalizationTestCase):
    """Check the placeholder tokens in strings have explanation in comments."""

    @classmethod
    def name(cls) -> str:
        return "placeholder_token_explanation"

    @classmethod
    def default_settings(cls) -> dict[str, Any]:
        return {}

    @classmethod
    def is_opt_in(cls) -> bool:
        return True

    def run_test(self) -> list[tuple[str, str]]:

        violations = []

        for string in self.collection.localized_strings:
            tokens = set(string.tokens())
            comment_tokens = set(string.comment_tokens())

            extra_in_tokens = tokens - comment_tokens
            extra_in_comments = comment_tokens - tokens

            if len(extra_in_tokens) != 0:
                violations.append(
                    (
                        f"Tokens are not described in the comment ({extra_in_tokens}): {string}",
                        string.language_code,
                    )
                )

            if len(extra_in_comments) != 0:
                violations.append(
                    (
                        f"Extra tokens appear in the comment ({extra_in_comments}): {string}",
                        string.language_code,
                    )
                )

        return violations
