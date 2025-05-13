# tests/test_operacoes.py

import unittest
from calculadora import operacoes

class TestOperacoes(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(operacoes.somar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(operacoes.subtrair(5, 2), 3)

if __name__ == "__main__":
    unittest.main()
