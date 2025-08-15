# test_app.py
import pytest
from app import calculate_sum, is_positive, multiply, greet # Make sure to import greet if you want to test it too

# --- Passing Test Cases (3) ---

def test_calculate_sum_positive():
    assert calculate_sum(2, 3) == 5

def test_is_positive_true():
    assert is_positive(10) is True

def test_is_positive_false_zero():
    assert is_positive(0) is False

# --- Failing Test Cases (2) ---

def test_calculate_sum_negative_incorrect_expectation():
    # This test expects an incorrect result for negative numbers
    assert calculate_sum(-1, -1) == 0 # EXPECTED TO FAIL: -1 + -1 is -2, not 0

def test_multiply_buggy_function():
    # This test expects correct multiplication, but the function is buggy
    assert multiply(2, 3) == 6 # EXPECTED TO FAIL: multiply(2,3) returns 5 (2+3)
