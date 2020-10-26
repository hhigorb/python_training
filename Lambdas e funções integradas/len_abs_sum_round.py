"""
Len, Abs, Sum e Round

Len:
len() -> Retorna o tamanho, ou seja, o número de itens de um iterável.

# Exemplos len()

print(len('Higor Henrique'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}))
print(len(range(11)))

Abs:
abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria seu valor real sem o sinal

# Exemplos abs()

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

Sum:
sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a ssoma total dos elementos,
incluindo o valor inicial

OBS: O valor inicial default é 0.

# Exemplos sum()

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))  # -> utilizando valor inicial 5, a soma irá se iniciar com 5

Round:
round() -> Retorna um número arredondado para n dígito de precisão após a casa decimal. Se a
precisão não for informada, retorna o inteiro mais próximo da entrada

# Exemplo round()

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.212121211, 2))
print(round(1.21999999, 2))
"""

# Exemplo round()

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.212121211, 2))
print(round(1.21999999, 2))




