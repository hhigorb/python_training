"""
POO - Classes

Classes são modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos: Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto. No caso da lâmpada, por exemplo, possivelmente iríamos
    querer saber se a lâmpada é 110 ou 220 volts, qual a sua cor, qual sua luminosidade, etc.

    - Métodos (funções): Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
    realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente
    iremos representar no sistema é o de ligar e desligar a lâmpada.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado.

Quando nomeamos nossas classes em Python, utilizamos por convenção o nome com inicial em maiúsculo.
Se o nome for composto, utiliza-se as iniciais de ambas as palavras com maiúsculo, todas juntas.

Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes
objetos que serão mapeados para classes de entidade.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


lamp = Lampada()
print(type(lamp))





