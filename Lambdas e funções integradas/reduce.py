"""
Reduce

OBS: A partir do Python3+ a função reduce não é mais uma função integrada (built-in) - Agora temos que
importar e utilizar esta função a partir do módulo 'functools'

Reduce basicamente é uma função que recebe dois parâmetros, uma função e um iterável. A função precisa ter
2 parâmetros. O reduce realiza a função para os 2 primeiros iteráveis e segue aplicando para o restante.

Exemplo:

Somar valores com reduce:

a1 + a2 + a3 + a4 + a5 + a6
Primeiro é somado a1 + a2 e o resultado disso é somado a a3 e assim adiante


"""

# Utilizando o reduce()

from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 8, 9, 23, 43, 23, 42]
multiplicacao = reduce(lambda x, y: x * y, dados)
print(multiplicacao)

# Comparando com um laço for:

controle = 1

for valor in dados:
    controle = controle * valor
print(controle)

