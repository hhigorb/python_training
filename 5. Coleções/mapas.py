"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}

idades = {
    "Higor": 20,
    "Larissa": 19,
}

# Iterar sobre dicionários:

for chave in idades:
    print(chave)

for chave in idades:
    print(idades[chave])

for chave in idades:
    print(f'{chave} tem {idades[chave]} anos')

# Acessando as chaves:

print(idades.keys())

for chave in idades.keys():
    print(idades[chave])

# Acessando os valores:

print(idades.values())

for idade in idades.values():
    print(idade)

Desempacotamento de dicionários:

for chave, valor in idades.items():
    print(f'Seu nome é {chave} e você tem {valor} anos')

Soma, valor máximo, valor mínimo, tamanho:

print(sum(idades.values()))
print(min(idades.values()))
print(max(idades.values()))
print(len(idades))

"""

