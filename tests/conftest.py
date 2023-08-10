from collections.abc import AsyncGenerator, AsyncIterable
from io import StringIO

import pytest
from faker import Faker
from jara_utils.cli_output import CLIOutput


@pytest.fixture(scope='session')
def faker() -> Faker:
    return Faker()


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
def random_numbers(faker: Faker) -> list[int]:
    return faker.pylist(faker.pyint(10, 80), False, [int])


@pytest.fixture()
def random_number_async_iterable(random_numbers: list[int]) -> AsyncIterable:
    async def generator() -> AsyncGenerator[int, None]:
        for number in random_numbers:
            yield number

    return generator()
