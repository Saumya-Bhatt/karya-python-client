# Contributing

Firstly, thank you for considering contributing to this project. We appreciate your time and effort. Please read the following guidelines before contributing.

## How can I contribute?

Karya is in no way a finished project. There's always room for improvements. Be it in terms of performance or documentation ro adding new features or fixing bugs! Following are some of the ways one can contribute to Karya:

1. Documentation - There is never enough documentation to explain something simply by reading it. But we can try!
2. Bug Fix - Noticed a bug? Just report it! Or if you're a seluth, go and raise a PR! This is in no way a bug-free software.
3. New Features - Currently the python client is a web-based client beacause the _karya server_ itself supports REST calls currently. But who knows, in the future we might move to something better!
4. Refactoring - There are always better ways to write a code. Go ahead and give it a shot at writing this client better, to make it more concise and easier to read.

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
