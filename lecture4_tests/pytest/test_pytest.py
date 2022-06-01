import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(20, -10) == 10
    assert Calculator.add(10, 20) != 52


def test_subtract():
    assert Calculator.subtract(24, 9) == 15
    assert Calculator.subtract(100, 105) == -5
    assert Calculator.subtract(100, 9) != 15


def test_multiply():
    assert Calculator.multiply(3, 5) == 15
    assert Calculator.multiply(30, 0.5) == 15
    assert Calculator.multiply(10, 10) != 1000


def test_divide():
    assert Calculator.divide(75, 5) == 15
    assert Calculator.divide(10, 20) == 0.5
    assert Calculator.divide(75, 15) != 15
    with pytest.raises(ValueError):
        Calculator.divide(75, 0)
