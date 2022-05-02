"""
**kwargs

Também podemos chamar este parâmetro de qualquer nome, mas por convenção é utilizado kwargs

Este é só mais um parâmetro, mas diferente de *args que coloca valores extra em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário

Exemplo:


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', vanessa='branco')

OBS: Os parâmetros *args e **kwargs não são obrigatórios

Nas nossas funções podemos ter (NESTA ORDEM):
    Parâmetros obrigatórios,
    *args,
    Parâmetros default (não obrigatórios),
    **kwargs

É essencial seguir essa ordem de parâmetros para não haver erros no código.

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(**kwargs)


print(minha_funcao(8, 'Higor'))
print(minha_funcao(8, 'Higor', 4, 5, 6, solteiro=True))
print(minha_funcao(8, 'Higor', 4, 5, 6, dicionario='sim'))

Desempacotar com **kwargs:


def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {
    "nome": "Higor",
    "sobrenome": 'Henrique',
}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario) # -> Em dicionário se utiliza duplo asterisco

OBS: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

Parâmetros da função são a, b, c, logo, as chaves dos dicionários devem ser a, b, c também.

"""

