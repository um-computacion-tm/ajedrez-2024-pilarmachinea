import unittest
from main import suma

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(suma(1,2), 3)

    def test_sum2(self):
        self.assertEqual(suma(3,3), 6)

    def test_sum3(self):
        self.assertEqual(suma(6,3), 9)

if __name__ == '__main__':
    unittest.main()