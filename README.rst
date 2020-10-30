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
    * Install all dependencies including the test ones: ``poetry install -E test``;
    * Do changes in the project;
    * Create unittests (please make sure  you will keep coverage to 100%);
    * Run all sanity commands (pytest, flake8, mypy)

Note: Run commands using poetry: ``poetry run pytest``;

What you can find in this repo?
-------------------------------
Exceptions
~~~~~~~~~~
All exceptions:
    * ``EnvironmentVariableNotFound`` when you expect to found an environment variable.

Environment
~~~~~~~~~~~
A simple wrapper over ``os.environ.get(...)`` to easy handling environment variables, we have support for:
    * sting
    * int
    * bool
    * list

**Watch out** ``get_list`` support only List of str to convert to a list of int for example you should use ``parse_int`` with a list comprehension.

Benchmark
~~~~~~~~~
A decorator named ``timeit`` which can be used on sync and async methods to see execution time.

    If execution time is below to ``0.50 seconds`` there will be no log. Works very well with ``enforce_types``.
    **Maybe** add threshold as environment variable?

Utils | Grouped by returned types.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* boolean
* integer
* string
* datetime
* iterable


.. _Sesotho: https://en.wikipedia.org/wiki/Sotho_language
.. _Poetry: https://github.com/sdispater/poetry
.. _Postman: https://www.getpostman.com
.. _presentation: https://docs.google.com/presentation/d/1RbkpSnGvNpZUGb_rxZrdXsWu4NoraZtWeLaq7KSQMlg/edit
.. _Enforce Annotation Source: https://stackoverflow.com/a/50622643/5676197

.. |python| image:: https://img.shields.io/badge/python-3.7.x-blue.svg
    :alt: Python 3.7.x
    :target: https://www.python.org/downloads/release/python-374/
.. |flake8| image:: https://img.shields.io/badge/code_style-flake8-brightgreen.svg
    :alt: Flake8
    :target: http://flake8.pycqa.org/en/latest/
.. |poetry| image:: https://img.shields.io/badge/dependency_manager-poetry-blueviolet.svg
    :alt: Poetry
    :target: https://poetry.eustace.io
