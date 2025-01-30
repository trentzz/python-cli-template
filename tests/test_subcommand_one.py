import pytest

from example_python_cli.subcommand_one import SubcommandOne


def test_subcommand_one_run():
    subcommand_one = SubcommandOne()
    subcommand_one.run()
    assert True


def test_subcommand_one_raises_runtime_error():
    subcommand_one = SubcommandOne()
    with pytest.raises(RuntimeError):
        subcommand_one.raises_runtime_error()
