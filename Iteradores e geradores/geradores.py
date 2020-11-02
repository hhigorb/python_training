"""
Geradores

Geradores (generators) são iterators

OBS: O contrário não é verdadeiro. Ou seja, nem todos os iterators são generators.

Outras informações:
    - Generators podem ser criados com funções geradoras.
    - Funções geradoras utilizam a palavra reservada yield
    - Generators podem ser criados com Expressões Geradoras

Diferenças entre Funções e Generator Functions (funções geradoras):

Funções:
    - Utilizam return
    - Retorna um vez
    - Quando executada, retorna um valor


Generator Functions:
    - Utilizam yield
    - Podem utilizar yield múltiplas vezes
    - Quando executada, retorna um generator

yield é utilizado quando se tem uma função que retorna uma sequência e você precisa iterar sobre ela.

"""

# Exemplo de Generator Function:


def conta_ate(valor_maximo):
    contador = 0
    while contador <= valor_maximo:
        yield contador
        contador += 1


for numero in conta_ate(5):
    print(numero)









