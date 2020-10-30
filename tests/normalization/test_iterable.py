from jara_utils.normalization.iterable import grouper
import math


def test_grouper_ok(faker):
    chunk_size, length_of_iterable = 2, faker.pyint(min_value=10, max_value=80)
    iterable = list(range(length_of_iterable))
    assert len([chunk for chunk in grouper(chunk_size, iterable)]) == math.ceil(length_of_iterable / chunk_size)


def test_grouper_with_empty_list():
    assert len([chunk for chunk in grouper(5, list())]) == 0
