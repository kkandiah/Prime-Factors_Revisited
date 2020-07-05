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
    assert p_1.arg == ValueError
