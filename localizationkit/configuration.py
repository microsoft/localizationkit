"""Configuration for localization tests."""

from typing import Any, cast, Dict, List

import toml


class Configuration:
    """Holds all the configuration data."""

    raw_config: Dict[str, Any]

    def __init__(self, raw_config: Dict[str, Any]) -> None:
        self.raw_config = raw_config

    def default_language(self) -> str:
        """Return the default language code.

        Defaults to en.

        :returns: The default language code
        """
        return self.raw_config.get("default_language", "en")

    def blacklist(self) -> List[str]:
        """Return the list of blacklisted tests.

        :returns: The blacklisted tests
        """
        return self.raw_config.get("blacklist", [])

    def opt_in(self) -> List[str]:
        """Return the list of opted in tests.

        :returns: The opted in tests
        """
        return self.raw_config.get("opt_in", [])

    def get_test_preferences(self, name: str) -> Dict[str, Any]:
        """Get the preferences for a given test.

        :param name: The name of the test

        :returns: The test preferences
        """
        return self.raw_config.get(name, {})

    @staticmethod
    def from_file(file_path: str) -> "Configuration":
        """Load the configuration from file.

        :param file_path: The path to the configuration file

        :returns: The parsed configuration object
        """

        with open(file_path) as config_file:
            return Configuration(cast(Dict[str, Any], toml.load(config_file)))
