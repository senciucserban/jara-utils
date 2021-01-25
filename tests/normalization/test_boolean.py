import pytest

from jara_utils.normalization import str_2_bool, is_dunder, is_email


@pytest.mark.parametrize(
    ('value', 'result'),
    [
        ('yes', True),
        ('true', True),
        ('t', True),
        ('y', True),
        ('1', True),
        ('no', False),
        ('false', False),
        ('f', False),
        ('n', False),
        ('0', False),
        ('invalid', None),
        ('', None),
    ])
def test_str_2_bool(value: str, result: bool):
    assert str_2_bool(value) is result


@pytest.mark.parametrize(
    ('value', 'result'),
    [
        ('__init__', True),
        ('__something__', True),
        ('__something', False),
        ('_something_', False),
        ('_something__', False),
        ('__something_', False),
        ('____', False),
        ('__', False),
    ])
def test_is_dunder(value: str, result: bool):
    assert is_dunder(value) is result


@pytest.mark.parametrize(
    ('value', 'result'),
    [
        ('hello@world.com', True),
        ('hello@world.co.uk', True),
        ('hello.world@example.com', True),
        ('hello-world@example.com', True),
        ('hello_world@example.com', True),
        ('hello_world.example.com', False),
        ('.hello@world.com', False),
        ('email', False),
        ('my_email', False),
        ('hello@world.', False),
        ('hello@world.&', False),
        ('hello@world', False),
        ('hello@127.0.0.1', False),
        ('hello@127.0.0.1:80', False),
        ('', False),
    ])
def test_is_email(value: str, result: bool):
    assert is_email(value) is result
