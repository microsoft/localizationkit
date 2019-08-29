"""Toolkit for validation of localized strings."""

import abc
import difflib
import inspect
from typing import Any, Dict, List, Optional, Set, Type

from localizationkit.configuration import Configuration
from localizationkit.localization_types import LocalizedCollection, LocalizedString
from localizationkit.utility_types import TestResult
from localizationkit.tests.test_case import LocalizationTestCase

from localizationkit import tests


def _find_tests() -> List[Type[LocalizationTestCase]]:
    """Find all the tests."""

    test_module_names = [
        module_name for module_name in dir(tests) if not module_name.startswith("__")
    ]
    test_modules = [getattr(tests, name) for name in test_module_names]

    names_seen: Set[str] = set()
    test_classes: List[Type[LocalizationTestCase]] = []

    for module in test_modules:

        for reference_name in dir(module):

            reference = getattr(module, reference_name)

            if not inspect.isclass(reference):
                continue

            if not issubclass(reference, LocalizationTestCase):
                continue

            if reference == LocalizationTestCase:
                continue

            if reference.__name__ in names_seen:
                raise Exception(
                    "At least 2 classes exist with the same name: " + reference.__name__
                )

            test_classes.append(reference)

    return test_classes


def run_tests(configuration: Configuration, collection: LocalizedCollection) -> List[TestResult]:
    """Run all tests."""

    test_classes = _find_tests()
    blacklist = set(configuration.blacklist())
    opt_ins = set(configuration.opt_in())

    results = []

    for test_class in test_classes:
        if test_class.name() in blacklist:
            continue

        if test_class.is_opt_in() and test_class.name() not in opt_ins:
            continue

        test_instance = test_class(configuration, collection)
        results.append(test_instance.execute())

    return results
