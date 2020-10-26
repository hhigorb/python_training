"""
Funções de maior grandeza -> Higher Order Functions

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções
como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis
do tipo de funções nos nossos programas.

# Exemplo -> Definindo as funções


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# testando as funções:


print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nested Functions -> Funções aninhadas

# Em Python, podemos também ter funções dentro de funções, que são conhecidas por Nested Functions, ou também
# Inner Functions (funções internas)

# Exemplo:

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(['Opa', 'Eai?', 'Tudo bem?'])
    return humor() + pessoa


print(cumprimento('higor'))

# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(['hahahaha', 'kkkkkk', 'yayayaya'])
    return rir


print(faz_me_rir())


"""

# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(['hahaha', 'kkk', 'yayaya'])
        return f'{risada} {pessoa}'
    return dando_risada()


print(faz_me_rir_novamente('higor'))






