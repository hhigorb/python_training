"""
Módulo Collections - Counter

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance Container Datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento

Utilizando o Counter:

from collections import Counter

# É possível utilizar qualquer tipo de iterável, aqui é utilizado uma lista:
lista = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]

print(Counter(lista))

Exemplo 2:

string = 'Higor Henrique'
print(Counter(string))

Most common é utilizado para verificar quais são os itens que mais aparecem no iterável.

texto = "It is a long established fact that a reader will be distracted by the readable content of a page when' \
        ' looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution' \
        ' of letters, as opposed to using 'Content here, content here', making it look like readable English. Many" \
        " desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and" \
        " a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have" \
        " evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."

print(Counter(texto).most_common())

nomes = ['Higor', 'Higor', 'Higor', 'Valéria', 'Claudia', 'Regina', 'Fátima', 'Valéria', 'Regina']

print(Counter(nomes).most_common(2)) # -> Pega as 2 mais comuns
"""







