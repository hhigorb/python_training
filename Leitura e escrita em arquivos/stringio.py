"""
StringIO

Atenção: Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão:
    - Permissão de leitura -> para ler o arquivo
    - Permissão de escrita -> para escrever o arquivo

StringIO -> utilizado para ler e criar arquivos em memória, sem necessidade de criar o arquivo txt

Semelhante a utilizar:

with open('arquivo.txt') as arquivo:

Porém não irá criar um arquivo, tudo será manipulado na própria memória, sendo manipulado pelas strings.

"""

# primeiro fazemos o import
from io import StringIO

mensagem = 'Essa é uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)

# Agora que temos o arquivo, podemos utilizar todos os métodos de leitura e escrita de arquivos:
print(arquivo.read())

# escrevendo outros textos:
arquivo.write(' outro texto')

# podemos inclusive movimentar o cursor:
arquivo.seek(0)

print(arquivo.read())