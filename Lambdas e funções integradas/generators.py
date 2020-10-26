"""
Generator Expression

Em aulas anteriores nós estudamos:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension

Não vimos:
- Tuple Comprehension... porque elas se chamam Generators

nomes = ['Carla', 'Camila', 'Cassiano', 'Cristiane', 'Cristiano', 'Vanessa']

# List comprehension
retorno = [nome[0] == 'C' for nome in nomes]
print(type(retorno))

# Generator
retorno2 = (nome[0] == 'C' for nome in nomes)
print(type(retorno2))

"""

from sys import getsizeof


# comparando performace entre comprehensions e generator

# gerando uma lista de números com list comprehension
list_comprehension = getsizeof([x * 10 for x in range(1000)])

# gerando uma lista de números com set comprehension
set_comprehension = getsizeof({x * 10 for x in range(1000)})

# gerando uma lista de números com dictionary comprehension
dict_comprehension = getsizeof({x: x * 10 for x in range(1000)})

# gerando uma lista de números com Generator
generator = getsizeof((x * 10 for x in range(10000)))

print('Para fazer a mesma tarefa, gastamos em memória: ')
print(f'List Comprehension: {list_comprehension} bytes')
print(f'Set Comprehension: {set_comprehension} bytes')
print(f'Dictionary Comprehension: {dict_comprehension} bytes')
print(f'Generator: {generator} bytes')

# Iterando em generators:

outro_generator = (numero * 10 for numero in range(10))

for numero in outro_generator:
    print(numero)

