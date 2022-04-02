from typing import List, AsyncIterator

import math
import pytest

from faker import Faker

from jara_utils.normalization import grouper, aenumerate, async_grouper


def test_grouper_ok(faker: Faker):
    chunk_size, length_of_iterable = 2, faker.pyint(min_value=10, max_value=80)
    iterable = list(range(length_of_iterable))
    assert len(list(grouper(chunk_size, iterable))) == math.ceil(length_of_iterable / chunk_size)


def test_grouper_with_empty_list():
    assert len(list(grouper(5, []))) == 0


@pytest.mark.asyncio()
@pytest.mark.parametrize('start', [0, 1, 2, 10])
async def test_async_enumerate(random_number_async_iterable: AsyncIterator, random_numbers: List[int], start: int):
    i = start
    final_index = len(random_numbers) - 1 + start
    result = []
    async for i, n in aenumerate(random_number_async_iterable, start):
        result.append(n)
    assert final_index == i
    assert result == random_numbers


@pytest.mark.asyncio()
async def test_async_grouper_ok(faker: Faker, random_numbers: List[int], random_number_async_iterable: AsyncIterator):
    chunk_size, length_of_iterable = 2, len(random_numbers)
    chunks = []
    async for chunk in async_grouper(chunk_size, random_number_async_iterable):
        chunks.append(chunk)
    assert len(chunks) == math.ceil(length_of_iterable / chunk_size)
