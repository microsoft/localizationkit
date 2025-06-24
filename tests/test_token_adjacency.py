"""Token adjacency tests."""

import os
import sys

import localizationkit.tests.token_adjacency

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


def test_token_adjacency(configuration):
    """Test that has comments works"""
    bad_strings = [
        "Open %@s in the app",
        "Browse all your %@s",
        "Invite more %@s to the event",
        "%@es have been added",
        "You have several %@-based options",
        "Send to %@'s inbox",
        "%@ (and %@s) are supported",
        "Start %@ing now to continue",
        "Create a new %@List",
        "Pick your best %@(s)",
        "non-%@ users are blocked",
        "@%@ has logged in",
    ]
    good_strings = [
        "Open %@ in the app",
        "You selected %@",
        "You selected %@.",
        "The %@ was updated successfully",
        "Searching for %@...",
    ]

    for bad_string in bad_strings:
        string = localizationkit.LocalizedString("Key", bad_string, "", "en")
        collection = localizationkit.LocalizedCollection([string])
        token_adjacency_test = localizationkit.tests.token_adjacency.TokenAdjacency(
            configuration, collection
        )
        result = token_adjacency_test.execute()
        assert result.succeeded() is False, f"This should have failed: {bad_string}"

    for good_string in good_strings:
        string = localizationkit.LocalizedString("Key", good_string, "", "en")
        collection = localizationkit.LocalizedCollection([string])
        token_adjacency_test = localizationkit.tests.token_adjacency.TokenAdjacency(
            configuration, collection
        )
        result = token_adjacency_test.execute()
        assert result.succeeded(), f"Failed for string: {good_strings}"
