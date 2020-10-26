"""
Trabalhando com módulos built-in (módulos integrados, que já vem instalados no Python)

# Utilizando aslias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

# Apelidos para funções:

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())

"""

# É recomendado utilizar tuplas para colocar múltiplos import de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice,
    uniform,
)

print(random())

print(randint(3, 7))

lista = ['Higor', 'Henrique', 'da', 'Silva']
shuffle(lista)
print(lista)

print(choice('Higor Henrique'))

print(uniform(3, 10))
