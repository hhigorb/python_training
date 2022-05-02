"""
Bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim
que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execucação problemática
except:
    // o que deve ser feito em caso de problemas

# Exemplo 1 - Tratando um erro genérico

try:
    higor()
except:
    print('Deu algum problema')

# Tente executar a função higor(), caso você encontre erros, imprima a mensagem de erro

# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema')

# Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar
de forma específica

# Exemplo 3 - Tratando um erro específico

try:
    higor()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico

try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - Tratando um erro específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamento de erros de uma vez:

try:
    len(5)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')


"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return 'O valor solicitado não existe'


dic = {"nome": "Higor"}
print(pega_valor(dic, "nome1"))


