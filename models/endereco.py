import re
import requests #modulo usado para requisição de HTTP

class Endereco:
    """Recebe o CEP e normaliza para conter apenas números.
•	Valida se o CEP tem 8 dígitos.
•	Faz uma requisição HTTP a API ViaCEP para obter dados como estado, cidade e bairro.
•	Disponibiliza os dados do endereço para uso.
•	Permite retornar o endereço formatado como string.
""" 
    def __init__(self, cep: str) -> str:
        self.numero = re.sub(r'\D', '', cep) #deixa só números

        if len(self.cep) !=8: #verifica quantidade de dígitos
            raise ValueError ('CEP inválido')
        
        #iniciando atributos de instancia do objeto com valores vazios do tipo string
        self.estado = ''
        self.cidade = ''
        self.bairro = ''

        self.buscar_dados()  #buscar os dados ViaCEP

    def buscar_dados(self) -> None:
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        #pega a url para consultar a API usando o self.cep
        resposta = requests.get(url) #faz a requisição na url e guarda a resposta
        dados = resposta.json() #converte a resposta json em um dicionario chamado dados

        if 'erro' in dados: #se encontrar erro significa que CEP não existe ou não foi encontrado
            raise ValueError('CEP não encontrado')
        
        self.estado = dados['uf']
        self.cidade = dados['localidade']
        self.bairro = dados['bairro']

    def mostrar_endereco(self) -> str:
        return f'{self.bairro}, {self.cidade} - {self.estado}'
    #retornano uma string formatada com o endereço completo

    
        
