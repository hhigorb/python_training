"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares

# Exemplos:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

print(list(zip1))

#  É possível gerar uma lista, tupla ou dicionário com o zip:

# tupla
zip1 = zip(lista1, lista2)
print(tuple(zip1))

# set
zip1 = zip(lista1, lista2)
print(set(zip1))

# dict
zip1 = zip(lista1, lista2)
print(dict(zip1))

# vale ressaltar que após utilizar o objeto, ele é apagado da memória

lista3 = [7, 8, 9, 10, 11]
print(list(zip(lista1, lista2, lista3)))  # -> Acabou no 9, já que as primeiras listas não tinham mais elementos

# OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhando
# com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabarem.

# Podemos utilizar diferentes iteráveis com zip()

tupla = (1, 2, 3, 4, 5)
lista = [6, 7, 8, 9, 10]
dicionario = {"a": 11, "b": 12, "c": 13, "d": 14, "e": 15}
conjunto = {16, 17, 18, 19, 20}

iteraveis = zip(tupla, lista, dicionario, conjunto)
print(list(iteraveis))

# lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))


"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

nota_final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(nota_final)