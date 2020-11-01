"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista, fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)

Se quisermos criar um set (conjunto):

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

Sintaxe do Dictionary Comprehension:

{chave: valor for valor in iteravel}

# Exemplos:

Exemplo 1:

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)


Exemplo 2:

numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)


Exemplo 3:

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)


"""

# Exemplo com lógica condicional:

impar_par = {num: ('par' if num % 2 == 0 else 'impar') for num in range(0, 100)}
print(impar_par)




