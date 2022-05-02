"""
POO - Abstração e Encapsulamento

O objetivo da programação orientada a objeto é encapsular o código dentro de um grupo lógico e hierárquico utilizando
classes.

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados
de usuário.


"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor precisa ser maior que 0!')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print(f'Saldo insuficiente!')
        else:
            print('Valor deve ser positivo!')

    def transferencia(self, valor, conta_destino):
        # 1 - Remover valor da conta origem
        self.__saldo -= valor

        # 2 - Adicionar valor na conta destino:
        conta_destino.__saldo += valor


conta1 = Conta('Higor', 5000, 10000)
conta2 = Conta('Marcos', 1000, 5000)

print(conta1.__dict__)
conta1.depositar(1000)
print(conta1.__dict__)

conta1.sacar(1000)
print(conta1.__dict__)

conta1.transferencia(100, conta2)
print(conta1.__dict__)
print(conta2.__dict__)



