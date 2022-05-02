"""
Try / Except / Else / Finally

Dica de quando e onde tratar código: TODA ENTRADA DEVE SER TRATADA!

# else -> é executado somente se não ocorrer o erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você precisa digitar um número!')
else:
    print(f'Você digitou {num}')

# Finally:

try:
    num = int(input('Digite um número: '))
except ValueError:
    print('Você precisa digitar um número!')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.
# O finally geralmente é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo:


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto, digite um valor inteiro.'
    except ZeroDivisionError:
        return 'Não é possível dividir um número por zero'


print(dividir(3, 0))


"""

# Forma semi-genérica de tratar exceções:


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(3, 'b'))




