import unittest

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        resultat = (2 + 3)
        self.assertEqual(resultat, 5)

if __name__ == '__main__':
    unittest.main()