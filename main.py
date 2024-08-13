import unittest

def sumar(a,b):
    return a+b

if __name__ == '__main__':
    sumar(30,30)

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(30,30),60)