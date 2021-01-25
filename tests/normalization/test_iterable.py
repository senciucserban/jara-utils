import math

from faker import Faker

from jara_utils.normalization import grouper


def test_grouper_ok(faker: Faker):
    chunk_size, length_of_iterable = 2, faker.pyint(min_value=10, max_value=80)
    iterable = list(range(length_of_iterable))
    assert len(list(grouper(chunk_size, iterable))) == math.ceil(length_of_iterable / chunk_size)


def test_grouper_with_empty_list():
    assert len(list(grouper(5, []))) == 0
