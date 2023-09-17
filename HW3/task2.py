import unittest

def numberInInterval(n):
    return 25 < n < 100

class TestNumberInInterval(unittest.TestCase):
    def test_number_within_interval(self):
        self.assertTrue(numberInInterval(50))

    def test_number_at_lower_boundary(self):
        self.assertFalse(numberInInterval(25))

    def test_number_at_upper_boundary(self):
        self.assertFalse(numberInInterval(100))

    def test_number_below_interval(self):
        self.assertFalse(numberInInterval(10))

    def test_number_above_interval(self):
        self.assertFalse(numberInInterval(150))

if __name__ == '__main__':
    unittest.main()
