"""Checks for comments."""

from typing import Any, Dict, List, Tuple

from localizationkit.tests.test_case import LocalizationTestCase


class CommentLinebreaks(LocalizationTestCase):
    """Check that comments do not contain linebreaks."""

    @classmethod
    def name(cls) -> str:
        return "comment_linebreaks"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {}

    @classmethod
    def is_opt_in(cls) -> bool:
        return True

    def run_test(self) -> List[Tuple[str, str]]:
        violations = []

        for string in self.collection.strings_for_language(self.configuration.default_language()):

            if string.comment is None:
                continue

            if "\n" in string.comment or "\r" in string.comment:
                violations.append((f"Comment contains linebreaks: {string}", string.language_code))

        return violations
