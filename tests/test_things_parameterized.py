#!/usr/bin/python3

# This is an example of how to create unit tests with the pytest lib.
# All functions that starts with the name test* will be executed when calling pytest.
# Functions not starting with test* will be ignored.
# Instead of creating one test for each input we can instead create one test for
# each function and then parameterize the values to test.

import src.find_13_in_number as task3
import pytest

@pytest.mark.parametrize("num, output", [(413044, 1), (18939213094, 6), (26, None), (9, None), (13940, 0), (4839813, 5), (241345, 2), (40013, 3)])
def test_13_pos_math(num, output):
    assert task3.find_13_by_math(num) == output, f"Should be {output}"

@pytest.mark.parametrize("num, should_not_be, should_be", [(413044, -1, 1)])
def test_13_pos_math_negation(num, should_not_be, should_be):
    assert task3.find_13_by_math(num) != should_not_be, f"Should be {should_be}"

def test_13_pos_math_10():
    # Test that you cannot enter a string to this function
    with pytest.raises(TypeError):
        result = task3.find_13_by_math("40013")

def test_13_pos_string_1():
    assert task3.find_13_by_string_conversion("413044") == 1, "Should be 1"



