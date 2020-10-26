"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

Recapitulando dicionários:

dicionario = {
    "curso": "Programação em Python"
}

print(dicionario)
print(dicionario["curso"])

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor de default, podendo utilizar um
lambda para isso. Esse valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma
chave que não existe, essa chave será criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores.
"""

# Fazendo import:

from collections import defaultdict

dicionario = defaultdict(lambda: "valor_padrão")

dicionario["curso"] = "Programação em Python"
print(dicionario)

print(dicionario["outro"])  # -> Aqui ocorreria uma Keyerror no dicionário comum
print(dicionario)
