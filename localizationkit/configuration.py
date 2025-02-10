"""Configuration for localization tests."""

from typing import Any, cast

import toml


class Configuration:
    """Holds all the configuration data."""

    raw_config: dict[str, Any]

    def __init__(self, raw_config: dict[str, Any]) -> None:
        self.raw_config = raw_config

    def default_language(self) -> str:
        """Return the default language code.

        Defaults to en.

        :returns: The default language code
        """
        return self.raw_config.get("default_language", "en")

    def blacklist(self) -> list[str]:
        """Return the list of blacklisted tests.

        :returns: The blacklisted tests
        """
        return self.raw_config.get("blacklist", [])

    def opt_in(self) -> list[str]:
        """Return the list of opted in tests.

        :returns: The opted in tests
        """
        return self.raw_config.get("opt_in", [])

    def get_test_preferences(self, name: str) -> dict[str, Any]:
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

        with open(file_path, encoding="utf-8") as config_file:
            return Configuration(cast(dict[str, Any], toml.load(config_file)))
