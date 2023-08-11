1.1.1
~~~~~
11.08.2023
    * Add Makefile;
    * Add `load_multiple_dotenvs` method in `jara_utils.dotenv_configs`;
    * Add two new extras: `dotenv` and `all`;

1.1.0
~~~~~
10.08.2023
    * Remove `update.sh` script;
    * Remove `flake8` and all the flake8 plugins;
    * Add `ruff` and `black`
    * Apply changes required by `ruff` and `black`
    * Move `setup.cfg` to `pyproject.toml`
    * Rename `exceptions.EnvironmentVariableNotFound` to `exceptions.EnvironmentVariableNotFoundError`
    * Remove `update.sh` script
    * Drop support for 3.9

1.0.0
~~~~~
17.01.2023
    * Add python 3.11 and remove 3.8 from CI/CD.
    * Updating pytz (2022.1 -> 2022.7.1)
    * Updating types-pytz (2021.3.6 -> 2022.7.1.0)
    * Updating ipdb (0.13.9 -> 0.13.11)
    * Updating ipython (8.2.0 -> 8.8.0)
    * Updating pytest-sugar (0.9.4 -> 0.9.6)

0.3.1
~~~~~
03.01.2022
    * Update ``poetry.lock``;

0.3.0
~~~~~
03.01.2022
    * Drop support for Python 3.7 and add support for Python 3.8;
    * Add ``aenumerate`` and ``async_grouper``;
    * Add ``flake8-commas`` and ``flake8-eradicate``;

0.2.1
~~~~~
13.07.2021
   * Updating faker (8.10.0 -> 8.10.1)

0.2.0
~~~~~
07.07.2021
   * Updated docs, cleanup github actions;
   * Moved ``pytest-sugar`` and ``pytest-deadfixtures`` to dev dependencies;
   * Added ``ipdb`` and ``iptyon`` to dev dependencies;
   * Added ``update.sh`` script, to update all the dependencies to last version;
   * Updating pytz (2020.5 -> 2021.1)
   * Installing types-pytz (2021.1.0)
   * Updating flake8 (3.8.4 -> 3.9.2)
   * Updating flake8-plugin-utils (1.3.1 -> 1.3.2)
   * Updating flake8-annotations (2.5.0 -> 2.6.2)
   * Updating flake8-comprehensions (3.3.1 -> 3.5.0)
   * Updating flake8-multiline-containers (0.0.17 -> 0.0.18)
   * Updating flake8-pytest-style (1.3.0 -> 1.5.0)
   * Updating flake8-simplify (0.12.0 -> 0.14.1)
   * Updating pytest (6.2.1 -> 6.2.4)
   * Updating pytest-asyncio (0.14.0 -> 0.15.1)
   * Updating pytest-cov (2.11.1 -> 2.12.1)

0.1.5
~~~~~
25.01.2021
   * Add some flake8 plugins and bandit;

0.1.4
~~~~~
01.11.2020
    * Update annotation for CLIOutput.error and CLIOutput.fail;
    * Update description;

0.1.3
~~~~~
01.11.2020
    * Small updates for pypi;

0.1.2
~~~~~
30.10.2020
    * Added CLI Output for fancy prints;
    * Added ``TextColor`` in constants;
    * Add all methods/classes in ``__init__`` file for shorter imports;

0.1.1
~~~~~
30.10.2020
    * Add a changelog file;
    * Update url for project in pypi;
