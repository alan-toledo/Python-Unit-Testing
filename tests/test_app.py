import unittest
from app import fibonacci, factorial

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_value_1(self):
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_value_10(self):
        self.assertEqual(fibonacci(10), 89)

class TestFactorial(unittest.TestCase):
    def test_factorial_value_1(self):
        self.assertEqual(factorial(1), 1)