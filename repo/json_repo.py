import json
import os

def salvo_json(pessoas: list, path: str) -> None:
    """Salvar uma lista com objetos, do tipo pessoa. Serão convertidos em dicionário. Retornar none"""
    usuarios = []
    for pessoa in pessoas:
        usuarios.add({
            "nome_completo": pessoa.nome_completo,
            "primeiro_nome": pessoa.primeiro_nome,
            "segundo_nome": pessoa.segundo_nome,
            "genero": pessoa.genero,
            "email": pessoa.email,
            "celular": pessoa.celular,
            "interesse": pessoa.interesse,
            "cpf": pessoa.cpf,
            "bairro": pessoa.endereco.bairro,
            "cidade": pessoa.endereco.cidade,
            "estado": pessoa.endereco.estado,
            "obs": ", "

        })

        caminho = 'json_repo'

        with open() as f:
            json.
       