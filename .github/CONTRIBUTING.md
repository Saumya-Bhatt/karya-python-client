# Contributing

Firstly, thank you for considering contributing to this project. We appreciate your time and effort. Please read the following guidelines before contributing.

## Local Setup

1. Clone the repository
2. Poetry is used for dependency management. Install poetry using the following command:
    ```shell
    pip install poetry
    ```
3. Install the dependencies using the following command:
    ```shell
    poetry install
    ```
4. Activate the virtual environment using the following command:
    ```shell
    poetry shell
    ```
5. And you are good to go! Try running one of the sample to ensure that everything is working fine.
    ```shell
    poetry run python ./samples/make_recurring_call.py
    ```

## Formatting and Linting

**NOTE:** Ruff formatting is setup as a pre-commit hook. Hence ensure that your PR has been properly formatted before pushing.

The [ruff](https://docs.astral.sh/ruff/) linter and formatter will be installed as a project dependency. To format, run
```shell
ruff format
```

For VSCode, you can install the [plugin](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) and add the following to `settings.json`:
```
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        }
        "editor.defaultFormatter": "charliermarsh.ruff",
    }
```