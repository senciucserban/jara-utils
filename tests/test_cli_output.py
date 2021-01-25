from io import StringIO

import pytest
from faker import Faker

from jara_utils.cli_output import CLIOutput
from jara_utils.constants import TextColor


@pytest.mark.parametrize(
    ('level', 'color'), [
        ('debug', TextColor.CYAN),
        ('info', TextColor.OKBLUE),
        ('success', TextColor.OKGREEN),
        ('warning', TextColor.YELLOW),
        ('error', TextColor.RED),
        ('fail', TextColor.RED),
    ])
def test_cli_output(faker: Faker, cli_output: CLIOutput, stream_buffer: StringIO, error_buffer: StringIO,
                    level: str, color: TextColor):
    word = faker.word()
    message = f'{faker.word()} {word} {faker.word()} {faker.word()} {faker.word()}'

    getattr(cli_output, level)(message)
    assert stream_buffer.getvalue() == f'{color}{message}{TextColor.ENDC}\n'

    stream_buffer.flush()
    getattr(cli_output, level)(message, highlights=[word])
    assert f'{TextColor.BOLD}{word}{TextColor.ENDC}{color}' in stream_buffer.getvalue()
