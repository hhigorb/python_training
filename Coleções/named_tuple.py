"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

Recapitulando tuplas:

tupla = (1, 2, 3)
print(tupla[0])

Named Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros

"""

# Realizando o import:

from collections import namedtuple

# Precisamos definir o nome e parâmetros:

# Forma 1: Declaração named tuple

cachorro = namedtuple('cachorro', 'idade raca nome ')

# Forma 2: Declaração named tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3: Declaração named tuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Utilizando a named tuple:

pitbull = cachorro(idade=2, nome='Belo', raça='Pitbull')
print(pitbull)

print(pitbull.idade)
print(pitbull.nome)
print(pitbull.raça)


