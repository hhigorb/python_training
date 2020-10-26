"""
Decorators com diferentes assinaturas

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.

# Relembrando


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, meu nome é {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'

# testando


print(saudacao('Higor'))
print(ordenar('Picanha', 'Batata Frita'))


"""





