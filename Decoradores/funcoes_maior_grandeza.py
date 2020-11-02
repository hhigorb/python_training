"""
Funções de maior grandeza - Higher Order Function - HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções
como resulto, ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar
variáveis do tipo de funções nos nossos programas.


# Exemplo - Definindo as funções:


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(n1, n2, funcao):
    return funcao(n1, n2)


# testando as funções:

print(calcular(10, 2, somar))
print(calcular(10, 2, diminuir))
print(calcular(10, 2, multiplicar))
print(calcular(10, 2, dividir))

# Nested Functions - Funções Aninhadas:

# Em Python, podemos também ter funções dentro de funções, que são conhecidas por Nested Functions, ou também
# Inner Functions (funções internas).


# Exemplo:

from random import choice


def cumprimento(nome):
    def humor():
        return choice(['Eai ', 'Como vai? ', 'Tudo beleza? '])
    return humor() + nome


# testando a função:

print(cumprimento('Higor'))


# Retornando funções de outras funções:

from random import choice


def faz_me_rir():
    def rir():
        return choice(['hahahaha', 'kkkkkkk', 'asuhasuashuas'])
    return rir


rindo = faz_me_rir()
print(rindo())


# Nested Functions podem acessar o escopo de funções externas, ou funções mais externas.


from random import choice


def faz_me_rir_novamente(nome):
    def dando_risada():
        risada = choice(['hahahaha', 'kkkkkkkk', 'ashsuasushasu'])
        return f'{risada} {nome}'
    return dando_risada


# testando:

risada = faz_me_rir_novamente('Higor')
print(risada())
print(risada())
print(risada())
"""



