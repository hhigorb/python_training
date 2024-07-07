"""
O desempacotamento em Python é uma técnica que permite atribuir valores de uma coleção (como uma lista ou tupla) a várias variáveis de uma vez.
Essa técnica é particularmente útil quando você deseja extrair valores de uma sequência de forma rápida e legível.
"""

# Considere uma tupla com três elementos:

valores = (1, 2, 3)

# Você pode desempacotar esses valores em três variáveis diferentes:

a, b, c = valores
print(a)  # Saída: 1
print(b)  # Saída: 2
print(c)  # Saída: 3

"""
Utilizando o _ (Underscore) no Desempacotamento
O underscore _ é frequentemente usado em Python como uma convenção para indicar que você está intencionalmente ignorando um valor específico.
Isso é útil quando você está desempacotando uma sequência, mas não precisa de todos os valores.
"""

# Por exemplo, se você tiver uma tupla com três elementos, mas só estiver interessado nos dois primeiros:

valores = (1, 2, 3)
a, b, _ = valores
print(a)  # Saída: 1
print(b)  # Saída: 2

# Neste caso, o terceiro valor é desempacotado para _, mas não é utilizado em nenhuma operação subsequente.

"""
O desempacotamento em Python é uma maneira poderosa e legível de extrair múltiplos valores de uma sequência. O uso do underscore _ é
uma prática comum para indicar valores que devem ser ignorados, tornando o código mais limpo e fácil de entender.
"""
