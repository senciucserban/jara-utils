import pytest
from faker import Faker


@pytest.fixture(scope='session')
def faker():
    f = Faker()
    return f
