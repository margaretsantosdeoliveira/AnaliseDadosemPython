import re
from cpf import CPF

class CPF:
    """Verifica a formatação e valida o CPF"""
    @staticmethod
    def formatar_cpf(cpf: str) -> str:
        """Remover os caracteres não numéricos e ao final devolver apenas dígitos"""
        return re.sub(r'\D', '', cpf)
    
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Validar um cpf após formatação e verficar a validade, retornar verdadeiro se for válido e false caso contrário """
        cpf_formatado = ServicoCPF.formatar_cpf(cpf)
        return CPF.validar_cpf(cpf_formatado)
