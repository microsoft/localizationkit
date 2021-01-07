"""Placeholder token explanation."""

from typing import Any, Dict, List, Set

from localizationkit.tests.test_case import LocalizationTestCase


class PlaceholderTokenExplanation(LocalizationTestCase):
    """Check the placeholder tokens in strings have explanation in comments."""

    @classmethod
    def name(cls) -> str:
        return "placeholder_token_explanation"

    @classmethod
    def default_settings(cls) -> Dict[str, Any]:
        return {"always": False}

    def run_test(self) -> List[str]:

        violations = []

        for string in self.collection.localized_strings:
            tokens = string.tokens()
            comment_tokens = string.comment_tokens()

            if not tokens or len(tokens) == 0:
                if comment_tokens or len(comment_tokens) > 0:
                    violations.append(f"Comment string has extra token explanations: {string}")
                    continue
                continue

            if not comment_tokens or len(comment_tokens) == 0:
                violations.append(f"Comment string is missing all token explanation: {string}")
                continue

            if len(comment_tokens) < len(tokens):
                violations.append(f"Comment string is missing explanantion for some tokens: {string}")
                continue

            if len(comment_tokens) > len(tokens):
                violations.append(f"""Comment string has explanation for extra tokens
                that are not a part of the string : {string}""")
                continue

            # Validate token format in both string and comment string if it has single token
            if len(tokens) < 2:
                if "%@" not in tokens[0]:
                    violations.append(f"String missing correctly formatted token: {string}")
                    continue
                if  "%@" not in comment_tokens[0]:
                    violations.append(f"String comment missing correctly formatted token: {string}")
                    continue
                continue

            # Validate position of both tokens and comment tokens to make sure all placeholder tokens
            # in string have corresponding explanation in the comment string
            positional_tokens: Set[int] = set()
            comment_positional_tokens: Set[int] = set()

            for token in tokens:
                if "$" not in token:
                    violations.append(f"String missing positional tokens: {string}")
                    continue

                position = int((token.split("$")[0]).replace("%", ""))

                if position in positional_tokens:
                    violations.append(f"Duplicate token position: {string}")
                    continue

                positional_tokens.add(position)

            for token in comment_tokens:
                if "$" not in token:
                    violations.append(f"Comment string missing positional tokens: {string}")
                    continue

                position = int((token.split("$")[0]).replace("%", ""))

                if position in comment_positional_tokens:
                    violations.append(f"Duplicate comment token position: {string}")
                    continue

                comment_positional_tokens.add(position)

            for i in range(1, len(tokens) + 1):
                if i not in positional_tokens:
                    violations.append(f"Token position index skipped: {string}")

            for i in range(1, len(comment_tokens) + 1):
                if i not in comment_positional_tokens:
                    violations.append(f"Comment Token position index skipped: {string}")

        return violations
