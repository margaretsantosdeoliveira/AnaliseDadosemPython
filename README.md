# AnaliseDadosemPython
Criando um sistema que analisa os dados contidos no arquivo lista_clientes.csv usando POO, com funcionalidades específicas.

ETAPA 1
1-  Classe CPF - Validador de CPF 
1.1 Funções
•   Remover caracteres que não sejam dígitos do CPF.
•   Verifica se o CPF tem 11 dígitos.
•   Verifica se todos os dígitos não são iguais.
•   Calcula e valida os dois dígitos verificadores do CPF usando o algoritmo.
•   Disponibiliza um atributo para indicar se o CPF é válido ou não.
•   Retorna o CPF com apenas números ao converter o objeto para string.
1.2 Funcionamento
•   Ao criar um objeto CPF, o código remove caracteres que não sejam números.
•   O método _validar executa as regras para verificar se o CPF é válido.
•   O resultado da validação é armazenado em self.valido.
•   Retorna o CPF apenas com números.

2-  Classe endereço - Consulta de endereço por CEP usando a API pública ViaCEP
2.1 Funções:
•   Recebe o CEP e normaliza para conter apenas números.
•   Valida se o CEP tem 8 dígitos.
•   Faz uma requisição HTTP a API ViaCEP para obter dados como estado, cidade e bairro.
•   Disponibiliza os dados do endereço para uso.
•   Permite retornar o endereço formatado como string.
2.2 Funcionamento
•   Ao criar um objeto Endereco com um CEP, a classe valida o formato.
•   Se o CEP for válido, consulta a API ViaCEP para obter os dados.
•   Armazena os dados em atributos (estado, cidade, bairro).
•   Método mostrar_endereco() retorna uma string com o endereço formatado.

3-  Classe Pessoa para tratamento dos nomes com extração do primeiro e segundo nome
3.1 Funções:
•   Primeiro formata os nomes completos para capitalizar, mantendo preposições (da, de, do, das, dos, e) em letras minúsculas.
•   Depois extrai o primeiro nome de um nome completo.
•   Em seguida, extrai o segundo nome ou o conjunto do segundo e terceiro nomes.
•   Trata nomes compostos e as palavras múltiplas. 
•   Consulta a API `genderize.io` para obter o gênero e retorna o gênero mais provável junto com o nível de confiança.
3.2 Funcionamento:
•   O nome completo é convertido para minúsculas e dividido em palavras.
•   Palavras que são preposições são mantidas em minúsculas.
•   Outras palavras são capitalizadas, ou seja, primeira letra maiúscula.
•   O método get_primeiro_nome() retorna a primeira palavra do nome.
•   O método get_segundo_nome() retorna a segunda palavra, ou as segunda e terceira palavras juntas.

ETAPA 2
1.	Leitura de Arquivo CSV em Python
•	Ler um arquivo CSV contendo dados de clientes, usando o módulo csv do Python. 
1.1 Funções:
•	Abrir um arquivo CSV no formato utf-8.
•	Utilizar csv.DictReader para ler os dados como dicionários.
•	Armazenar dados lidos em uma lista de dicionários.
•	Tratamento de possíveis erros

2- Exportar Lista de Pessoas para JSON
•	O arquivo tem uma função que retorna nada, serve para converter uma lista de objetos do tipo pessoa em um arquivo .json. 
2.1 Funções:
•	Convertendo os objetos  do tipo pessoa para dicionários.
•	Salvando os dados no .json.
2.2 Estrutura de saída desejada: 
•	nome_completo, primeiro_nome, segundo_nome, gênero, email, celular, interesse, cpf, endereco.bairro, endereco.cidade, endereco.estado, 

ETAPA 3
1-	CPF Service
1.1	Função:
•	Validação e formatação do CPF
1.2	Funcionalidade:
•	Primeiro formata o CPF, depois verifica se ele é válido.
•	Retorna True se o CPF for válido, ou False se for inválido.

2-  Gender_Service
2.1 Funções:
•   Consulta a API para verificar o gênero
•   Retorna a probabilidade e o nível de confiança

ETAPA 4
•	Testes unitários que verificam se pequenas partes do código e seu funcionamento, utilizando a biblioteca unittest para criar e organizar esses testes de forma padronizada.
