"""
Entendendo o *args

O *args é um parâmetro como qualquer outro. Isso significa que você poderá chamar
de qualquer coisa, desde que comece com asterisco

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função coloca os valores extras informadas como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

Entendendo o args:


def soma_todos_numeros(*args):
    total = 0
    for valor in args:
        total += valor
    return total


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(3, 2))
print(soma_todos_numeros(3, 2, 6))
print(soma_todos_numeros(3, 2, 6, 8))

Outro exemplo:


def verifica_info(*args):
    if 'Higor' in args and 'Henrique' in args:
        return 'Bem-vindo, Higor!'
    return 'Opss, pessoa errada!'


print(verifica_info(1, 2, 3))
print(verifica_info(True, '123', 'Maria'))
print(verifica_info('Higor', 'Henrique'))

Outro exemplo:


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6, 7))

Desempacotador:

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 9]
print(soma_todos_numeros(*lista_de_numeros))

OBS: O asterisco serve para informemos ao Python que estamos
passando como argumento uma coleção de dados, dessa forma ele saberá que
precisará antes desempacotar os dados

"""

