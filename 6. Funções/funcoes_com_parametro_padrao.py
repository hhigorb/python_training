"""
Funções com parâmetro padrão

- Funções onde a passagem de parâmetro seja opcional.

Exemplo de função onde a passagem de parâmetro seja opcional:

print('Higor Henrique')
print()

Exemplo de função onde a passagem de parâmetro seja obrigatória:

def quadrado(numero):
    return numero ** 2

print(quadrado())

Função com parâmetro opcional:


def exponencial(numero, potencia=2):
    return numero ** potencia

Se for passado apenas um argumento, o parâmetro potencia terá o valor padrão 2.
Se for passado 2 argumentos, será considerado os argumentos digitados pelo usuário.

OBS: Em funções Python, os parâmetros com valores padrão DEVEM sempre estar ao final da declaração:


ERRO:
def teste(num=2, potencia):
    return num ** potencia

CORRETO:
def teste(potencia, num=2):
    return num ** potencia

def mostra_informacao(nome='Higor', instrutor=False):
    if nome == 'Higor' and instrutor:
        return 'Bem vindo, instrutor Higor!'
    elif nome == 'Higor':
        return 'Eu pensei que você fosse o instrutor!'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(nome='Ozzy'))

Porque utilizar parâmetros com valor default?
- Nos permite ser mais flexiveis nas funções
- Evita erro com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legíveis de código

Quais tipos de dados podemos utilizar como valor default para parâmetros?
- Qualquer tipo de dado, entre eles:
    - Números, strings, floats, booleans, listas, tuplas, dicionários, funções etc.

Exemplos:


def soma(n1, n2):
    return n1 + n2


def mat(n1, n2, func=soma):
    return func(n1, n2)


def subtracao(n1, n2):
    return n1 - n2


print(mat(2, 3))
print(mat(2, 3, subtracao))

Escopo - evitar problemas e confusões

Variáveis globais
Variáveis locais

nome = 'Higor'  # variavel global


def diz_oi():
    nome = 'Python' # variavel local
    return f'Oi {nome}'


print(diz_oi())

OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    nome = 'Higor'  # variavel local
    return f'Olá {nome}'


print(diz_oi())
print(nome)  -> Como é uma variável local, ela não existe no escopo global, logo gera um erro

ATENÇÃO COM VARIÁVEIS GLOBAIS:

total = 0


def incrementa():
    total += 1  -> A variável local está sendo utilizada para processamento sem ter sido inicializada
    return total

print(incrementa())

Resolvendo o problema:

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total += 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())


"""

