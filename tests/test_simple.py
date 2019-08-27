"""Simple tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class BaseTests(unittest.TestCase):
    """Base tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_run_tests(self):
        """Test run_tests."""
        strings = localizationkit.LocalizedString("Key", "Value", "Comment", "en")
        collection = localizationkit.LocalizedCollection([strings])
        results = localizationkit.run_tests(self.configuration, collection)
        self.assertGreater(len(results), 0)

    def test_comment_similarity(self):
        """Test that comment similarity works"""
        strings = localizationkit.LocalizedString("Key", "Value", "Comment", "en")
        collection = localizationkit.LocalizedCollection([strings])
        similarity_test = localizationkit.tests.comment_similarity.CheckCommentSimilarity(
            self.configuration, collection
        )
        similarity_test.execute()

    def test_has_comments(self):
        """Test that has comments works"""
        bad_comments = [None, "", "Hello", "Hello world", "This is a comment"]
        good_comments = [
            "This is a nice and long comment with lots of words",
            "Here is another comment that also has a lot of words in it",
        ]

        for comment in bad_comments:
            string = localizationkit.LocalizedString("Key", "Value", comment, "en")
            collection = localizationkit.LocalizedCollection([string])
            has_comment_test = localizationkit.tests.has_comments.HasComments(
                self.configuration, collection
            )
            result = has_comment_test.execute()
            self.assertFalse(result.succeeded())

        for comment in good_comments:
            string = localizationkit.LocalizedString("Key", "Value", comment, "en")
            collection = localizationkit.LocalizedCollection([string])
            has_comment_test = localizationkit.tests.has_comments.HasComments(
                self.configuration, collection
            )
            result = has_comment_test.execute()
            self.assertTrue(result.succeeded())

    def test_token_matching(self):
        """Test that token matching works"""
        test_cases = [
            (
                True,
                [
                    localizationkit.LocalizedString(
                        "Key", "This is a string with no tokens", "Some comment", "en"
                    ),
                    localizationkit.LocalizedString(
                        "Key", "This is a string with no tokens", "Some comment", "fr"
                    ),
                ],
            ),
            (
                True,
                [
                    localizationkit.LocalizedString(
                        "Key", "This is a string with a token: %@", "Some comment", "en"
                    ),
                    localizationkit.LocalizedString(
                        "Key", "This is a string with a token: %@", "Some comment", "fr"
                    ),
                ],
            ),
            (
                True,
                [
                    localizationkit.LocalizedString(
                        "Key",
                        "This is a string with multiple tokens: %1$d, %2$s, %3$@",
                        "Some comment",
                        "en",
                    ),
                    localizationkit.LocalizedString(
                        "Key",
                        "This is a string with multiple tokens: %1$d, %2$s, %3$@",
                        "Some comment",
                        "fr",
                    ),
                ],
            ),
            (
                False,
                [
                    localizationkit.LocalizedString(
                        "Key",
                        "This is a string with multiple tokens: %1$d, %2$s, %3$@, %4$@",
                        "Some comment",
                        "en",
                    ),
                    localizationkit.LocalizedString(
                        "Key",
                        "This is a string with multiple tokens: %1$d, %2$s, %3$@",
                        "Some comment",
                        "fr",
                    ),
                ],
            ),
        ]

        for (expected_result, strings) in test_cases:
            collection = localizationkit.LocalizedCollection(strings)
            test = localizationkit.tests.token_matching.TokenMatching(
                self.configuration, collection
            )
            result = test.execute()
            if expected_result:
                self.assertTrue(result.succeeded())
            else:
                self.assertFalse(result.succeeded())

    def test_token_position_identifiers(self):
        """Test that token position identifiers works"""
        test_cases = [
            (
                True,
                localizationkit.LocalizedString(
                    "Key", "This is a string with no tokens", "Some comment", "en"
                ),
            ),
            (
                True,
                localizationkit.LocalizedString(
                    "Key", "This is a string with one token: %@", "Some comment", "en"
                ),
            ),
            (
                True,
                localizationkit.LocalizedString(
                    "Key", "This is a string with two tokens: %1$@ %2$@", "Some comment", "en"
                ),
            ),
            (
                False,
                localizationkit.LocalizedString(
                    "Key",
                    "This is a string with two non-positional tokens: %@ %@",
                    "Some comment",
                    "en",
                ),
            ),
            (
                False,
                localizationkit.LocalizedString(
                    "Key", "This is a string with a skipped index: %1$@ %3$@", "Some comment", "en"
                ),
            ),
        ]

        for (expected_result, string) in test_cases:
            collection = localizationkit.LocalizedCollection([string])
            test = localizationkit.tests.token_position_identifiers.TokenPositionIdentifiers(
                self.configuration, collection
            )
            result = test.execute()
            if expected_result:
                self.assertTrue(result.succeeded())
            else:
                self.assertFalse(result.succeeded())
