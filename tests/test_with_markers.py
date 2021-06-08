#!/usr/bin/python3

# This is an example of how to create unit tests with the pytest lib and use markers.
# All functions that starts with the name test* will be executed when calling pytest.
# Functions not starting with test* will be ignored.


import src.find_13_in_number as task3
import pytest

@pytest.mark.great
def test_13_pos_math_1():
    assert task3.find_13_by_math(413044) == 1, "Should be 1"

@pytest.mark.great
def test_13_pos_math_2():
    assert task3.find_13_by_math(413044) != -1, "Should be 1"

@pytest.mark.other
def test_13_pos_math_3():
    assert task3.find_13_by_math(18939213094) == 6, "Should be 6"

def test_13_pos_math_4():
    assert task3.find_13_by_math(26) == None, "Should be None"

def test_13_pos_math_5():
    assert task3.find_13_by_math(9) == None, "Should be None"

def test_13_pos_math_6():
    assert task3.find_13_by_math(13940) == 0, "Should be 0"

def test_13_pos_math_7():
    assert task3.find_13_by_math(4839813) == 5, "Should be 5"

def test_13_pos_math_8():
    assert task3.find_13_by_math(241345) == 2, "Should be 2"

def test_13_pos_math_9():
    assert task3.find_13_by_math(40013) == 3, "Should be 3"

@pytest.mark.exceptiontest
def test_13_pos_math_10():
    # Test that you cannot enter a string to this function
    with pytest.raises(TypeError):
        result = task3.find_13_by_math("40013")

def test_13_pos_string_1():
    assert task3.find_13_by_string_conversion("413044") == 1, "Should be 1"

