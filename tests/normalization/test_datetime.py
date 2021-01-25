from datetime import datetime

import pytz
from faker import Faker

from jara_utils.normalization import date_2_datetime, str_2_datetime


def test_date_2_datetime_ok(faker: Faker):
    assert isinstance(date_2_datetime(faker.date_object()), datetime)
    assert date_2_datetime(faker.date_object()).tzinfo == pytz.UTC
    assert isinstance(date_2_datetime(faker.date_object(), naive=True), datetime)
    assert date_2_datetime(faker.date_object(), naive=True).tzinfo is None


def test_str_2_datetime_ok(faker: Faker):
    my_string_date = faker.date('%Y-%m-%d')
    my_date = str_2_datetime(my_string_date)
    assert isinstance(my_date, datetime)
    assert my_date != datetime.min
    assert my_date.tzinfo == pytz.UTC


def test_str_2_datetime_naive_ok(faker: Faker):
    my_string_date = faker.date('%Y-%m-%d')
    my_date = str_2_datetime(my_string_date, naive=True)
    assert isinstance(my_date, datetime)
    assert my_date != datetime.min
    assert my_date.tzinfo is None


def test_str_2_datetime_invalid(faker: Faker):
    my_string_date = faker.word()
    assert str_2_datetime(my_string_date) == datetime.min.replace(tzinfo=pytz.UTC)
    assert str_2_datetime(my_string_date).tzinfo == pytz.UTC
    assert str_2_datetime(my_string_date, naive=True).tzinfo is None
    assert str_2_datetime(my_string_date, invalid=None) is None


def test_str_2_datetime_wrong_type(faker: Faker):
    my_string_date = faker.pyint()
    assert str_2_datetime(my_string_date) == datetime.min.replace(tzinfo=pytz.UTC)
    assert str_2_datetime(my_string_date).tzinfo == pytz.UTC
    assert str_2_datetime(my_string_date, naive=True).tzinfo is None
    assert str_2_datetime(my_string_date, invalid=None) is None
