import pytest

from example_python_cli.basic import Basic


def test_basic_run():
    """
    Test the run method of the Basic class
    """
    basic = Basic("a")
    basic.run()
    assert True


def test_basic_raises_runtime_error():
    """
    Test the raises_runtime_error method of the Basic class
    """
    basic = Basic("a")
    with pytest.raises(RuntimeError):
        basic.raises_runtime_error()
