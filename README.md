# visiumlint - Visum linting package
![CI](https://github.com/VisiumCH/visium-lint/actions/workflows/ci.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/visiumlint.svg)](https://badge.fury.io/py/visiumlint)

All of your favorite linters and formatters gathered in a single command!

Visiumlint relies on `black`, `isort`, `pylint`, `pydocstyle` and `mypy`.

# Installation

`pipenv install visiumlint`

# Example usage
- Create a pipenv environment
- Install visiumlint using the above command.
- Activate the environment using `pipenv shell`
- Run the visium package by running the command `visiumlint`

# Hook

You can automate visiumlint when commiting changes with a [git hook](https://githooks.com/) and the [pre-commit](https://pre-commit.com/) library. The hook will not execute `Pylint`.

- Make sure to have installed pre-commit, or else run `pip install pre-commit`

- Add a file called `.pre-commit-config.yaml` to the root of your project:
```yaml
repos:
-     repo: https://github.com/VisiumCH/visiumlint
      rev: 1.6.0
      hooks:
      -     id: visiumlint
            language: python
            types: [python]
            require_serial: true
```
- Run `pre-commit autoupdate`. This will use the latest available version of visiumlint.
# Development
## Manage your python environment

### Set up the environment
The python environment is managed with `pipenv`. You can set up your environment with the following steps:

- Run `pipenv lock` to generate the `Pipfile.lock` which lists the version of your python packages.
- Run `pipenv install --dev` to actually create a virtual environment and install the python packages. The flag `--dev` allows to install the development packages (for linting, ...).



### Activate and use your environment

To run code under your newly set up environment, you have two options:

- *Open a shell*: activate your environment with `pipenv shell`. Note that this command will also source environment variables from your `.env` file.

- *Pipenv CLI*: you can also run scripts using your python environment with `pipenv run script.py`. This can be convenient within a `docker build` execution for example.


### Some tips about pipenv

**About deploying in production**

Note that when deploying your code in production, you should not install the dev package, it is preferred to run the following command: `pipenv install --system --deploy`.

**About using git with pipenv**

Make sure to commit the `Pipfile.lock` in `git`. It will make your code more reproducible because other developers could install the exact same python packages as you used.

---
