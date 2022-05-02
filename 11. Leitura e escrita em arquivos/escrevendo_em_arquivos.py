"""
Escrevendo em arquivos

Ao abrir um arquivo para leitura, não é possível realizar a escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemo lê-lo, apenas escrever nele.

Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo: após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro.

Ao abrir um arquivo para escrita no modo write, se o arquivo não existir ele automaticamente será criado.
Caso já exista, será apagado e sobrescrito com o novo conteúdo solicitado.

# Exemplo de escrita - modo 'w' -> write

with open('texto.txt', 'w') as arquivo:
    arquivo.write('Escrevendo dados no arquivo...\n')
    arquivo.write('É possível adicionar quantas linhas quiser\n')
    arquivo.write('Última linha')


"""

# recebendo dados do usuário para escrita em arquivo:

with open('usuario.txt', 'w') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair' para sair: ")
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break



