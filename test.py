import unittest
from main import sumar

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(30,30),60)