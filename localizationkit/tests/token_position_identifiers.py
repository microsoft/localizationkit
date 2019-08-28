"""Token position identifiers."""

from typing import Any, Dict, List, Set

from localizationkit.tests.test_case import LocalizationTestCase


class TokenPositionIdentifiers(LocalizationTestCase):
    """Check the tokens in strings have position identifiers."""

    @classmethod
    def name(cls) -> str:
        return "token_position_identifiers"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {"always": False}

    def run_test(self) -> List[str]:

        violations = []

        always = self.get_setting("always")

        for string in self.collection.localized_strings:
            tokens = string.tokens()

            if not tokens or len(tokens) == 0:
                continue

            # If it has fewer than 2 tokens and we aren't set to always, we can
            # just skip
            if len(tokens) < 2 and not always:
                continue

            # Track the positions we've seen
            positional_tokens: Set[int] = set()

            for token in tokens:
                if "$" not in token:
                    violations.append(f"String missing positional tokens: {string}")
                    continue

                position = int((token.split("$")[0]).replace("%", ""))

                if position in positional_tokens:
                    violations.append(f"Duplicate token position: {string}")
                    continue

                positional_tokens.add(position)

            for i in range(1, len(tokens) + 1):
                if i not in positional_tokens:
                    violations.append(f"Token position index skipped: {string}")

        return violations
