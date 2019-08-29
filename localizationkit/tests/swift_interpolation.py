"""Swift interpolation."""

import re
from typing import Any, Dict, List

from localizationkit.tests.test_case import LocalizationTestCase


class SwiftInterpolation(LocalizationTestCase):
    """Check for Swift string interpolation."""

    @classmethod
    def name(cls) -> str:
        return "swift_interpolation"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {}

    @classmethod
    def is_opt_in(cls) -> bool:
        return True

    def run_test(self) -> List[str]:

        violations = []

        pattern = re.compile(r'\\\([^\)"]*\)', flags=re.DOTALL)

        for string in self.collection.localized_strings:

            if pattern.findall(string.value):
                violations.append(f"Swift string interpolation found in string: {string}")
                continue

        return violations
