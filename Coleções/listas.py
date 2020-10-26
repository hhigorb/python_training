"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamanho fixo, ou seja, não é necessário definir um tamanho para a lista, é limitado à memória
disponível

- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

Listas em Python são representadas por colchetes -> []
Além disso, listas são mutáveis, ou seja, podem mudar constantemente.

lista1 = [99, 53, 2, 34, 1, 33, 94, 55, 74]
lista2 = ['H', 'i', 'g', 'o', 'r', '', 'H', 'e', 'n', 'r', 'i', 'q', 'u', 'e']
lista3 = []
lista4 = list(range(11))
lista5 = list('Higor Henrique')

Podemos facilmente checar se determinado valor está contido na lista:

n = 7

if n in lista4:
    print(f'O número {n} está na lista!')
else:
    print(f'O número {n} não está na lista!')

Podemos facilmente ordenar uma lista:

lista1.sort()
print(lista1)

Podemos facilmente contar o número de ocorrências de um valor em uma lista:

print(lista1.count(2))
print(lista5.count('H'))

Adicionar elementos em listas (utiliza-se a função append):
OBS: Com append só é possível adicionar um elemento por vez, e o elemento é sempre adicionado
ao final da lista

lista1.append(42)
lista1.append([8, 3, 11]) -> Coloca a lista como elemento único (sublista)
lista1.extend([123, 44, 67]) -> Coloca cada elemento da lista como valor adicional à lista
OBS: O extend só aceita iteráveis, como listas, strings, etc.
Já o append aceita qualquer valor (que seja único)

Podemos inserir um novo elemento na lista informando a posição do índice
Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista

lista1.insert(0, 'Novo valor')
print(lista1)

Podemos facilmente juntar duas listas:

lista6 = lista1 + lista2

ou

lista1.extend(lista2)

É possível inverter uma lista:

lista1.reverse()
print(lista1)

ou

print(lista1[::-1])

Copiar uma lista:

lista6 = lista2.copy()
print(lista6)

Podemos contar quantos elementos possuem dentro da lista:

print(len(lista1))

Podemos remover o último elemento de uma lista:
OBS: O pop não somente remove o último elemento mas também o retorna

lista5.pop()
print(lista5)

Também é possível definir qual posição do elemento remover com o pop
OBS: Os elementos à direita deste índice serão deslocados para a esquerda

lista5.pop(2)

Podemos remover todos os elementos da lista

lista5.clear()

É possível repetir os elementos de uma lista:

nova = [1, 2, 3]
nova = nova * 3

É possível converter uma string em uma lista com o split
Por padrão, o split separa a string pelos espaços, mas é possível definir o separador

Exemplo 1:

string = 'Higor Henrique da Silva'
string = string.split('')
print(string)

Exemplo 2:

string2 = 'Higor,Henrique,da,Silva'
string2 = string.split(',')
print(string2)

Convertendo uma lista em uma string:

nome = ['Higor', 'Henrique', 'da', 'Silva']
nome = ' '.join(nome)
print(nome)

Iterando sobre listas
Exemplo 1:

soma = ''

for elemento in lista5:
    soma += elemento
print(soma)

Exemplo 2:

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

Utilizando variáveis em listas:

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

Fazendo acesso aos elementos de forma indexada:

            0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) -> verde
print(cores[1]) -> amarelo
print(cores[2]) -> azul
print(cores[3]) -> branco

Fazer acesso aos elementos de forma indexada inversa:

print(cores[-1]) -> branco
print(cores[-2]) -> azul
print(cores[-3]) -> amarelo
print(cores[-4]) -> verde

Gerar índice em um for:

for indice, cor in enumerate(cores):
    print(indice, cor)

Listas aceitam valores repetidos:

lista = []
lista.append(44)
lista.append(44)
lista.append(33)
lista.append(33)
lista.append(44)
print(lista)

Outros métodos não tão importantes mas também úteis:

1. Encontrar o índice de um elemento na lista:

numeros = [5, 1, 2, 3, 4, 5, 6, 7]
print(numeros.index(3)) -> Em qual índice está o valor '3'

OBS: Se houverem valores repetidos na lista, será retornado o primeiro elemento encontrado

print(numeros.index(5, 1) -> Buscar o índice do número 5 a partir da posição 1, ou seja, buscar outro que não seja o
primeiro
print(numeros.index(5, 4, 6) -> Buscar o índice do número 5 entre os índices 4 e 6

Slicing:

lista[inicio:fim:passo]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista[1:])  # Começar do elemento 1 e ir até o final
print(lista[::])  # Pegar todos os elementos
print(lista[-3:])  # Pegar os elementos de forma inversa (aqui vai pegar o 8, 9, 10)
print(lista[:2])  # Pegar do início até o índice 2 (o 2 não é incluído)
print(lista[1:3])  # Pegar do índice 1 até o 3 (o 3 não é incluído)
print(lista[1::2])  # Começa no índice 1, vai até o final e pula de 2 em 2
print(lista[::-1])  # Inverte a lista

Soma, valor máximo, valor mínimo, tamanho da lista:

lista = [1, 2, 3, 4, 5]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

Desempacotamento de listas:

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1, num2, num3, *_ = lista

print(num1)
print(num2)
print(num3)
print(_)

Deep Copy:

lista = [1, 2, 3, 4, 5]
nova_lista = lista.copy()
nova_lista.append(45)

print(lista)
print(nova_lista)

Copiar uma lista dessa forma não afeta a lista que foi copiada, ambas as listas possuem valores independentes

Shallow Copy:

lista = [1, 2, 3, 4, 5]
nova_lista = lista
nova_lista.append(45)

print(lista)
print(nova_lista)

Nesse caso, modificando apenas a lista copiada, o novo valor se refletiu em ambas as listas

"""


