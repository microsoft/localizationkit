"""Invalid tokens."""

import re
from typing import Any, Dict, List

from localizationkit.tests.test_case import LocalizationTestCase


class InvalidTokens(LocalizationTestCase):
    """Check the tokens in strings are all valid."""

    @classmethod
    def name(cls) -> str:
        return "invalid_tokens"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {}

    def run_test(self) -> List[str]:

        violations = []

        invalid_token_pattern = re.compile(r"(%[^@%\.a-z0-9]+)|([^%]%$)", flags=re.DOTALL)

        for string in self.collection.localized_strings:
            matches = invalid_token_pattern.findall(string.value)

            # Any matches are a bad thing
            if matches and len(matches) > 0:
                violations.append(f"Translation contains invalid tokens ({matches}): {string}")

        return violations
