"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos e métodos
da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matrícula

Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?

class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('higor', 'henrique', '123.456.789.11', 5000)
funcionario1 = Funcionario('carlos', 'peixoto', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [PESSOA]
    - Super Classe
    - Classe mãe
    - Classe pai
    - Classe base
    - Classe genérica

Quando uma classe herda de outra classe, ela é chamada:
    [CLIENTE, FUNCIONÁRIO]
    - Sub classe
    - Classe filha
    - Classe específica


Sobrescrita de métodos (Overriding):

Sobrescrita de método ocorre quando reescrevemos/reimplementamos um método presente na super classe em classes
filhas.

Com a função super(), é possível acessar qualquer atributo ou método da super classe.
"""

# Refatorando as classes com HERANÇA:


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Nome: {self.nome}, matrícula: {self.__matricula}'


cliente1 = Cliente('higor', 'henrique', '123.456.789.11', 5000)
funcionario1 = Funcionario('carlos', 'peixoto', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())