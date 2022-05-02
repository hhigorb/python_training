"""
Entendendo Iterators e Iterables

Iterator:
    - É um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterable:
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.


"""

nome = 'Higor'  # é um iterable, mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # é um iterable, mas não é um iterator

iterable1 = iter(nome)
iterable2 = iter(numeros)

print(next(iterable1))
print(next(iterable1))
print(next(iterable1))
print(next(iterable1))
print(next(iterable1))

print(next(iterable2))
print(next(iterable2))
print(next(iterable2))
print(next(iterable2))
print(next(iterable2))
print(next(iterable2))




