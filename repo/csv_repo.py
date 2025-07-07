import csv

def ler_csv(lista_clientes.csv):
    """Abrir o arquivo CSV
    Usar o Dict para ler o arquivo como dicionário
    Armazenar em uma lista
    Fazer o tratamento dos erros
    Retornar uma lista"""
    dados = []

    try:
        with open(lista_clientes.csv, newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                dados.append(linha)
        return dados

    except FileNotFoundError:
        print(f"Erro: '{lista_clientes.csv}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

    return []  