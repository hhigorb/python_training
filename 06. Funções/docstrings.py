"""
Docstrings em Python são strings de documentação usadas para documentar módulos, classes, funções ou métodos.
Elas são definidas dentro do código fonte e servem para descrever o propósito, comportamento e uso de uma parte específica do código.

Podemos ter acesso a documentação de uma função em Python utilizando
a propriedade __doc__

Podemos ainda fazer acesso à documentação com a função help():

print(help(diz_oi()))

As docstrings são colocadas no início de um módulo, classe, função ou método, entre aspas triplas (' ou ").
Elas são opcionais, mas são consideradas uma boa prática de programação, pois ajudam outros programadores
(e até mesmo você mesmo, no futuro) a entenderem o funcionamento do código.

Por exemplo, uma docstring de uma função poderia descrever o que a função faz, quais são os seus parâmetros e o que ela
retorna. Aqui estão alguns exemplos simples:
"""

def soma(a, b):
    """
    Esta função retorna a soma de dois números.

    Args:
        a (int): O primeiro número.
        b (int): O segundo número.

    Returns:
        int: A soma de a e b.
    """
    return a + b

"""
Neste exemplo, a docstring descreve brevemente o propósito da função soma, os parâmetros que ela espera
(a e b), e o que ela retorna (um inteiro, que é a soma de a e b).
"""

"""
Outro exemplo
"""

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'


print(diz_oi())


def exponencial(numero, potencia=2):
    """
    função que retorna por padrão o quadrado de 'numero', ou 'número' à potência informada
    :param numero: Número que desejamos retornar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'número' por 'potencia'
    """
