import pytest
from faker import Faker
from jara_utils.decorators import timeit


def test_timeit_on_sync_method_ok(faker: Faker) -> None:
    @timeit
    def method(my_arg: int, my_kwarg: int | None = None) -> str:
        return f'{my_arg} - {my_kwarg}'

    arg, kwarg = faker.pyint(), faker.pyint()
    assert method(arg, my_kwarg=kwarg) == f'{arg} - {kwarg}'
    assert method(arg) == f'{arg} - None'


def test_timeit_on_sync_method_from_a_class_ok(faker: Faker) -> None:
    class MyClass:
        @timeit
        def method(self, my_arg: int, my_kwarg: int | None = None) -> str:
            return f'{my_arg} - {my_kwarg}'

    arg, kwarg = faker.pyint(), faker.pyint()
    my_class = MyClass()
    assert my_class.method(arg, my_kwarg=kwarg) == f'{arg} - {kwarg}'
    assert my_class.method(arg) == f'{arg} - None'


def test_timeit_on_sync_method_with_custom_name(faker: Faker) -> None:
    @timeit(name='My sync method')
    def method(my_arg: int, my_kwarg: int | None = None) -> str:
        return f'{my_arg} - {my_kwarg}'

    arg, kwarg = faker.pyint(), faker.pyint()
    assert method(arg, kwarg) == f'{arg} - {kwarg}'
    assert method(arg) == f'{arg} - None'


def test_timeit_on_sync_method_raise_an_exception(faker: Faker) -> None:
    @timeit
    def method(my_arg: int, my_kwarg: int | None = None) -> None:  # noqa: ARG001
        msg = 'some error'
        raise ValueError(msg)

    with pytest.raises(ValueError, match='some error'):
        method(faker.pyint(), faker.pyint())


@pytest.mark.asyncio()
async def test_timeit_on_async_method_ok(faker: Faker) -> None:
    @timeit
    async def method(my_arg: int, my_kwarg: int | None = None) -> str:
        return f'{my_arg} - {my_kwarg}'

    arg, kwarg = faker.pyint(), faker.pyint()
    assert await method(arg, kwarg) == f'{arg} - {kwarg}'
    assert await method(arg) == f'{arg} - None'


@pytest.mark.asyncio()
async def test_timeit_on_async_method_from_a_class_ok(faker: Faker) -> None:
    class MyClass:
        @timeit
        async def method(self, my_arg: int, my_kwarg: int | None = None) -> str:
            return f'{my_arg} - {my_kwarg}'

    arg, kwarg = faker.pyint(), faker.pyint()
    my_class = MyClass()
    assert await my_class.method(arg, kwarg) == f'{arg} - {kwarg}'
    assert await my_class.method(arg) == f'{arg} - None'


@pytest.mark.asyncio()
async def test_timeit_on_async_method_with_custom_name(faker: Faker) -> None:
    """Decorate an async method using a custom name"""

    @timeit(name='My async method')
    async def method(my_arg: int, my_kwarg: int | None = None) -> str:
        return f'{my_arg} - {my_kwarg}'

    arg, kwarg = faker.pyint(), faker.pyint()
    assert await method(arg, kwarg) == f'{arg} - {kwarg}'
    assert await method(arg) == f'{arg} - None'


@pytest.mark.asyncio()
async def test_timeit_on_async_method_raise_an_exception(faker: Faker) -> None:
    """Raises an error"""

    @timeit
    async def method(my_arg: int, my_kwarg: int | None = None) -> None:  # noqa: ARG001
        msg = 'some error'
        raise ValueError(msg)

    with pytest.raises(ValueError, match='some error'):
        await method(faker.pyint(), faker.pyint())
