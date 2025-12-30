import pytest

def func_retval():
    some_int = 50
    return some_int

@pytest.mark.xfail
def test_func_one(input_value):
    assert func_retval() < input_value

@pytest.mark.skip
def test_func_two(input_value):
    assert func_retval() > input_value