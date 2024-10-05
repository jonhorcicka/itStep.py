import unittest

def faktorial(self):
    pass

class TestFaktorial(unittest.TestCase):
    def test_nula_jedna(self):
        self.assertEqual(faktorial(0), 1)
        self.assertEqual(faktorial(1), 1)

    def test_kladne_cislo(self):
        self.assertEqual(faktorial(5), 120)
    
    def test_zaporne_cislo(self):
        with self.assertRaises(ValueError):
            faktorial(-1)

unittest.main()