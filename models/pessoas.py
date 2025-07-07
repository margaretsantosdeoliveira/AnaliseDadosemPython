import re
import requests

class Pessoa:
    """•	Primeiro formata os nomes completos para capitalizar, mantendo preposições (da, de, do, das, dos, e) em letras minúsculas.
•	Depois extrai o primeiro nome de um nome completo.
•	Em seguida, extrai o segundo nome ou o conjunto do segundo e terceiro nomes.
•	Trata nomes compostos e as palavras múltiplas. 
"""
    preposicoes = ['da', 'de', 'do', 'das', 'dos', 'e']

    def __init__(self, nome_completo:str) -> None: #retorna nome pois apenas inicia o objeto
        self.nome_completo = self.formatar_nome(nome_completo)
        self.primeiro_nome = self.get_primeiro_nome() #extrair primeiro nome
        self.segundo_nome = self.get_segundo_nome() #extrair segundo nome

        self.genero = genero
        self.email = email
        self.celular = celular
        self.interesse = interesse

    def formatar_nome(self, nome_completo: str) -> str:
        partes = nome_completo.lower().split() #converter todos os nomes para letras minúsculas e depois dividir
        nome_formatado = [] #lista para armazenar cada parte do nome

        for parte in partes: #para cada parte na lista, o nome é dividido em palavras min
            if parte in self.preposicoes: #verifica se a palavra está na lista
                nome_formatado.append(parte) #se for preposição, adiciona na lista nome_formatado
            else:
                 nome_formatado.append(parte.capitalize()) #colocar a primeira letra maiuscula

        return ' '.join(nome_formatado) #juntar todas as palavras da lista em unica str

    def get_primeiro_nome(self) -> str:
        partes = self.nome_completo.split() #dividir em lista usando separador
        return partes [0] if len(partes) >0 else '' 
    #retornar primeira palavra se tiver ou se a lista for vazia retornar a string

    
    def get_segundo_nome(self) -> str:
         partes = self.nome_completo.split() #dividindo nome em palavras
         if len(partes) > 2:
             return ' '.join(partes[1:3])
         #se tiver 3 ou mais palavras retornar elas juntas e separadas pelo espaço
         elif len(partes) > 1:
             return partes[1] #retornar a segunda palavra se apenas tiver duas
         else:
             return '' #se houver menos de duas palavras, retornar string vazia
        
    
  
         
        