import math
from collections.abc import AsyncIterator

import pytest
from faker import Faker
from jara_utils.normalization import aenumerate, async_grouper, grouper


def test_grouper_ok(faker: Faker) -> None:
    chunk_size, length_of_iterable = 2, faker.pyint(min_value=10, max_value=80)
    iterable = list(range(length_of_iterable))
    assert len(list(grouper(chunk_size, iterable))) == math.ceil(length_of_iterable / chunk_size)


def test_grouper_with_empty_list() -> None:
    assert len(list(grouper(5, []))) == 0


@pytest.mark.asyncio()
@pytest.mark.parametrize('start', [0, 1, 2, 10])
async def test_async_enumerate(
    random_number_async_iterable: AsyncIterator,
    random_numbers: list[int],
    start: int,
) -> None:
    i = start
    final_index = len(random_numbers) - 1 + start
    result = []
    async for i, n in aenumerate(random_number_async_iterable, start):  # noqa: B007
        result.append(n)
    assert final_index == i
    assert result == random_numbers


@pytest.mark.asyncio()
async def test_async_grouper_ok__leftover(
    random_numbers: list[int],
    random_number_async_iterable: AsyncIterator,
) -> None:
    chunk_size, length_of_iterable = 2, len(random_numbers)
    if length_of_iterable % 2 == 0:
        length_of_iterable -= 1
        del random_numbers[0]

    chunks = []
    async for chunk in async_grouper(chunk_size, random_number_async_iterable):
        chunks.append(chunk)  # noqa: PERF402
    assert len(chunks) == math.ceil(length_of_iterable / chunk_size)


@pytest.mark.asyncio()
async def test_async_grouper_ok__perfect_chunks(
    random_numbers: list[int],
    random_number_async_iterable: AsyncIterator,
) -> None:
    chunk_size, length_of_iterable = 2, len(random_numbers)
    if length_of_iterable % 2 == 1:
        length_of_iterable += 1
        random_numbers.append(1)

    chunks = []
    async for chunk in async_grouper(chunk_size, random_number_async_iterable):
        chunks.append(chunk)  # noqa: PERF402
    assert len(chunks) == math.ceil(length_of_iterable / chunk_size)
