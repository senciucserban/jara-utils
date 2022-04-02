from io import StringIO
from typing import AsyncIterable, List

import pytest
from faker import Faker

from jara_utils.cli_output import CLIOutput


@pytest.fixture(scope='session')
def faker() -> Faker:
    f = Faker()
    return f


@pytest.fixture()
def stream_buffer() -> StringIO:
    return StringIO()


@pytest.fixture()
def error_buffer() -> StringIO:
    return StringIO()


@pytest.fixture()
def cli_output(stream_buffer: StringIO, error_buffer: StringIO) -> CLIOutput:
    return CLIOutput(stream_buffer, error_buffer)


@pytest.fixture()
def random_numbers(faker: Faker) -> List[int]:
    return faker.pylist(faker.pyint(10, 80), False, [int])


@pytest.fixture()
def random_number_async_iterable(faker: Faker, random_numbers: List[int]) -> AsyncIterable:
    async def generator():
        for number in random_numbers:
            yield number
    return generator()
