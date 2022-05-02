"""
Modos de abertura de arquivo

r -> Abre o arquivo para leitura ou o cria, caso não exista. O cursor é posicionado no inicio do arquivo.
r+ -> Abre o arquivo para leitura e escrita ou o cria, caso não exista. O cursor é posicionado no inicio do arquivo.
w -> abre para escrita - sobrescreve caso o arquivo já exista
w+ -> Se o arquivo já existir, ele tem tamanho reduzido para zero (conteúdo do arquivo é apagado) e é
aberto para escrita e leitura. Se não existir, um novo arquivo é criado.
x -> abre para escrita somente se o arquivo não existir
a -> abre para escrita adicionando o conteúdo ao final do arquivo
a+ -> Abre o arquivo para leitura e escrita. Caso não exista, ele é criado e o cursor é posicionado no final do arquivo

# abrindo no modo 'a' -> append, se o arquivo não existir, será criado. Caso exista, o próximo conteúdo
será adicionado sempre ao final.

# exemplo com x
try:
    with open('higor.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo')
except FileExistsError:
    print('Arquivo já existe.')

# exemplo com a

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')

        else:
            break
"""

with open('outro.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.write('teste\n')
