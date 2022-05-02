"""
Funções com retorno

Em Python, quando uma função não retorna nenhum valor, o retorno é None.

OBS: Funções Python que retornam valores devem retornar estes valores com a palavra
reservada return

Refatorando a primeira função:

def diz_oi():
    return 'Oi'


print(diz_oi())

OBS: Sobre a palavra reservada return:

1 - Ela finaliza a função, ou seja, ela sai da execução da função
2 - Podemos ter, em uma função, diferentes returns
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

Exemplo 1: Ela finaliza a função, ou seja, ela sai da execução da função


def diz_oi():
    print('Estou sendo executado antes do retorno')
    return 'Oi'
    print('Estou sendo executado após o retorno')

print(diz_oi())

Exemplo 2: Podemos ter, em uma função, diferentes returns

def nova_funcao():
    variavel = 0
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

Exemplo 3: Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

def outra_funcao():
    return (2, 3, 4, 5)


num1, num2, num3, num4 = outra_funcao() -> Aqui está desempacotando a tupla
print(num1, num2, num3, num4)

Vamos criar uma função para jogar a moeda

from random import randint


def joga_moeda():
    if randint(0, 1) == 1:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

Erros comuns na utilização do retorno, mas são apenas codificações desnecessárias:

def e_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    else: -> Evitar colocar o else, já que se a condição for false, irá sempre cair no próximo return
        return False

print(e_impar())

Forma correta:

def e_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False
"""


