import pytest

from jara_utils.constants import TextColor


@pytest.mark.parametrize(
    'level,color', [
        ('debug', TextColor.CYAN),
        ('info', TextColor.OKBLUE),
        ('success', TextColor.OKGREEN),
        ('warning', TextColor.YELLOW),
        ('error', TextColor.RED),
        ('fail', TextColor.RED),
    ])
def test_cli_output(faker, cli_output, stream_buffer, error_buffer, level, color):
    word = faker.word()
    message = f'{faker.word()} {word} {faker.word()} {faker.word()} {faker.word()}'

    getattr(cli_output, level)(message)
    assert stream_buffer.getvalue() == f'{color}{message}{TextColor.ENDC}\n'

    stream_buffer.flush()
    getattr(cli_output, level)(message, highlights=[word])
    assert f'{TextColor.BOLD}{word}{TextColor.ENDC}{color}' in stream_buffer.getvalue()
