from datetime import datetime

import pytest
from faker import Faker
from jara_utils.normalization import age_from, parse_int


@pytest.mark.parametrize(
    ('value', 'result'),
    [
        (1, 1),
        ('53', 53),
        (134.61, 134),
        ('string', None),
        ([], None),
        (datetime.now(), None),
    ],
)
def test_parse_int(value: str | float | list | datetime, result: int | None) -> None:
    assert parse_int(value) == result


def test_age_from(faker: Faker) -> None:
    age = faker.pyint(min_value=18, max_value=60)
    assert age_from(None) is None
    assert age_from(datetime.min) is None
    assert age_from(faker.date_of_birth(minimum_age=age, maximum_age=age)) == age
