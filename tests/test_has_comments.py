"""Has comments tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class HasCommentsTests(unittest.TestCase):
    """Has comments tests."""

    def setUp(self):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        self.config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
        self.configuration = localizationkit.Configuration.from_file(self.config_path)

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
