import os
from pathlib import Path

import pytest


@pytest.fixture(scope='session')
def system_env_variable_name() -> str:
    return 'JARA_UTILS_VARIABLE'


@pytest.fixture(scope='session')
def system_env_variable_value() -> str:
    return '1'


@pytest.fixture(scope='session')
def dotenv_paths() -> list[Path]:
    base_dir = Path(__file__).parent
    return [base_dir.joinpath(file) for file in ['.env.template', '.env.test', '.env']]


@pytest.fixture(scope='session')
def dotenv_invalid_paths() -> list[Path]:
    base_dir = Path(__file__).parent
    return [base_dir.joinpath(file) for file in ['.env.something_else', '.env.unknown']]


@pytest.fixture(autouse=True)
def _set_system_env(system_env_variable_name: str, system_env_variable_value: str) -> None:
    os.environ[system_env_variable_name] = system_env_variable_value
