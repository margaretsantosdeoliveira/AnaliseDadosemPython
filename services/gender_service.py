import requests

class GenderService:
    """Será responsável por consultar uma API extena para verificar o genero com
    base no primeiro nome da classe pessoa.py """
    def __init__(self, api_url='https://api.genderize.io'):
        self.api_url = api_url

    def identificar_genero(nome_completo):
        """Define a função que vai identificar o genero com base no nome"""    
        primeiro_nome = get_primeiro_nome(nome_completo)
        url = f"https://api.genderize.io/?name={primeiro_nome}"
        resposta = requests.get(url)
        """Verifica na HTTP GET - API e o resultado é armazenado na variável resposta."""
        if resposta.status_code == 200: #verificando se a resposta foi bem sucedida
            dados = resposta.json() #convertendo o conteúdo em dicionário
            genero = dados.get("gender")
            probabilidade = dados.get("probability")
            
            if genero:
                return f"{primeiro_nome} provavelmente é {genero} (confiança: {float(probabilidade) * 100:.1f}%)."
            else:
                return f"Não foi possível identificar o gênero."