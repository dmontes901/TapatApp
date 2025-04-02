import unittest

class TestCalculadora(unittest.TestCase):
    def test_resta(self):
        resultat = (2 - 3)
        self.assertEqual(resultat, -1)

class TestCalculadora2(unittest.TestCase):
    def test_divisio(self):
        resultat2 = (4 / 0)
        self.assertEqual(resultat2, 0)

if __name__ == '__main__':
    unittest.main()