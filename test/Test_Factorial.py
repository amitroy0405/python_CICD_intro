import pytest
from src.factorial import Factorial

@pytest.fixture()
def fact():
    fact = Factorial(5)
    return fact


def test_getValueofFactorial(fact):
    assert fact.get_factorialValue() == 120 

def test_totalofFactorial(fact):
    assert fact.sum_factorial() == 600