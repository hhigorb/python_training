"""
Documentando funções com Docstrings

Podemos ter acesso a documentação de uma função em Python utilizando
a propriedade __doc__

Podemos ainda fazer acesso à documentação com a função help():

print(help(diz_oi()))


"""

# Exemplos:


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