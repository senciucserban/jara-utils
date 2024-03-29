====
Jara
====

    Jara means bear in `Sesotho`_ :bear:

|python| |flake8| |poetry|

I'm tired of writing same stuff in every project. In addition to this, to make unittests every time for them.

Installation
------------
The package is available on pypi so you can install the project with ``pip install jara-utils``.

How to contribute to the package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clone project locally and then:
    * Install all dependencies including the test and the dev oanes: ``poetry install -E test -D``;
    * Do changes in the project;
    * Create unittests (please make sure  you will keep coverage to 100%);
    * Run all sanity commands (pytest, flake8, mypy, bandit);
    * Check if there is any duplicated or dead fixtures by running ``pytest`` with ``--dead-fixtures`` and ``--dup-fixtures``;

Note: Run commands using poetry: ``poetry run <command>``;

What you can find in this repo?
-------------------------------
Exceptions
~~~~~~~~~~
All exceptions:
    * ``EnvironmentVariableNotFoundError`` when you expect to found an environment variable.

Environment
~~~~~~~~~~~
A simple wrapper over ``os.environ.get(...)`` to easy handling environment variables, we have support for types like: string, int, bool, list

**Watch out** ``get_list`` support only List of str to convert to a list of int for example you should use ``parse_int`` with a list comprehension.

Benchmark
~~~~~~~~~
A decorator named ``timeit`` which can be used on sync and async methods to see execution time.

    If execution time is below to ``0.50 seconds`` there will be no log.
    **Maybe** add threshold as environment variable?

Utils | Grouped by returned types.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* boolean: ``str_2_bool``, ``is_dunder``, ``is_email``;
* datetime: ``date_2_datetime``, ``str_2_datetime``;
* integer: ``'parse_int``, ``age_from``;
* iterable: ``grouper``, ``async_grouper``, ``aenumerate``;
* string: ``snake_to_camel``, ``camel_to_snake``;


CLI Output
~~~~~~~~~~
Class used for output, which can be, console (by default), file or any buffer. Can be used for fancy outputs, like color text, highlight (bold) words.
Color available and which method will produce the color:

* Cyan (debug)
* Light blue (info)
* Light green (success)
* Yellow (warning)
* Red (error/fail)


.. _Sesotho: https://en.wikipedia.org/wiki/Sotho_language

.. |python| image:: https://img.shields.io/badge/python-3.11.x-blue.svg
    :alt: Python 3.7.x
    :target: https://www.python.org/downloads/release/python-3111/
.. |flake8| image:: https://img.shields.io/badge/code_style-flake8-brightgreen.svg
    :alt: Flake8
    :target: http://flake8.pycqa.org/en/latest/
.. |poetry| image:: https://img.shields.io/badge/dependency_manager-poetry-blueviolet.svg
    :alt: Poetry
    :target: https://poetry.eustace.io
