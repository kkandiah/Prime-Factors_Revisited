#prime.py
"""
a function to generate prime factors of a given number
using an iterator class, and then, a simpler generator class.
"""
class PrimeFactors:
    """
    docstring for Prime_Factors.
    """
    def __init__(self, number):
        if not isinstance(number, int):
            self.number = ValueError
        else:
            self.number = number

    def __iter__(self):
        """
        Returns the instance object which is an iterator.
        """
        self.control = 0
        return self

    def __next__(self):
        """
        Defines the instance object as an iterator.
        """
        if self.number == 1 or self.control == 1:
            raise StopIteration
        i = 2
        while i * i <= self.number:
            if self.number % i:
                i += 1
            else:
                self.number //= i
                prime_factor = i
                return prime_factor

        if self.number > 1:
            prime_factor = self.number
            self.control = 1
            return prime_factor
