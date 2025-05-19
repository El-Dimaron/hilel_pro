import unittest
from main import Fibonacci, formatted_name


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        print("Set up an instance of the Fibonacci class before each test")
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
        print("Tear down an instance of the Fibonacci class after each test")
        self.fibonacci = None


class TestFormattedName(unittest.TestCase):

    def test_formatted_name_normal(self):
        test_cases = [
            (('John', 'Smith', 'Petrovich'), "John Petrovich Smith"),
            (('joHn', 'smiTh', ' petroviCh  '), "John  Petrovich   Smith"),
            (('john', 'smith'), "John Smith"),
            (('john', 'smith', ' '), "John   Smith"),
        ]
        for test, expected in test_cases:
            with self.subTest(test=test, expected=expected):
                result = formatted_name(*test)
                self.assertEqual(result, expected)

    def test_formatted_name_empty(self):
        self.assertEqual(formatted_name('', ''), " ")

    def test_formatted_name_wrong_data_type(self):
        test_cases = [
            ('john', 69),
            (1.2, "smith"),
            ('john', "smith", 13),
            (["John", "Adnriyovych"], "Smith"),
        ]

        for test in test_cases:
            with self.subTest(test=test):
                with self.assertRaises(TypeError):
                    formatted_name(*test)
