"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização, nós passamos apenas um parâmetro de entrada, que neste
caso é o caminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é ele que trabalhamos então.

Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então
teremo o erro FileNotFoundError

arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))

reultado -> <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

io.TextIOWrapper -> tipo do dado
name='texto.txt' -> nome do arquivo que foi aberto
mode='r' -> modo de leitura, no caso r de read()
encoding='cp1252' -> tipo de caracteres, encoding

"""

arquivo = open('texto.txt')

# para ler o conteúdo de um arquivo após sua abertura, devemos utilizar a função read()
print(arquivo.read(20))  # -> É possível passar um parâmetro para limitar a quantidade de caracteres a serem lidos

# OBS: O arquivo é lido do início até o fim, de cima para baixo e começando da esquerda para a direita. Exatamente como
# linhas de código

# A função read() retorna o arquivo que foi aberto em formato string.


