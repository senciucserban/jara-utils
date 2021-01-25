from io import StringIO

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
