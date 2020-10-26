"""
List Comprehension

Utilizando list comprehension, nós podemos gerar novas listas com dados processados a partir de outro
iterável.

Sintaxe da List Comprehension:

[dado for dado in iterável]

Exemplos:

numeros = [1, 2, 3, 4, 5]

# definição: para cada numero na lista de numeros, multiplica tal numero por 10
res = [numero * 10 for numero in numeros]

print(res)


# definindo uma função
def funcao(valor):
    return valor * valor


# adicionando a função ao comprehension
res = [funcao(numero) for numero in numeros]
print(res)

List Comprehension vs Loop:

# loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    resultado = numero * 2
    numeros_dobrados.append(resultado)

print(numeros_dobrados)

# List Comprehension:

valores_dobrados = [numero * 2 for numero in numeros]
print(valores_dobrados)

"""

# Outros exemplos:

nome = 'Higor Henrique da Silva'
letra_maiuscula = [letra.upper() for letra in nome]
print(letra_maiuscula)

# Exemplo 2:

amigos = ['maria', 'julia', 'pedro', 'guilherme']
primeira_letra_maiuscula = [amigo.title() for amigo in amigos]
print(primeira_letra_maiuscula)

# Exemplo 3:

numero_ao_cubo = [numero * 3 for numero in range(0, 11)]
print(numero_ao_cubo)

# Exemplo 4:

true_or_false = [bool(valor) for valor in [0, [], (), 1, True, 3.14]]
print(true_or_false)

# Exemplo 5:

converte_str = [str(numero) for numero in [0, 1, 2, 3, 4, 5]]
print(converte_str)


