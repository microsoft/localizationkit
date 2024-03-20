"""Exception types."""


class LocalizationKitException(Exception):
    """Represents an exception from this library."""


class DuplicateTestException(LocalizationKitException):
    """Represents an exception where multiple tests with the same name appear."""
