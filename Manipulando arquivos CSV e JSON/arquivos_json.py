"""
Arquivos JSON

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube...) e terceiros
(nós desenvolvedores).

Arquivos JSON nada mais é que um formato de arquivo para manter e trocar informações legíveis pelas pessoas. O arquivo
contém apenas texto e usa a extensão .json.

Simplificando, um arquivo JSON nada mais é que um dicionário de chaves:valores
"""

import json

# Transformando um arquivo Python em JSON:

# um objeto Python (dicionário)
x = {
    "nome": 'Higor',
    "idade": 20,
    "cidade": 'Americana',
}

# convertendo para um arquivo JSON:

y = json.dumps(x)

# O resultado é uma string:
print(y)
print(type(y))


# Transformando um arquivo JSON em Python:


# arquivo json:
x = '{ "nome":"Higor", "idade":20, "cidade":"Americana"}'

y = json.loads(x)

# o resultado é um dicionário python:

print(y['idade'])
