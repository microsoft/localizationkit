"""Utility types for tests."""

from typing import List, Optional


class TestResult:
    """A simple result type

    :param name: The name of the test
    :param violations: The violations (if any)
    """

    _success: bool
    name: str
    violations: Optional[List[str]]

    def __init__(self, success: bool, name: str, violations: Optional[List[str]]):
        self._success = success
        self.name = name
        self.violations = violations

    def succeeded(self) -> bool:
        """Check if the result succeeded or not.

        :returns: True if it succeeded, False otherwise
        """
        return self._success

    @staticmethod
    def success(name: str) -> "TestResult":
        """Create a new success result.

        :param name: The name of the test

        :returns: A success result
        """
        return TestResult(True, name, None)

    @staticmethod
    def failure(name: str, violations: Optional[List[str]]) -> "TestResult":
        """Create a new failure result.

        :param name: The name of the test
        :param violations: The violations in the tests

        :returns: A failure result
        """
        return TestResult(False, name, violations)
