"""
Debug de Código

Veja este tutorial de como debugar scripts Python no VSCode:
https://code.visualstudio.com/docs/python/debugging

Debugar é uma prática essencial no desenvolvimento de software para encontrar e corrigir erros no código.
Aqui estão alguns dos principais conceitos e tópicos relacionados ao processo de depuração em Python:

Breakpoint: Ponto onde a execução do programa é pausada para inspecionar variáveis e estado do programa.

Step Over: Executa a próxima linha de código, mas não entra em funções chamadas; continua na linha seguinte.

Step Into: Executa a próxima linha de código e entra nas funções chamadas para inspecionar o que acontece dentro delas.

Step Out: Continua a execução até sair da função atual, pausando na linha de código que chamou essa função.

Watch Expressions: Expressões monitoradas para ver como seus valores mudam durante a execução do programa.

Call Stack: Exibe a sequência de chamadas de função que levou ao ponto atual de execução.

Variable Inspection: Inspeção dos valores das variáveis durante a depuração para entender como os dados estão sendo manipulados.

Conditional Breakpoints: Breakpoints que só pausam a execução quando uma condição específica é verdadeira.

Exception Handling: Pausa a execução quando uma exceção é levantada, mesmo que seja tratada depois, para investigar a causa do erro.

Logging: Registro de informações sobre a execução do programa em diferentes níveis de severidade (DEBUG, INFO, WARNING, ERROR, CRITICAL).

Debugando com PDB

PDB -> Python Debugger

Em Python, podemos debugar de várias formas, com IDEs diferentes, como PyCharm ou VSCode (oferece um 
painel de depuração onde você pode adicionar breakpoints e inspecionar variáveis), ou até mesmo
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




