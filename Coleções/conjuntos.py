"""
Conjuntos

Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
da matemática.

No Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a
ordenação deles. Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python por chaves {}.

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:

    - Um dicionário tem chave/valor
    - Um conjunto tem apenas valor

Definindo um conjunto:

conjunto = {1, 2, 3, 4, 5, 6, 7, 7, 7}  -> Repare que temos valores repetidos
print(conjunto)
print(type(conjunto))

OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem
gerar erros e não fará parte do conjunto.

Podemos verificar se determinado elemento está contido no conjunto:

if 3 in conjunto:
    print('Tem o 3')
else:
    print('Não tem o 3')

Importante lembrar que, além de não termos valores duplicados, não temos ordem:

Listas aceitam valores duplicados, então temos 10 elementos:
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

Tuplas aceitam valores duplicados, então temos 10 elementos:
tupla = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Tupla: {tupla} com {len(tupla)} elementos')

Dicionários não aceitam chaves duplicados, então temos 8 elementos:
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

Conjuntos não aceitam valores duplicados, então temos 8 elementos:
conjunto = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

Assim como as outras coleções Python, podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 32.22, 44}
print(s)
print(type(s))

Podemos interar em um set normalmente:

for valor in s:
    print(valor)

Usos interessantes com sets:

Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
informam manualmente a cidade de onde vieram.

Nós adicionamos cada cidade em uma lista Python, já que em uma lista, podemos adicionar novos elementos
e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande' ]

print(cidades)
print(len(cidades))

Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

Podemos utilizar o set para isso:

print(len(set(cidades)))

OBS: Vale ressaltar que, em conjuntos não existe ordem, a ordem do conjunto é gerado automaticamente.

Adicionando elementos em um conjunto:

s = {1, 2, 3}
s.add(4) -> Duplicidade não gera erro, simplesmente é ignorado e não é adicionado
print(s)

Remover elementos em um conjunto:

Forma 1:

s = {1, 2, 3}
print(s)
s.remove(3)
print(s)

Forma 2:

s.discard(2)
print(s)


Copiando um conjunto para outro:

s = {1, 2, 3, 4, 5}

Forma 1: Deep Copy (é criado elementos independentes)

novo = s.copy()
print(novo)

novo.add(6)
print(novo)

Forma 2: Shallow Copy (alterar o elemento copiado também altera o elemento original)

novo = s
novo.add(6)
print(novo)
print(s)

Podemos remover todos os itens de um conjunto:

s.clear()
print(s)

Métodos matemáticos de Conjuntos:

Imagine que temos dois conjuntos, um contendo estudantes do curso Python e um
contendo estudantes do curso Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

Veja que alguns alunos que estudam Python também estudam Java.

Precisamos gerar um conjunto com nomes de estudantes únicos.

Forma 1: Utilizando union

unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

Forma 2: Utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

Gerar um conjunto de estudantes que estão em ambos os cursos:

Forma 1: Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

Forma 2: Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

Gerar um conjunto de estudantes que não estão no outro curso:

cursa_python = estudantes_python.difference(estudantes_java)
print(cursa_python)

cursa_java = estudantes_java.difference(estudantes_python)
print(cursa_java)

Soma, valor máximo, valor mínimo, tamanho:

s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""

