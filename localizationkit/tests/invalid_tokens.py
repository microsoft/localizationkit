"""Invalid tokens."""

import re
from typing import Any

from localizationkit.tests.test_case import LocalizationTestCase


class InvalidTokens(LocalizationTestCase):
    """Check the tokens in strings are all valid."""

    @classmethod
    def name(cls) -> str:
        return "invalid_tokens"

    @classmethod
    def default_settings(cls) -> dict[str, Any]:
        return {}

    def run_test(self) -> list[tuple[str, str]]:

        violations = []

        invalid_token_pattern = re.compile(r"(%[^@%\.a-zA-Z0-9 ]+)", flags=re.DOTALL)

        for string in self.collection.localized_strings:
            matches = invalid_token_pattern.findall(string.value)

            # Any matches are a bad thing
            if matches and len(matches) > 0:
                violations.append(
                    (
                        f"Translation contains invalid tokens ({matches}): {string}",
                        string.language_code,
                    )
                )

        return violations
