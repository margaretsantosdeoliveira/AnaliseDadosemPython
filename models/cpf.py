import re
"""modulo de expressoes para alterar strings"""

class CPF:
    """Remover caracteres que não sejam dígitos do CPF.
•	Verifica se o CPF tem 11 dígitos.
•	Verifica se todos os dígitos não são iguais.
•	Calcula e valida os dois dígitos verificadores do CPF usando o algoritmo.
•	Disponibiliza um atributo para indicar se o CPF é válido ou não.
•	Retorna o CPF com apenas números ao converter o objeto para string.
"""
    def __init__(self, numero: str) -> str:
        self.numero = self._somente_digitos(numero) #remover oq não for digito
        self.valido = self._validar() 

    def _somente_digitos(self, cpf: str) -> str:
        return re.sub(r'\D', '', cpf) #remover itens que não são números
        
    def _validar(self) -> bool:  
        cpf = self.numero
        if len(cpf) != 11 or cpf == cpf[0] *11: 
            #não pode ter todos os digitos iguais ou obrigatório ter 11 digitos
            return False
        
        def calcular_digito(parcial: str, peso: int) -> int:
            total = sum(int(d) * p for d, p in zip(parcial, range(peso, 1, -1)))
            #calcular a soma dos digitos de uma sequencia
            resto = (total *10) %11
            return 0 if resto == 10 else resto 

        dig1 = calcular_digito(cpf[:9], 10) #calcula o primeiro digito
        dig2 = calcular_digito(cpf[:10], 11) #calcula o segundo usando os 10 primeiros numeros
        
        return cpf[-2:] == f'{dig1}{dig2}' #retorna a verificação dos ultimos digitos do CPF
        
    def __str__(self):
        return self.numero