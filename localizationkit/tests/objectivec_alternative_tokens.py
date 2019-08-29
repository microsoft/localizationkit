"""Objective-C alternative tokens."""

import re
from typing import Any, Dict, List

from localizationkit.tests.test_case import LocalizationTestCase


class ObjectivecAlternativeTokens(LocalizationTestCase):
    """Check for Objective-C alternative tokens.

    Objective-C seems to be perfectly happy with positional tokens of the form
    %1@ rather than %1$@. While not illegal, it is preferred that they are
    consistent so that tools don't experience unexpected failures, etc.
    """

    @classmethod
    def name(cls) -> str:
        return "objectivec_alternative_tokens"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {}

    @classmethod
    def is_opt_in(cls) -> bool:
        return True

    def run_test(self) -> List[str]:

        violations = []

        pattern = re.compile(r"(%(?:[0-9]+)(?:\.[0-9]+)?[@a-z][a-z]?)", flags=re.DOTALL)

        for string in self.collection.localized_strings:

            if pattern.findall(string.value):
                violations.append(f"Objective-C alternative tokens were found in string: {string}")
                continue

        return violations
