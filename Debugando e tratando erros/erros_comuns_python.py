"""
Erros mais comuns em Python

ATENÇÃO:
É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python
não reconhece como parte da linguagem

# Exemplos SyntaxError:

1.
def funcao:
    print('Higor Henrique')

2.
def = 1


3.
return

NameError -> Ocorre quando uma variável ou função não foi definida

# Exemplos NameError:

1.
print(higor)

2.
higor()

TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado

# Exemplos TypeError:

1.
print(len(5))

2.
print('Higor' + [])

IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido

# Exemplos IndexError:

lista = ['Higor']
print(lista[1])

ValueError -> Ocorre quando uma função ou operação built-in recebe um argumento com tipo correto mas valor
inapropriado.

# Exemplos ValueError:

1.
print(int('Higor'))

KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

# Exemplos KeyError:

1.
dicionario = {"Higor": "Henrique"}
print(dicionario['Higor'])

AtrributeError -> Ocorre quando uma variável não tem atributo/função

Exemplos AttributeError:

1.
tupla = (11, 2, 31, 4)
print(tupla.sort())

IndentationError -> Ocorre quando não respeitamos indentação do Python (4 espaços)

Exemplos IndentationError:

1.
def nova():
print('Higor')

2.
for i in range(10):
print(i)

OBS: Expections e Erros são sinônimos na programação.

"""




