"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída

Refatorando uma função:


def quadrado(numero):
    return numero * numero


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

Refatorando a função:

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print(f'Muitos anos de vida, {aniversariante}')


cantar_parabens('Higor')

Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
em uma função quanto parâmetros forem necessários. Os parâmetros são separados por vírgula.

Exemplo:


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(52, 10))

print(multiplica(3, 5))
print(multiplica(4, 5))

print(outra(1, 2, 'teste '))

Nomeando parâmetros:


def nome_completo(nome, sobrenome):
    return (f'Seu nome completo é {nome} {sobrenome}')


print(nome_completo('Higor', 'Henrique'))

Diferença entre parâmetros e argumentos:

Parâmetros são variáveis declaradas na definição de uma função
Argumentos são dados passados durante a execução de uma função

A ordem dos parâmetros importa:

nome = 'Larissa'
sobrenome = 'Cristina'

print(nome_completo(sobrenome, nome))

Argumentos nomeados (Keyword Arguments)

Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos
utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Jo'))

Erro comum na utilização de return:


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

O return finaliza a função, como ele está no bloco do for, quando acabar o loop ele finalizará a função antes de
executar o restante. O correto seria:


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

"""

