"""Base call tests."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


class BaseCallTests(unittest.TestCase):
    """Base call tests."""

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
