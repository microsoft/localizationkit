"""Checks for comments."""

from typing import Any

from localizationkit.tests.test_case import LocalizationTestCase


class HasComments(LocalizationTestCase):
    """Check that strings have comments."""

    @classmethod
    def name(cls) -> str:
        return "has_comments"

    @classmethod
    def default_settings(cls) -> dict[str, Any]:
        return {"minimum_comment_length": 30, "minimum_comment_words": 10}

    def run_test(self) -> list[tuple[str, str]]:

        minimum_comment_length = self.get_setting("minimum_comment_length")
        minimum_comment_words = self.get_setting("minimum_comment_words")

        violations = []

        for string in self.collection.strings_for_language(self.configuration.default_language()):

            if string.comment is None:
                violations.append((f"Comment was empty: {string}", string.language_code))
                continue

            if minimum_comment_length >= 0 and len(string.comment) < minimum_comment_length:
                violations.append(
                    (
                        f"Comment did not meet minimum length of {minimum_comment_length}: {string}",
                        string.language_code,
                    )
                )
                continue

            if (
                minimum_comment_words >= 0
                and len(string.comment.split(" ")) < minimum_comment_words
            ):
                violations.append(
                    (
                        f"Comment did not meet minimum word count of {minimum_comment_words}: {string}",
                        string.language_code,
                    )
                )
                continue

        return violations
