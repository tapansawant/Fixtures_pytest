import Divisible


def test_checkDivisibleby5():
    x = 10
    result = Divisible.checkDivisibleby5(x)
    assert True == result


def test_fcheckDivisibleby5():
    x = 11
    result = Divisible.checkDivisibleby5(x)
    assert False == result


def test_checkDivisibleby7():
    x = 14
    result = Divisible.checkDivisibleby7(x)
    assert True == result


def test_fcheckDivisibleby7():
    x = 11
    result = Divisible.checkDivisibleby7(x)
    assert False == result


def test_checkDivisibleby9():
    x = 18
    result = Divisible.checkDivisibleby9(x)
    assert True == result


def test_fcheckDivisibleby9():
    x = 17
    result = Divisible.checkDivisibleby9(x)
    assert False == result


def test_checkDivisibleby11():
    x = 22
    result = Divisible.checkDivisibleby11(x)
    assert True == result


def test_fcheckDivisibleby11():
    x = 23
    result = Divisible.checkDivisibleby11(x)
    assert False == result
