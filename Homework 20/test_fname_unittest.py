import unittest
from main import formatted_name


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
