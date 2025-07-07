import unittest
from pessoas import Pessoa

class TestPessoa(unittest.TestCase):
    def test_fomatacao_nome_preposicoes(self):
        pessoa = Pessoa("Maria do Carmo")
        self.assertEqual(pessoa.nome_completo, "Maria do Carmo")
        self.assertEqual(pessoa.primeiro_nome, "Maria")
        self.assertEqual(pessoa.segundo_nome, "do Carmo")
        

    def test_nome_sem_preposicoes():
        pessoa = Pessoa("Maria Oliveira")
        self.assertEqual(pessoa.nome_completo, "Maria Oliveira")
        self.assertEqual(pessoa.primeiro_nome, "Maria")
        self.assertEqual(pessoa.segundo_nome, "Oliveira")

if __name__ == '__main__':
    unittest.main()
    