import pytest
from _pytest.monkeypatch import MonkeyPatch
from faker import Faker

from jara_utils.environment import get_str
from jara_utils.exceptions import EnvironmentVariableNotFound


def test_required_ok(monkeypatch: MonkeyPatch, faker: Faker):
    variable_name = faker.word().upper()
    variable_value = faker.word()
    invalid = faker.word()
    monkeypatch.setenv(variable_name, variable_value)
    assert get_str(variable_name) == variable_value
    assert get_str(variable_name, invalid=invalid) == variable_value
    monkeypatch.delenv(variable_name)


def test_raise_environment_variable_not_found(faker: Faker):
    variable_name = faker.word().upper()
    with pytest.raises(EnvironmentVariableNotFound) as e:
        get_str(variable_name, required=True)
    assert variable_name in str(e.value)


def test_without_value(monkeypatch: MonkeyPatch, faker: Faker):
    variable_name = faker.word().upper()
    invalid = faker.word()
    monkeypatch.setenv(variable_name, '')
    assert get_str(variable_name) is None
    assert get_str(variable_name, invalid=invalid) == invalid


def test_not_required_ok(faker: Faker):
    variable_name = faker.word().upper()
    invalid = faker.word()
    assert get_str(variable_name) is None
    assert get_str(variable_name, invalid=invalid) == invalid
