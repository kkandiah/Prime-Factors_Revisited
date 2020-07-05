#prime.py
"""
a function to generate prime factors of a given number
using an iterator class, and then, a simpler generator class.
"""
class PrimeFactors:
    """
    docstring for Prime_Factors.
    """

    def __init__(self, arg):
        if not isinstance(arg, int):
            self.arg = ValueError
        else:
            self.arg = arg
