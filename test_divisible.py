import Divisible
import pytest


@pytest.fixture
def input():
    a = 25
    return a


def test_checkDivisibleby5(input):
    # x = 10
    result = Divisible.checkDivisibleby5(input)
    assert True == result


def test_fcheckDivisibleby5(input):
    result = Divisible.checkDivisibleby5(input)
    assert False == result


def test_checkDivisibleby7(input):
    result = Divisible.checkDivisibleby7(input)
    assert True == result


def test_fcheckDivisibleby7(input):
    result = Divisible.checkDivisibleby7(input)
    assert False == result


def test_checkDivisibleby9(input):
    result = Divisible.checkDivisibleby9(input)
    assert True == result


def test_fcheckDivisibleby9(input):
    result = Divisible.checkDivisibleby9(input)
    assert False == result


def test_checkDivisibleby11(input):
    result = Divisible.checkDivisibleby11(input)
    assert True == result


def test_fcheckDivisibleby11(input):
    result = Divisible.checkDivisibleby11(input)
    assert False == result
