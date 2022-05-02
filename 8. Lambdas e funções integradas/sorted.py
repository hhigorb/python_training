"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort(), já estudada. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted SEMPRE retorna uma lista com os elementos do iterável ordenados

# Exemplo:

numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior
print(numeros)  # -> Caso seja impresso novamente, o valor voltará a ser o original

# Adicionando parâmetros ao sorted()

numeros = [6, 1, 8, 2]
print(numeros)  # Lista original
print(sorted(numeros))  # utilizando o sorted
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor (inverte)

# Podemos utilizar o sorted() para coisas mais complexas

pedidos = {
    'cappuccino': 54,
    'latte': 56,
    'expresso': 72,
    'americano': 48,
    'cortado': 41
}

pedidos_ordenados = sorted(pedidos.items(), key=lambda x: x[1], reverse=True)

for pedido in pedidos_ordenados:
    print(pedido[0], pedido[1])
"""

# Outro exemplo:

musicas = [
    {"titulo": "Highest in the room", "tocou": 3},
    {"titulo": "Franchise", "tocou": 5},
    {"titulo": "HOT", "tocou": 7},
    {"titulo": "Thriller", "tocou": 10},
    {"titulo": "Jeffrey", "tocou": 15},

]


mais_tocadas = sorted(musicas, key=lambda musica: musica['tocou'], reverse=True)

print('MÚSICAS MAIS TOCADAS DA RÁDIO 2020:')
print()

for musicas in mais_tocadas:
    print(musicas)

print('=' * 50)

# Votação para saber o doce favorito de um certo grupo de pessoas:

# votos
doces = {
    "jujuba": 33,
    "bolo": 55,
    "chocolate": 95,
    "bala": 101,
    "torta de limão": 100000
}

mais_votados = sorted(doces.items(), key=lambda doce: doce[1], reverse=True)

for cada_doce in mais_votados:
    print(cada_doce[0], cada_doce[1])

