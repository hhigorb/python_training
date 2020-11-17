"""
Lendo arquivos CSV

CSV - Comma Separeted Values -> Valores Separados por Vírgula

O Python possui 2 formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas
    - DictReader -> Permite que iteremoss sobre as linhas do arquivo CSV como OrderedDict


# Reader:

from csv import reader

with open('lutadores.csv', encoding='utf8') as file:
    leitor_csv = reader(file)  # a função reader devolve um iterator
    next(leitor_csv)  # pula o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]}cm')


"""

# DictReader:

from csv import DictReader

with open('lutadores.csv', encoding='utf8') as file:
    leitor_csv = DictReader(file, delimiter=',')  # -> Defininido o separador, no caso a vírgula.
    for linha in leitor_csv:
        # Cada linha é um Ordered Dict
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']}cm")






