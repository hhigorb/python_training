"""
Módulo Collections - Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

Em um dicionário, a ordem de inserção dos elementos não é garantida.

dicionario = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,

}

for chave, valor in dicionario.items():
    print(chave, valor)

OrderedDict -> É um dicionário que nos garante a ordem de inserção dos elementos.

Fazendo import:

from collections import OrderedDict

dicionario = OrderedDict({
    "v1": 1,
    "v2": 2,
    "v3": 3,
    "v4": 4,
    "v5": 5,
    "v6": 6,
})

for chave, valor in dicionario.items():
    print(chave, valor)

Entendendo a diferença entre Dict e Ordered Dict:

from collections import OrderedDict

Dicionários comuns:

dict1 = {
    "a": 1,
    "b": 2,
}

dict2 = {
    "b": 2,
    "a": 1,
}

print(dict1 == dict2) -> True, pois a ordem dos elementos não importa para o dicionário

Ordered Dict:

odict1 = OrderedDict({
    "a": 1,
    "b": 2,
})

odict2 = OrderedDict({
    "b": 2,
    "a": 1,
})

print(odict1 == odict2) -> False, já que a ordem dos elementos importa para o Ordered Dict
"""

