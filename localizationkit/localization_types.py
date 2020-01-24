"""Types for localization."""

import re
from typing import ClassVar, List, Pattern


class LocalizedString:
    """Represents a localized string.

    :param key: The unique key for the string
    :param value: The value for the string
    :param comment: The comment for the string
    :param language_code: The language code for the language the string is in
    """

    _TOKEN_REGEX: ClassVar[
        str
    ] = r"(%(?:[0-9]+\$)?[0-9]*\.?[0-9]*(?:h|hh|l|ll|q|L|z|t|j){0,2}[dDuUxXoOfFeEgGcCsSaAp@])"
    _TOKEN_PATTERN: ClassVar[Pattern] = re.compile(_TOKEN_REGEX, flags=re.DOTALL)

    key: str
    value: str
    comment: str
    language_code: str

    def __init__(self, key: str, value: str, comment: str, language_code: str) -> None:
        self.key = key
        self.value = value
        self.comment = comment
        self.language_code = language_code

    def tokens(self) -> List[str]:
        """Find and return the tokens in the string.

        :returns: The list of tokens in the string
        """
        return LocalizedString._TOKEN_PATTERN.findall(self.value)

    def __str__(self) -> str:
        """Generate and return the string representation of the object.

        :returns: A string representation of the object
        """
        return str(
            {
                "key": self.key,
                "value": self.value,
                "comment": self.comment,
                "language": self.language_code,
            }
        )


class LocalizedCollection:
    """A collection of localized strings.

    :param localized_strings: The list of localized strings in the collection
    """

    localized_strings: List[LocalizedString]

    def __init__(self, localized_strings: List[LocalizedString]) -> None:
        self.localized_strings = localized_strings

    def strings_for_key(self, key: str) -> List[LocalizedString]:
        """Return all the strings matching the key

        i.e. This will have a list of strings with identical keys, but different
        languages.

        :returns: The list of strings with the matching key
        """
        return [string for string in self.localized_strings if string.key == key]

    def strings_for_language(self, language_code: str) -> List[LocalizedString]:
        """Return all the strings matching the language code

        :returns: The list of strings with the matching language code
        """
        return [
            string for string in self.localized_strings if string.language_code == language_code
        ]

    def languages(self) -> List[str]:
        """Return the list of languages in the collection.

        :returns: The list of langauges in the collection
        """
        languages = set()
        for string in self.localized_strings:
            languages.add(string.language_code)
        return list(languages)
