"""Base type for localization."""

import abc
from typing import Any, Dict, List

from localizationkit.configuration import Configuration
from localizationkit.localization_types import LocalizedCollection
from localizationkit.utility_types import TestResult


class LocalizationTestCase(abc.ABC):
    """Base object for a localization test case.

    :param configuration: The root configuration object
    :param collection: The collection to run the test on
    :param test_settings: The base test settings for the current test
    """

    configuration: Configuration
    collection: LocalizedCollection
    test_settings: Dict[str, Any]

    def __init__(self, configuration: Configuration, collection: LocalizedCollection):
        self.configuration = configuration
        self.collection = collection
        self.test_settings = configuration.get_test_preferences(self.__class__.name())

    def get_setting(self, name: str) -> Any:
        """Get a setting, falling back to the default if not specified.

        :param name: The name of the setting to fetch

        :returns: The overridden setting if specified, the default otherwise
        """
        return self.test_settings.get(name, self.__class__.default_settings()[name])

    @classmethod
    @abc.abstractmethod
    def name(cls) -> str:
        """Get the name of the test.

        :returns: The name of the test
        """
        raise NotImplementedError("Name should always be overridden")

    @classmethod
    @abc.abstractmethod
    def default_settings(cls) -> Dict[str, Any]:
        """Get the default settings for the test.

        :returns: The default settings for the test
        """
        raise NotImplementedError("default_settings should always be overridden")

    @classmethod
    def is_opt_in(cls) -> bool:
        """Check if the test is opt in or not.

        Not all tests make sense for everyone (e.g. language specific tests), so
        we make those opt in

        :returns: True if this is an opt in method, False otherwise
        """
        return False

    @abc.abstractmethod
    def run_test(self) -> List[str]:
        """Run the test

        :returns: The list of violations encountered
        """
        raise NotImplementedError("run_test should always be overridden")

    def execute(self) -> TestResult:
        """Execute the test and return the result

        :returns: A test result
        """
        try:
            violations = self.run_test()

            if violations is None:
                raise Exception(f"Failed to get exceptions from test: {self.__class__.name()}")

            if len(violations):
                return TestResult.failure(self.__class__.name(), violations)

            return TestResult.success(self.__class__.name())
        except Exception as ex:
            return TestResult.failure(self.__class__.name(), [str(ex)])
