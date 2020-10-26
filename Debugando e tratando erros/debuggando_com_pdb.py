"""
Debuggando com PDB
PDB -> Python Debugger

Em Python, podemos debuggar de várias formas, com IDEs diferentes, como PyCharm ou VSCode, ou até mesmo
utilizando o PDB - Python Debugger

# Exemplo com Pycharm:

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 2))

# Exemplo com PDB - Python Debugger:

# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

Comandos básicos do PDB:
l -> Listar onde estamos no código
n -> Próxima linha
p -> Imprime variável
c -> Continua a execução - finaliza o debugging

import pdb

nome = 'Higor'
sobrenome = 'Henrique'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + 'faz o curso ' + curso
print(final)

import pdb

nome = 'Higor'
sobrenome = 'Henrique'
pdb.set_trace()  # ou breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + 'faz o curso ' + curso
print(final)

# A partir do Python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando debug foi
incorporado como função built-in chamada breakpoint()


"""




