"""
Para executar um script Python pela linha de comando, você pode usar o comando python ou python3,
dependendo de como o Python está configurado no seu sistema. O comando básico é:

python3 main.py

Aqui, python3 chama o interpretador Python, e main.py é o nome do arquivo do seu script.

Passando Argumentos para o Script
Às vezes, você pode querer passar argumentos para o seu script Python para alterar seu comportamento sem modificar o código.
Isso pode ser feito simplesmente adicionando os argumentos após o nome do script na linha de comando. Por exemplo:

python3 main.py arg1

Neste caso, arg1 é um argumento que você está passando para o script main.py.

Acessando Argumentos no Script
Para acessar esses argumentos dentro do seu script Python, você pode usar o módulo sys. Aqui está um exemplo simples de como fazer isso:
"""

# main.py

import sys

def main():
    # sys.argv é uma lista que contém os argumentos passados para o script
    args = sys.argv[1:]  # Ignora o primeiro elemento, que é o nome do script

    if args:
        print("Argumentos recebidos:", args)
    else:
        print("Nenhum argumento recebido")

if __name__ == "__main__":
    main()

"""
Ao executar python3 main.py arg1, a saída será:

Argumentos recebidos: ['arg1']
"""
