"""
Reversed

OBS: Não confunda com a função reverse() que estudamos em listas.

A função reverse() funciona apenas em listas, já a reversed() funciona com qualquer
iterável.

Sua função é inverter o iterável

A função reversed retorna um iterável chamado List Reverse Iterator.

"""

# Exemplos:

lista = [1, 2, 3, 4, 5]
invertido = reversed(lista)
print(invertido)
print(type(invertido))

# Podemos converter o elemento revertido para uma lista, tupla ou conjunto

# lista
print(list(reversed(lista)))

# tupla
print(tuple(reversed(lista)))

# set
print(set(reversed(lista)))  # -> lembrando que o set não define a ordem

# iterar sobre o reversed:

for letra in reversed('Higor Henrique'):
    print(letra, end='\n')

# É possível utilizar o reversed() para fazer um loop for reverso

for valor in reversed(range(11)):
    print(valor)