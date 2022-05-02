"""
POO - O método suoer()

O método super() se refere à super classe
"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'{self.__especie} faz {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        #  Animal.__init__(self, nome, especie)  -> outra forma
        super().__init__(nome, especie)
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')

