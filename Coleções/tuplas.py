"""
Tuplas

Tuplas são bastante parecidas com listas. Existem duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis, isso significa que ao se criar uma tupla, ela não muda.
Toda operação em uma tupla gera uma nova tupla.

Cuidado 1: As tuplas são representadas por (), mas veja:
Mesmo sem parênteses, o Python considera uma variável com vários valores uma tupla.

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

Cuidado 2: Tuplas com 1 elemento:

tupla3 = (4) -> Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,) -> Isso é uma tupla!
print(tupla4)
print(type(tupla4))

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula, e não pelo uso do parênteses

Podemos gerar uma tupla dinamicamente com o range:

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

Desempacotamento com tupla:

tupla = ('Higor Henrique', 'da Silva')
nome, sobrenome = tupla

print(nome)
print(sobrenome)

OBSERVAÇÃO: Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis

Soma, valor máximo, valor mínimo e tamanho (se os valores forem todos inteiros ou reais, exceto pelo len):

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(sum(tupla))
print(min(tupla))
print(max(tupla))
print(len(tupla))

Concetenação de tuplas:

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) -> Tuplas são imutáveis, mas é possível concatena-las

tupla1 = tupla1 + tupla2 -> Tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)

Verificar se determinado elemento está contido na tupla:

tupla = (1, 2, 3)

print(3 in tupla)

Iterando sobre uma tupla:

tupla = (1, 2, 3)

for numero in tupla:
    print(numero)

for indice, valor in enumerate(tupla):
    print(indice, valor)

Contando elementos dentro de uma tupla:

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

nome = tuple('Higor Henrique')
print(nome)
print(nome.count('H'))

Dicas na utilização de tuplas:

Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

Exemplo 1:

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

Como não existem outros meses, não tem um motivo para essa tupla ser alterada

O acesso a elementos de uma tupla também é semelhante a de uma lista:

print(meses[5])

Iterar com while:

i = 0

while i < len(meses):
    print(meses[i])
    i += 1

Verificando em qual índice um elemento está na tupla:

print(meses.index('Julho'))

Slicing: Exatamente como ocorre nas listas

tupla[inicio:fim:passo]

print(meses[0:])  # -> Início até o final
print(meses[5:])  # -> Começa no 5 e vai até o final
print(meses[::-1])  # -> Imprime a tupla ao contrário
print(meses[2:8:2])  # -> Vai do índice 2 ao 7 (o último nunca é incluído) pulando de 2 em 2

Copiando uma tupla para outra:
Na tupla não temos o problema do Shallow Copy

tupla = (1, 2, 3)
nova = tupla
outra = (4, 5, 6)
nova = nova + outra

print(nova)
print(tupla)

"""






