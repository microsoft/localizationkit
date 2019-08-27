"""Checks for comments."""

from typing import Any, Dict, List

from localizationkit.tests.test_case import LocalizationTestCase


class HasComments(LocalizationTestCase):
    """Check that strings have comments."""

    @classmethod
    def name(cls) -> str:
        return "has_comments"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {"minimum_comment_length": 1, "minimum_comment_words": 1}

    def run_test(self) -> List[str]:

        minimum_comment_length = self.get_setting("minimum_comment_length")
        minimum_comment_words = self.get_setting("minimum_comment_words")

        violations = []

        for string in self.collection.strings_for_language(self.configuration.default_language()):

            if string.comment is None:
                violations.append(f"Comment was empty: {string}")
                continue

            if len(string.comment) == 0:
                violations.append(f"Comment was empty: {string}")
                continue

            if len(string.comment) < minimum_comment_length:
                violations.append(
                    f"Comment did not meet minimum length of {minimum_comment_length}: {string}"
                )
                continue

            if len(string.comment.split(" ")) < minimum_comment_words:
                violations.append(
                    f"Comment did not meet minimum word count of {minimum_comment_words}: {string}"
                )
                continue

        return violations
