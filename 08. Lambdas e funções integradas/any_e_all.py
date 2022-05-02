"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

# Exemplo (all):

# É possível utilizar com qualquer iterável: listas, tuplas, strings, etc.
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True
print(all([]))  # Retorna True se o iterável estiver vazio

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all(nome[0] == 'C' for nome in nomes))

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

print(any([0, 1, 2, 3, 4, 5]))  # retorna True
print(any([0, False, [], {}, None]))  # retorna False
"""


