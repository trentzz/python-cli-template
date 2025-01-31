# python-cli-template

## Quickstart

### Dependencies

- python (would recommend at least 3.10)
- pipx (see pipx page for installation)
- poetry (can be installed with `pipx install poetry`)

### Trying it out

To try the example cli project as is, simply run:

```bash
cd python-cli-template
poetry install
poetry run example -h
```

### Making it your own

1. Change the name of the project!
   1. Change the name in `pyproject.toml`. This name is the name that will appear on pypi when you publish it, but don't worry, if you want the actual cli command to be different, we can change that later. This name cannot include spaces.
   2. Change the folder name `example_python_cli`. This should be the same as the name in the `pyproject.toml` file, but all dashes (`-`) must be replaced with underscores (`_`).
   3. Update internal imports that start with `from example_python_cli.xxxx import xxxx`.
2. Change your cli command in `pyproject.toml`. (see [Cli command name](#cli-command-name))
3. Add your own cli options in `cli.py`. (see [Adding cli options](#adding-cli-options))
4. Add your own files and connect them to the cli. (see [Connecting classes to cli options](#connecting-classes-to-cli-options))

### Installing and running

When you're ready, simply re-run:

```bash
poetry install
poetry run <your-cli-command> -h
```

### Publishing

To publish to pypi:

1. Go to pypi.org and request an API token with publishing permissions.
2. Add the API token.
3. Update your version number in `pyproject.toml`.
4. `poetry publish --build`

And that's it!

## Development process

### Adding cli options

#### Basic options

#### Useful argparse options

### Connecting classes to cli options

### Testing and dependency injection

### Mypy and static analysis

## Explanation and extras

### Poetry

#### Pyproject.toml

##### Cli command name

### Subcommands

#### Adding subcommand options with Argparse

#### Connecting subcommands to classes

### Adding static and reference files

## Contribute
