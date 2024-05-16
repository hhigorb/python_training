"""
Docstrings em Python são strings de documentação usadas para documentar módulos, classes, funções ou métodos.
Elas são definidas dentro do código fonte e servem para descrever o propósito, comportamento e uso de uma parte específica do código.

As docstrings são colocadas no início de um módulo, classe, função ou método, entre aspas triplas (' ou ").
Elas são opcionais, mas são consideradas uma boa prática de programação, pois ajudam outros programadores
(e até mesmo você mesmo, no futuro) a entenderem o funcionamento do código.

Por exemplo, uma docstring de uma função poderia descrever o que a função faz, quais são os seus parâmetros e o que ela
retorna. Aqui está um exemplo simples:
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
