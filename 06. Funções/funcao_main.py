"""
Em Python, a função main não tem um significado especial como em algumas outras linguagens de programação, como C ou C++. Em vez disso,
é uma convenção de nomenclatura que algumas pessoas usam para indicar o ponto de entrada principal de um programa.

O ponto de entrada principal de um script Python é geralmente o código que está no nível mais alto do arquivo. Por exemplo:
"""

def main():
    # Código principal do programa aqui
    print("Olá, mundo!")

if __name__ == "__main__":
    main()

"""
Neste exemplo, a função main é definida para conter o código principal do programa. Em seguida, a condição if __name__ == "__main__": garante que
o código dentro dele só será executado se o script for executado diretamente (em oposição a ser importado como um módulo em outro script).
Isso é uma prática comum para permitir que o mesmo script seja usado tanto como um programa independente quanto como um módulo importável.
"""
