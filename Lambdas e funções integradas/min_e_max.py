"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {"a": 1, "b": 8, "c": 4, "d": 99, "e": 34, "f": 129}
print(max(dicionario.values()))

# Faça um programa que receba dois valores e retorne o maior

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))

print(max(v1, v2))

# com strings:

print(max('a', 'ab', 'abc'))
print(max('Higor Henrique'))  # letra alfabética maior

min() -> Retorna o menor em um iterável ou menor de dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

dicionario = {"a": 1, "b": 8, "c": 4, "d": 99, "e": 34, "f": 129}
print(min(dicionario.values()))

# Faça um programa que receba dois valores e retorne o menor

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))

print(min(v1, v2))

# com strings:

print(min('a', 'ab', 'abc'))
print(min('Higor Henrique'))  # letra alfabética menor (aqui foi o espaço)

# Outros exemplos:

nomes = ['Arya', 'Samsom', 'Dora', 'Tim', 'Ollivander']  # aqui está levando em consideração a 1 letra alfabética
print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim


"""

# Música mais tocada e menos tocada:

musicas = [
    {"titulo": "Highest in the room", "tocou": 3},
    {"titulo": "Franchise", "tocou": 5},
    {"titulo": "HOT", "tocou": 7},
    {"titulo": "Thriller", "tocou": 10},
    {"titulo": "Jeffrey", "tocou": 15},

]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

