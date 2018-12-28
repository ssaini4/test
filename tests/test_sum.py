import unittest
from src.sum import addition

class TestSum(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(8, addition(4,4))
        self.assertNotEqual(7, addition(3,3))

