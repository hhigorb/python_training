# if __name__ == "__main__"

O `if __name__ == "__main__"` é uma construção em Python que permite que você escreva código que será executado apenas quando o arquivo Python for
executado diretamente, e não quando ele for importado como um módulo em outro programa.

O Python atribui automaticamente um nome especial "main" ao arquivo que está sendo executado. Isso significa que quando você executa
o arquivo Python diretamente, ele tem o nome "main".

O bloco `if __name__ == "__main__"`: é uma maneira de verificar se o arquivo Python está sendo executado como um programa principal ou se está sendo
importado como um módulo em outro programa.

Se o arquivo estiver sendo executado diretamente, o código dentro do bloco if __name__ == "__main__": será executado. Isso permite que você
coloque o código que deseja que seja executado quando o arquivo é usado como um programa independente.

Se o arquivo for importado como um módulo em outro programa, o código dentro do bloco if __name__ == "__main__": não será executado, pois
o nome "main" não corresponderá ao nome do arquivo.

Em resumo, o `if __name__ == "__main__"`: é usado para garantir que o código dentro dele seja executado apenas quando o arquivo Python for
executado diretamente, tornando-o útil para criar scripts executáveis, mas não para código que é apenas reutilizável como um módulo em outros programas.
