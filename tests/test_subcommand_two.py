import pytest

from example_python_cli.subcommand_two import SubcommandTwo


def test_subcommand_two_run():
    subcommand_two = SubcommandTwo()
    subcommand_two.run()
    assert True


def test_subcommand_two_raises_runtime_error():
    subcommand_two = SubcommandTwo()
    with pytest.raises(RuntimeError):
        subcommand_two.raises_runtime_error()
