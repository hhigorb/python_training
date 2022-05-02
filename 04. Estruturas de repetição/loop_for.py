"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:

- String
    nome = 'Higor Henrique'
- Lista
    lista = [0, 1, 2, 3, 4, 5]
- Range
    numeros = range(1, 10)

Quando não precisamos de um valor, podemos descarta-lo utilizando o underline:

for _, letra in enumerate(nome):
    print(letra)
"""

nome = 'Higor Henrique'
lista = [0, 2, 3, 4, 5, 6]
numeros = range(1, 10)

# Iterando em uma string
for letra in nome:
    print(letra)

print('_' * 50)

# Iterando em uma lista
for numero in lista:
    print(numero)

print('_' * 50)

# Iterando em um range
"""
OBS: No range o valor final não é incluído. Ou seja, de range 0 a 10, será de 0 a 9
"""
for numero in range(0, 10):
    print(numero)

print('_' * 50)

# Enumerate gera um índice para cada iterável
for i, v in enumerate(nome):
    print(v)

print('_' * 50)

# Exemplo de for:

qtd = int(input('Informe quantas vezes o loop deve rodar: '))
soma = 0

for i in range(1, qtd + 1):
    valor = int(input(f'Informe o valor {i}/{qtd}: '))
    soma = soma + valor
print(soma)
