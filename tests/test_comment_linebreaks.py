"""Has comments tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class CommentLinebreaksTests(unittest.TestCase):
    """Comment linebreaks tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

    def test_comment_linebreaks(self):
        """Test that has comments works"""
        bad_comments = [
            "\n",
            "\r",
            "\r\n",
            "\n\r",
            "Hello\nWorld",
            "\nHello World",
            "Hello World\n",
        ]
        good_comments = [
            None,
            "",
            "Hello World",
            "This is a nice and long comment with lots of words that would "
            + "normally induce a linebreak for automatic wrapping, but "
            + "shouldn't here. This is a nice and long comment with lots of "
            + "words that would normally induce a linebreak for automatic "
            + "wrapping, but shouldn't here.",
        ]

        for comment in bad_comments:
            string = localizationkit.LocalizedString("Key", "Value", comment, "en")
            collection = localizationkit.LocalizedCollection([string])
            comment_linebreak_test = localizationkit.tests.comment_linebreaks.CommentLinebreaks(
                self.configuration, collection
            )
            result = comment_linebreak_test.execute()
            self.assertFalse(result.succeeded())

        for comment in good_comments:
            string = localizationkit.LocalizedString("Key", "Value", comment, "en")
            collection = localizationkit.LocalizedCollection([string])
            comment_linebreak_test = localizationkit.tests.comment_linebreaks.CommentLinebreaks(
                self.configuration, collection
            )
            result = comment_linebreak_test.execute()
            self.assertTrue(result.succeeded())
