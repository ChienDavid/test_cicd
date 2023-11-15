import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 3, 5]), 9, 'The result should be 9')

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 3, 6)), 10, 'The result should be 10')


if __name__ == '__main__':
    unittest.main()
