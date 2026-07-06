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

        # "%%" is the printf escape for a literal percent sign and is always
        # valid, so consume it first in the alternation. The capturing group
        # only matches a "%" that starts something which is *not* a valid
        # conversion (i.e. is followed by a character other than a conversion
        # flag/specifier, "@", "%", ".", alphanumeric, or space). Matching "%%"
        # via the first branch leaves an empty capture group, which is filtered
        # out below, so "50%%)" no longer trips on the trailing "%)".
        invalid_token_pattern = re.compile(r"%%|(%[^@%\.a-zA-Z0-9 ]+)", flags=re.DOTALL)

        for string in self.collection.localized_strings:
            matches = [match for match in invalid_token_pattern.findall(string.value) if match]

            # Any matches are a bad thing
            if matches and len(matches) > 0:
                violations.append(
                    (
                        f"Translation contains invalid tokens ({matches}): {string}",
                        string.language_code,
                    )
                )

        return violations
