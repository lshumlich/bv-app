#
# pytest utils/functions_test.py -s -k add
# 
#
import unittest
import utils.functions as funcs


class TestFunctions(unittest.TestCase):
    """ Sample of a test suite

    This tests our simple API to ensure the results are proper
    """

    def test_stuff(self):
        print("Running TestFunctions, not a good idea to put print statements in tests.")

    def test_math_add(self):
        assert funcs.math('+', 1, 1) == 2

    def test_math_subtract(self):
        self.assertEqual(funcs.math('-', 1, 1), 0)

    def test_math_bad_operator(self):
        with self.assertRaises(Exception):
            funcs.math('xxx', 1, 1), 2

    def test_math_bad_parm(self):
        with self.assertRaises(Exception):
            funcs.math('+', 1)

        with self.assertRaises(TypeError):
            funcs.math('+', 1, 'xx')

        with self.assertRaises(TypeError):
            funcs.math('+', 1)
