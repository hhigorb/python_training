"""
Tipo Float

Tipo real, decimal -> casas decimais

OBS: O separador das casas decimais na programação é ponto, não vírgula.
"""

valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição

valor1, valor2 = 1.44, 2.44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# É possível converter um float para um int, mas se perde a precisão

resultado = int(valor)
print(resultado)
print(type(resultado))

# É possível trabalhar com números complexos

variavel = 5j
