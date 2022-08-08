"""Has comments tests."""

# pylint: disable=line-too-long

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_has_comments(configuration):
    """Test that has comments works"""
    bad_comments = [None, "", "Hello", "Hello world", "This is a comment"]
    good_comments = [
        "This is a nice and long comment with lots of words",
        "Here is another comment that also has a lot of words in it",
    ]

    for comment in bad_comments:
        string = localizationkit.LocalizedString("Key", "Value", comment, "en")
        collection = localizationkit.LocalizedCollection([string])
        has_comment_test = localizationkit.tests.has_comments.HasComments(configuration, collection)
        result = has_comment_test.execute()
        assert result.succeeded() is False

    for comment in good_comments:
        string = localizationkit.LocalizedString("Key", "Value", comment, "en")
        collection = localizationkit.LocalizedCollection([string])
        has_comment_test = localizationkit.tests.has_comments.HasComments(configuration, collection)
        result = has_comment_test.execute()
        assert result.succeeded()
