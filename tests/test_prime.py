#test_prime.py
"""
A unit test module for prime module
"""

import prime

def  test_valueerror():
    """
    asserts that when prime_factors is called with a data type
    that is not an integer (e.g. a string or float), a ValueError is raised.
    """
    p_1 = prime.PrimeFactors('a')
    assert p_1.number == ValueError

def test_one():
    """
    asserts that when prime_factors is called with 1,
    an empty list will be generated
    """
    p_1 = list(prime.PrimeFactors(1))
    assert p_1 == []

def test_two():
    """
    asserts that when prime_factors is called with 2,
    the list [2] will be generated
    """
    p_1 = list(prime.PrimeFactors(2))
    assert p_1 == [2]

def test_three():
    """
    asserts that when prime_factors is called with 3,
    the list [3] will be generated
    """
    p_1 = list(prime.PrimeFactors(3))
    assert p_1 == [3]

def test_four():
    """
    asserts that when prime_factors is called with 4,
    the list [2, 2] will be generated
    """
    p_1 = list(prime.PrimeFactors(4))
    assert p_1 == [2, 2]

def test_six():
    """
    asserts that when prime_factors is called with 6,
    the list [2, 3] will be generated
    """
    p_1 = list(prime.PrimeFactors(6))
    assert p_1 == [2, 3]

def test_eight():
    """
    asserts that when prime_factors is called with 8,
    the list [2, 2, 2] will be generated
    """
    p_1 = list(prime.PrimeFactors(8))
    assert p_1 == [2, 2, 2]

def test_nine():
    """
    asserts that when prime_factors is called with 9,
    the list [3, 3] will be generated
    """
    p_1 = list(prime.PrimeFactors(9))
    assert p_1 == [3, 3]
