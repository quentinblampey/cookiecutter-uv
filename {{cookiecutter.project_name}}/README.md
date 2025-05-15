# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Getting started

### Requirements

The project uses `uv` as a Python package manager. If not already installed, see [their official documentation](https://docs.astral.sh/uv/getting-started/installation/), or run the command below on MacOS or Linux:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

Run the commands below to install the package.

```bash
git clone https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
cd {{cookiecutter.project_name}}

make install # or just `uv sync`
```

> Note: the `make install` command will install the dependencies with `uv`, as well as the [`pre-commit hooks`](https://pre-commit.com/).

## Usage

### Documentation

You can serve the documentation:

```sh
make docs
```

### Code quality check

You can run the code quality check as below. It will run the pre-commit and mypy.

> Note that the pre-commit are run before any commit anyway, but not mypy.

```sh
make check
```

### Tests

You can run the tests via:

```sh
make test
```

Afterward, open the report with `open htmlcov/index.html`
