"""Token matching."""

from typing import Any

from localizationkit.tests.test_case import LocalizationTestCase


class TokenAdjacency(LocalizationTestCase):
    """Check that nothing is directly adjacent to a token. e.g. Don't allow `You have new %@s` for plurals."""

    @classmethod
    def name(cls) -> str:
        return "token_adjacency"

    @classmethod
    def is_opt_in(cls) -> bool:
        """Check if the test is opt in or not."""
        return True

    @classmethod
    def default_settings(cls) -> dict[str, Any]:
        return {"only_check_language": None}

    def run_test(self) -> list[tuple[str, str]]:

        violations = []

        only_check_language = self.get_setting("only_check_language")

        allowed_characters = '.\n\r\t,:;" '

        for string in self.collection.localized_strings:
            if only_check_language and string.language_code != only_check_language:
                continue

            tokens = string.tokens_with_positions()

            if not tokens or len(tokens) == 0:
                continue

            for token, start, end in tokens:
                preceding_char = string.value[start - 1] if start > 0 else None
                if preceding_char:
                    if preceding_char not in allowed_characters:
                        violations.append(
                            (
                                f"Token '{token}' is directly preceded by '{preceding_char}' in string: {string}",
                                string.language_code,
                            )
                        )

                succeeding_char = string.value[end] if end < len(string.value) else None
                if succeeding_char:
                    if succeeding_char not in allowed_characters:
                        violations.append(
                            (
                                f"Token '{token}' is directly followed by '{succeeding_char}' in string: {string}",
                                string.language_code,
                            )
                        )

        return violations
