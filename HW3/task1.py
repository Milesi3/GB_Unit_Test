import unittest

def is_even_odd_number(n):
    if n % 2 == 0:
        return True
    return False

class TestIsEvenOddNumber(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even_odd_number(4))

    def test_odd_number(self):
        self.assertFalse(is_even_odd_number(7))

    def test_zero(self):
        self.assertTrue(is_even_odd_number(0))

    def test_negative_even_number(self):
        self.assertTrue(is_even_odd_number(-2))

    def test_negative_odd_number(self):
        self.assertFalse(is_even_odd_number(-3))

if __name__ == '__main__':
    unittest.main()
