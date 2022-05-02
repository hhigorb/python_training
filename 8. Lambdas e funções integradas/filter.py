"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# biblioteca para trabalhar com dados estatísticos
import statistics

# dados coletadoss de algum sensor:
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), filter() recebe 2 parâmetros, sendo uma função e um iterável.

retorno = filter(lambda x: x > media, dados)
print(list(retorno))

# filtrando dados não preenchidos em uma lista:
paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Colômbia', '', 'Equador', '', '', 'Venezuela']
retorno = filter(None, paises)
print(list(retorno))

# outra forma:
paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Colômbia', '', 'Equador', '', '', 'Venezuela']
retorno = filter(lambda pais: len(pais) > 0, paises)
print(list(retorno))


"""

# Exemplo mais complexo:

users = [
    {"username": "samuel", "tweets": ['Eu gosto de bolo', 'Eu gosto de sorvete']},
    {"username": "larissa", "tweets": ['Eu amo meu gato']},
    {"username": "jeff", "tweets": []},
    {"username": "higor", "tweets": ['Eu gosto de cachorro', 'Vou sair hoje']},
    {"username": "gall", "tweets": []},
]

# Filtrar os usuários que estão inativos no Twitter

usuarios_inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, users))
print(usuarios_inativos)

# outra forma:
usuarios_inativos = list(filter(lambda usuario: not usuario["tweets"], users))
print(usuarios_inativos)

# Combinar filter() e map():

nomes = ['Vanessa', 'Ana', 'Maria']

# devemos criar uma lista contendo 'sua instrutora é:' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

# filtrando pessoas que possuem crédito superior a 1000 reais

conta_bancaria = [
    {"nome": "higor", "credito": 1500}, {"nome": "carlos", "credito": 7000}, {"nome": "marta", "credito": 2500},
    {"nome": "jose", "credito": 10000}, {"nome": "marcos", "credito": 700}, {"nome": "maria", "credito": 200},
]

valores_acima_de_1000 = list(filter(lambda valor: valor["credito"] > 1000, conta_bancaria))
print(valores_acima_de_1000)



















