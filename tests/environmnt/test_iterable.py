import pytest
from _pytest.monkeypatch import MonkeyPatch
from faker import Faker

from jara_utils.environment import get_list
from jara_utils.exceptions import EnvironmentVariableNotFound


def test_required_ok(monkeypatch: MonkeyPatch, faker: Faker):
    variable_name = faker.word().upper()
    word_list = [faker.word() for _ in range(faker.pyint(2, 5))]
    invalid = [faker.word() for _ in range(faker.pyint(2, 5))]
    variable_value = ','.join(word_list)
    monkeypatch.setenv(variable_name, variable_value)
    assert get_list(variable_name) == word_list
    assert get_list(variable_name, invalid=invalid) == word_list
    monkeypatch.delenv(variable_name)


def test_raise_environment_variable_not_found(faker: Faker):
    variable_name = faker.word().upper()
    with pytest.raises(EnvironmentVariableNotFound) as e:
        get_list(variable_name, required=True)
    assert variable_name in str(e.value)


def test_without_value(monkeypatch: MonkeyPatch, faker: Faker):
    variable_name = faker.word().upper()
    invalid = [faker.word() for _ in range(faker.pyint(2, 5))]
    monkeypatch.setenv(variable_name, '')
    assert get_list(variable_name) == []
    assert get_list(variable_name, invalid=invalid) == invalid


def test_not_required_ok(faker: Faker):
    variable_name = faker.word().upper()
    invalid = [faker.word() for _ in range(faker.pyint(2, 5))]
    assert get_list(variable_name) == []
    assert get_list(variable_name, invalid=invalid) == invalid
