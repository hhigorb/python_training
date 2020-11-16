"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe
filha herde todos os atributos e métodos de todas as classes herdadas.

A herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação direta
    - Por multiderivação indireta


# Exemplo 1 - Multiderivação direta


class Base1:
    pass


class Base2:
    pass


class MultiDerivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação indireta:


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass


Não importa se a derivação é direta ou indireta, a classe que realizar a herança herdará todos os atributos e métodos
das super classes.
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou o {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando!'

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
tatu.andar()
tatu.cumprimentar()

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())

