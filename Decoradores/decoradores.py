"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorator tem uma sintaxe própria usando @.

# Decorators:


def primeira_mensagem(funcao):
    def segunda_mensagem():
        print('Prazer te conhecer!')
        funcao()
        print('Tenha um excelente dia!')
    return segunda_mensagem


@primeira_mensagem
def apresentacao():
    print('Meu nome é Higor!')


apresentacao()


"""

from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo}ms para executar')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(5):
        sleep(1)


demora()











