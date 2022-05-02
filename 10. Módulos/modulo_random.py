"""
Módulo Random - e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios.

OBS: Existem duas formas de se utilizar um módulo ou função deste

Forma 1 -> Importando o módulo completo (Não recomendado)

import random

OBS: Ao realizar import do módulo completo, todas as funções, atributos, classes e propriedades que estiverem
dentro do módulo ficarão disponíveis (ficarão em memória). Caso você saiba quais funções você precisa utilizar
deste módulo, então esta não seria a forma ideial de utilização.

random() -> gera um númeror real pseudo aleatório entre 0 e 1.
print(random.random())

Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função
separados por ponto.

Forma 2 -> Importando uma função específica do módulo (forma recomendada)

from random import random

No import acima estamos importando apenas a função random

for i in range(10):
    print(random())

# uniform() -> gerar um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído

# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos

from random import randint

# gerador de apostas para a mega-sena:
for i in range(6):
    print(randint(1, 61), end=', ')

# choice() -> mostra um valor aleatório entre um iterável

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))


"""

# shuffle() -> tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas)
