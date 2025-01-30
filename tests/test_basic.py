import pytest

from example_python_cli.basic import Basic


def test_basic_run():
    basic = Basic()
    basic.run()
    assert True


def test_basic_raises_runtime_error():
    basic = Basic()
    with pytest.raises(RuntimeError):
        basic.raises_runtime_error()
