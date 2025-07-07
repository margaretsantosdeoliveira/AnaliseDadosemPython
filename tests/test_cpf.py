import unittest
from cpf import CPF

class TestCPF(unittest):
    def test_cpf_valido(self):
        cpf = CPF('123.456.789-10')
        self.assertTrue(cpf.valido)
        self.assertEqual(str(cpf), '12345678910')

    def test_cpf_digitos_repetidos(self):
        cpf = CPF('111.111.111-11')
        self.assertFalse(cpf.valido)
        self.assertEqual(str(cpf), '11111111111')

    def test_cpf_invalido_tamanho(self):
        cpf = CPF('123.456.789')
        self.assertFalse(cpf.valido)
        self.assertEqual(str(cpf), '123456789')

if __name__ == '__main__':
    unittest.main()
    