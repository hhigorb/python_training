"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decorators também são exemplos de Higher Order Functions
- Decorators tem uma síntaxe própria, usando '@'.


# Decorators como funções (síntaxe não recomendada):


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a)!')


# testando a função:

teste = seja_educado(saudacao)
teste()


# outro teste:

def boa_noite():
    print('Boa noite!!')


noite = seja_educado(boa_noite)
noite()


"""

# Decorators com síntaxe recomendada:


def seja_educado(funcao):
    def sendo_educado():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_educado


# utilizando decorator:
@seja_educado
def nome_pessoa():
    print(f'Olá, Higor!')


nome_pessoa()


# outro exemplo:

@seja_educado
def dormir():
    print('ZzZzZzZzZzZzZ')


dormir()































