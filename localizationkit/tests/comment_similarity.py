"""Comment similarity."""

import difflib
from typing import Any, Dict, List

from localizationkit.tests.test_case import LocalizationTestCase


class CheckCommentSimilarity(LocalizationTestCase):
    """Check the similarity between comments and values."""

    @classmethod
    def name(cls) -> str:
        return "comment_similarity"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {"maximum_similarity_ratio": 0.5}

    def run_test(self) -> List[str]:

        maximum_similarity_ratio = self.get_setting("maximum_similarity_ratio")

        violations = []

        for string in self.collection.strings_for_language(self.configuration.default_language()):
            if string.value is None or string.comment is None:
                continue

            similarity = difflib.SequenceMatcher(None, string.value, string.comment).ratio()

            if similarity > maximum_similarity_ratio:
                violations.append(
                    f"Value and comment exceeded similarity ratio of {maximum_similarity_ratio}: {string}"
                )
                continue

        return violations
