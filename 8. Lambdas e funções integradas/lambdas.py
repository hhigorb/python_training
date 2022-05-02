"""
Utilizando lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja
funções anônimas.

Função em Python:
def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão lambda:
calculo = lambda x: 3 * x + 1  # -> Forma incorreta de se utilizar uma lambda. Não se utiliza em uma variável
print(calculo(3))

Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('      higor', '       henrique'))

Em funções Python podemos ter nenhuma ou várias entradas, em lambdas também!

Outro exemplo:

autores = ['Isaac Asimov', 'Ray Bradbury', 'Roberto Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells,', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


"""






