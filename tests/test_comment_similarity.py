"""Comment similarity tests."""

import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_comment_similarity(configuration):
    """Test that comment similarity works"""
    strings = localizationkit.LocalizedString("Key", "Value", "Comment", "en")
    collection = localizationkit.LocalizedCollection([strings])
    similarity_test = localizationkit.tests.comment_similarity.CheckCommentSimilarity(
        configuration, collection
    )
    result = similarity_test.execute()
    assert result.succeeded()
