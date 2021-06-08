#!/usr/bin/python3

# This is an example of how to use the built in unittest lib to create test functions
# that can use the different variations of assert, like assertEqual. Those tests
# can be executed both from unittest and from pytest as long as the functions starts
# with test*. Functions not starting with test* will be ignored.
# The classes that inherits from unittest.TestCase can be called whatever.

# Methods could be
# .assertEqual(a, b)       // OK if a==b
# .assertTrue(x)           // OK if bool(x) is True
# .assertFalse(x)
# .assertIs(a, b)          // OK if a is b
# .assertIsNone(x)         // OK if x is None
# .assertIn(a, b)          // OK if a in b
# .assertIsInstance(a, b)  // OK if a is an instance of type b
# (Most of above also has the opposite, like .assertIsNotInstance etc.)

import unittest
import src.find_13_in_number as task3
import pytest

class TestTask3(unittest.TestCase):

    @pytest.mark.funtest # It is possible to only run this by using -m funtest
    def test_13_pos_math_1(self):
        self.assertEqual(task3.find_13_by_math(413044), 1, "Should be 1")

    def prov_13_pos_math_2(self): # This is never run since it does not start with test
        self.assertNotEqual(task3.find_13_by_math(413044), -1, "Should be 1")

    def test_13_pos_math_3(self):
        self.assertEqual(task3.find_13_by_math(18939213094,), 6, "Should be 6")

    def test_13_pos_math_4(self):
        self.assertIsNone(task3.find_13_by_math(26), "Should be None")

    def test_13_pos_math_5(self):
        self.assertIsNone(task3.find_13_by_math(9), "Should be None")

    def test_13_pos_math_6(self):
        self.assertEqual(task3.find_13_by_math(13940), 0, "Should be 0")

    def test_13_pos_math_7(self):
        self.assertEqual(task3.find_13_by_math(4839813), 5, "Should be 5")

    def test_13_pos_math_8(self):
        self.assertEqual(task3.find_13_by_math(241345), 2, "Should be 2")

    def test_13_pos_math_9(self):
        self.assertEqual(task3.find_13_by_math(40013), 3, "Should be 3")

    def test_13_pos_math_10(self):
        # Test that you cannot enter a string to this function
        with self.assertRaises(TypeError):
            result = task3.find_13_by_math("40013")

class TestTask4(unittest.TestCase):
    def test_13_pos_string_1(self):
        self.assertEqual(task3.find_13_by_string_conversion("413044"), 1, "Should be 1")

if __name__ == '__main__':
    unittest.main()
