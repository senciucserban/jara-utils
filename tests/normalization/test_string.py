import pytest

from jara_utils.normalization import snake_to_camel, camel_to_snake


@pytest.mark.parametrize(
    ('value', 'result'),
    [
        ('', ''),
        ('snake_case', 'SnakeCase'),
        ('CamelCase', 'CamelCase'),
        ('camelCase', 'CamelCase'),
        ('_snake_case', 'SnakeCase'),
        ('snake__case', 'Snake_Case'),  # Da fuq?
        ('snake_case__', 'SnakeCase__'),  # Da fuq?
        ('this_is_a_snake_case_string', 'ThisIsASnakeCaseString'),
    ])
def test_snake_to_camel_with_upper_true(value: str, result: str):
    assert snake_to_camel(value) == result


@pytest.mark.parametrize(
    ('value', 'result'),
    [
        ('', ''),
        ('snake_case', 'snakeCase'),
        ('camelCase', 'camelCase'),
        ('CamelCase', 'CamelCase'),
        ('_snake_case', 'SnakeCase'),
        ('snake__case', 'snake_Case'),  # Da fuq?
        ('this_is_a_snake_case_string', 'thisIsASnakeCaseString'),
    ])
def test_snake_to_camel_with_upper_false(value: str, result: str):
    assert snake_to_camel(value, upper=False) == result


@pytest.mark.parametrize(
    ('value', 'result'),
    [
        ('', ''),
        ('CamelCase', 'camel_case'),
        ('camelCase', 'camel_case'),
        ('snake_case', 'snake_case'),
        ('camel', 'camel'),
        ('Camel', 'camel'),
        ('CAMEL', 'came_l'),  # Da fuq?
    ])
def test_camel_to_snake(value: str, result: str):
    assert camel_to_snake(value) == result
