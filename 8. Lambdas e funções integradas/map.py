"""
Map

Com map, fazemos mapeamento de valores para função.
A função map() executa uma função específica para cada item de um iterável

Como funciona o map?

def area(r):
    return 3.14 * (r ** 2)


print(area(2))
print(area(5.3))

# Usando loop com a função area para calcular cada raio da lista 'raios'

raios = [2, 5, 7.1, 8.3, 10, 44]

areas = []
for valor in raios:
    areas.append(area(valor))

print(areas)

# Forma 2 - Map:
# Map é uma função que recebe dois parâmetros. O primeiro a função, o segundo um iterável

areas = map(area, raios)
print(list(areas))

Outro exemplo da utilização de map:


def tamanho_string(a):
    return len(a)

tamanho_cada_valor = map(tamanho_string, ['Higor', 'Henrique', 'da', 'Silva'])
print(tamanho_cada_valor)


# Utilizando map com lambdas:

lista_de_nomes = ['higor', 'carla', 'marcos', 'jose', 'pedro']
transforma_nomes = map(lambda nome: nome.upper(), lista_de_nomes)
print(list(transforma_nomes))

# OBS: Após utilizar a função map, transformando-a em uma lista por exemplo, se tentar transformar novamente,
# retornará um valor vazio.

"""

# Outro exemplo: Pegar um conjunto de cidades e suas temperaturas em Graus Celsius e transformar em graus F

temp_cidade = {
    "Nova York": 25,
    "Cairo": 22,
    "São Paulo": 34,
    "Berlim": 23,
    "Tokyo": 19,
}

temp_cidades2 = [('São Paulo', 34), ('Nova York', 25), ('Cairo', 22), ('Berlim', 23), ('Tokyo', 19)]


# Formula conversão C para F: F = 9/5 * C + 32

c_para_f = map(lambda c: 9/5 * c + 32, temp_cidade.values())
print(list(c_para_f))

# Outro exemplo:

conta_bancaria = [
    {"nome": "higor", "credito": 1500}, {"nome": "carlos", "credito": 7000}, {"nome": "marta", "credito": 2500},
    {"nome": "jose", "credito": 10000}, {"nome": "marcos", "credito": 700}, {"nome": "maria", "credito": 200},
]


valores_abaixo_de_1000 = list(map(lambda valor: valor["credito"] < 1000, conta_bancaria))
print(valores_abaixo_de_1000)














