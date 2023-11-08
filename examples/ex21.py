"""
Testing the `factorial` method
"""
import unittest
from vin_utils import factorial


class FactorialTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass() called')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass() called')

    def setUp(self) -> None:
        print('setUp() called')

    def tearDown(self) -> None:
        print('tearDown() called')

    def test_factorial_of_valid_input(self):
        print('test_factorial_of_valid_input() called')
        val = 5
        expected = 120
        actual = factorial(val)
        self.assertEqual(expected, actual)

    def test_factorial_of_text(self):
        print('test_factorial_of_text() called')
        try:
            factorial('asd')
            self.fail('Expected to raise TypeError; did not do so!')
        except TypeError:
            pass

    def test_factorial_of_non_numeric(self):
        print('test_factorial_of_non_numeric() called')
        def fn():
            factorial('asd')
        self.assertRaises(TypeError, fn)


unittest.main(module='ex21')  # needed to run in CLI - `python ex21.py`
