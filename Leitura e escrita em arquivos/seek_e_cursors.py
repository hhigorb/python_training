"""
Seek e Cursors

seek() -> Utiliza para movimentar o cursor pelo arquivo

arquivo = open('texto.txt')
print(arquivo.read())

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe
# um parâmetro que indica onde queremos colocar o cursor.
# Movimentando o cursor pelo arquivo com a função seek():

arquivo.seek(20)
print(arquivo.read())

# Já que a função read() transforma o arquivo em string, podemos buscar com o seek() onde queremos começar
simplesmente com o mesmo método e fatiamento de strings

# Utilizando a função readLine() -> função que lê o arquivo linha a linha

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

# função readlines() -> coloca cada linha como cada item de uma lista

print(arquivo.readlines())

OBS: Quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo no
disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os
trabalhos com o arquivo devemos fechar essa conexão. Para isso, utilizamos a função close().

Passos para trabalhar com um arquivo:

1 - Abrir o arquivo,
2 - Trabalhar o arquivo,
3 - Fechar o arquivo.
"""

# abrir o arquivo
arquivo = open('texto.txt')

# trabalhando com o arquivo
print(arquivo.read())

# fechar o arquivo
arquivo.close()

print(arquivo.closed)  # -> verifica se o arquivo está fechado ou aberto


