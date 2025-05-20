import unittest
from main import Fibonacci


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_fibonacci_normal(self):
        test_cases = [
            (0, 0),
            (1, 1),
            (10, 55),
            (100, 354224848179261915075),
            (200, 280571172992510140037611932413038677189525),
        ]
        for test, expected in test_cases:
            with self.subTest(test=test, expected=expected):
                result = self.fibonacci(test)
                self.assertEqual(result, expected)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)

    def test_fibonacci_float(self):
        with self.assertRaises(ValueError):
            self.fibonacci(2.5)

    def test_fibonacci_str(self):
        test_cases = ["", "10", "ten", "."]

        for test in test_cases:
            with self.subTest(test=test):
                with self.assertRaises(ValueError):
                    self.fibonacci(test)

    def tearDown(self):
        self.fibonacci = None
