from io import StringIO

import pytest
from faker import Faker

from jara_utils.cli_output import CLIOutput


@pytest.fixture(scope='session')
def faker():
    f = Faker()
    return f


@pytest.fixture
def stream_buffer():
    return StringIO()


@pytest.fixture
def error_buffer():
    return StringIO()


@pytest.fixture
def cli_output(stream_buffer, error_buffer):
    return CLIOutput(stream_buffer, error_buffer)
