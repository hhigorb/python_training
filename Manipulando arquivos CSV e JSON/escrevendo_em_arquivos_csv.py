"""
Escrevendo em arquivos CSV

writer() -> Gera um objeto para que possamos escrever em arquivos CSV. Utilizamos o método writerow() para escrever
cada linha. Este método recebe uma linha.

from csv import writer

with open('filmes.csv', 'w', encoding='utf8') as file:
    escritor_csv = writer(file)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Qual o nome do filme? ')
        if filme != 'sair':
            genero = input('Digite o gênero: ')
            duracao = input('Digite a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])



"""

# DictWriter:

# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.

from csv import DictWriter

with open('filmes2.csv', mode='w', encoding='utf8') as file:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(file, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Qual o nome do filme? ')
        if filme != 'sair':
            genero = input('Digite o gênero: ')
            duracao = input('Digite a duração (em minutos): ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})