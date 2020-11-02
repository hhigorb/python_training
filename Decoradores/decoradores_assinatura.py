"""
Decoradores scom diferentes assinaturas

A assinatura de uma função é representado pelo seu retorno, nome e parâmetros de entrada.

# relembrando:


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


print(saudacao('Higor'))


# Refatorando com a Decorator Pattern


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Eu gostaria de {principal} acompanhado de {acompanhamento}, por favor!'


# testando:

print(saudacao('Higor'))
print(ordenar('Picanha', 'Batata Frita'))


# Vale lembrar que, podemos utilizar parâmetros nomeados.

print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

"""

# Decorator com argumentos:


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(n1, n2):
    return n1 + n2


# testando:

print(comida_favorita('banana', 'melancia'))

print(soma_dez(10, 30))
