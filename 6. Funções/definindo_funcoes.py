"""
Definindo funções

- Funções são pequenas partes de código que realizam tarefas específicas
- Pode ou não receber entradas de dados e retornar uma saída de dados
- Muito úteis para executar procedimentos similares por repetidas vezes

OBS: Se você escrever uma função que realiza várias tarefas dentro dela é
bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos o curso:
- print()
- len()
- max()
- min()
- count()
e muitas outras

Exemplo de utilização de funções:

cores = ['Verde', 'Amarelo', 'Azul', 'Branco']

Utilizando a função integrada (Built-in) do Python - print()

print(cores)

Como definir uma função?

Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
nome_da_funcao -> SEMPRE com letra minúsculas, e se for nome composto, separado por underline
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser
opcionais ou não
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função
acontece. Neste bloco, pode ter ou não retorno da função.

OBS: Para definir uma função, utilizamos a palavra reserva 'def'. Além disso, o bloco de código é aberto
com os 'dois pontos'.

Definindo a primeira função:

def diz_oi():
    print('Oi!')

OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções
2 - Veja que nossa função só executa 1 tarefa, ou seja, única coisa que ela faz é dizer "Oi"
3 - Veja que esta função não recebe nenhum parâmetro de entrada
4 - Veja que esta função não retorna nada.

Utilizando funções:

diz_oi()

ATENÇÃO:
Nunca esqueça de utilizar o parênteses ao executar uma função!

Exemplo 2:


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida!')

cantar_parabens()

"""


