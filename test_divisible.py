import Divisible
import pytest


# @pytest.fixture()
# def input():
#     a = 25
#     return a

@pytest.mark.parametrize("num,output", [(5, True), (2, False), (10, True), (7, False)])
def test_checkDivisibleby5(num, output):
    result = Divisible.checkDivisibleby5(num)
    assert result == output


#
#
# def test_fcheckDivisibleby5(input):
#     result = Divisible.checkDivisibleby5(input)
#     assert False == result
#
@pytest.mark.parametrize("num,output", [(7, True), (2, False), (14, True), (33, False)])
def test_checkDivisibleby7(num, output):
    result = Divisible.checkDivisibleby7(num)
    assert result == output


#
# def test_fcheckDivisibleby7(input):
#     result = Divisible.checkDivisibleby7(input)
#     assert False == result
#
@pytest.mark.parametrize("num,output", [(9, True), (2, False), (18, True), (33, False)])
def test_checkDivisibleby9(num, output):
    result = Divisible.checkDivisibleby9(num)
    assert result == output


#
# def test_fcheckDivisibleby9(input):
#     result = Divisible.checkDivisibleby9(input)
#     assert False == result
#
@pytest.mark.parametrize("num,output", [(11, True), (2, False), (22, True), (34, False)])
def test_checkDivisibleby11(num, output):
    result = Divisible.checkDivisibleby11(num)
    assert result == output
#
# def test_fcheckDivisibleby11(input):
#     result = Divisible.checkDivisibleby11(input)
#     assert False == result
