import os
from pathlib import Path

from jara_utils.dotenv_configs import load_multiple_dotenvs


def test_system_env(system_env_variable_name: str, system_env_variable_value: str) -> None:
    """Make sure there is a system environment variable set."""
    assert os.environ.get(system_env_variable_name) == system_env_variable_value


def test_load_missing_files(
    dotenv_invalid_paths: list[Path],
    system_env_variable_name: str,
    system_env_variable_value: str,
) -> None:
    """Make sure the method will not throw any error when files are missing."""
    load_multiple_dotenvs(dotenv_invalid_paths)
    assert os.environ.get(system_env_variable_name) == system_env_variable_value


def test_load_with_overwrite(dotenv_paths: list[Path], system_env_variable_name: str) -> None:
    """Load the variables from dotenv files and overwrite the existing env variables."""
    load_multiple_dotenvs(dotenv_paths, overwrite_existing=True)

    assert os.environ[system_env_variable_name] == '3'
    assert 'JARA_UTILS_NONE' not in os.environ
    assert os.environ['JARA_UTILS_EMPTY_STRING'] == ''
    assert os.environ['JARA_UTILS_USERNAME'] == 'john'


def test_load_without_overwrite(
    dotenv_paths: list[Path],
    system_env_variable_name: str,
    system_env_variable_value: str,
) -> None:
    """Load the variables from dotenv files and don't overwrite the existing env variables."""
    load_multiple_dotenvs(dotenv_paths, overwrite_existing=False)

    assert os.environ[system_env_variable_name] == system_env_variable_value
    assert 'JARA_UTILS_NONE' not in os.environ
    assert os.environ['JARA_UTILS_EMPTY_STRING'] == ''
    assert os.environ['JARA_UTILS_USERNAME'] == 'john'
