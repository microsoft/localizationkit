"""Swift interpolation."""

import re
from typing import Any

from localizationkit.tests.test_case import LocalizationTestCase


class SwiftInterpolation(LocalizationTestCase):
    """Check for Swift string interpolation."""

    @classmethod
    def name(cls) -> str:
        return "swift_interpolation"

    @classmethod
    def default_settings(cls) -> dict[str, Any]:
        return {}

    @classmethod
    def is_opt_in(cls) -> bool:
        return True

    def run_test(self) -> list[tuple[str, str]]:

        violations = []

        pattern = re.compile(r'\\\([^\)"]*\)', flags=re.DOTALL)

        for string in self.collection.localized_strings:

            if pattern.findall(string.value):
                violations.append(
                    (
                        f"Swift string interpolation found in string: {string}",
                        string.language_code,
                    )
                )
                continue

        return violations
