"""Pytest configuration."""

import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import localizationkit


@pytest.fixture
def configuration() -> localizationkit.Configuration:
    """Base configuration for running tests."""
    current_file_path = os.path.abspath(__file__)
    current_folder_path = os.path.dirname(current_file_path)
    config_path = os.path.abspath(os.path.join(current_folder_path, "config.toml"))
    return localizationkit.Configuration.from_file(config_path)
