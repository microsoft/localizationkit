"""Has comments tests."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_comment_linebreaks(configuration):
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
            configuration, collection
        )
        result = comment_linebreak_test.execute()
        assert result.succeeded() is False

    for comment in good_comments:
        string = localizationkit.LocalizedString("Key", "Value", comment, "en")
        collection = localizationkit.LocalizedCollection([string])
        comment_linebreak_test = localizationkit.tests.comment_linebreaks.CommentLinebreaks(
            configuration, collection
        )
        result = comment_linebreak_test.execute()
        assert result.succeeded()
