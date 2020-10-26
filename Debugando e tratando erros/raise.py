"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

# Exemplo


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Higor', 'azul')

# Primeiro exemplo refatorado:

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Higor', 'preto')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""




