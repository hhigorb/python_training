"""
Set Comprehension

"""

# Exemplos:

numeros = {num for num in range(0, 7)}
print(numeros)

# outro exemplo:

numeros = {x ** 2 for x in range(10)}
print(numeros)

# transformando o exemplo acima em um dicionário:

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# mais um exemplo:

letras = {letra for letra in 'Higor Henrique'}
print(letras)