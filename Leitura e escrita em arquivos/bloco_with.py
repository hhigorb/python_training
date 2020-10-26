"""
O bloco with

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após
o bloco with.



"""

# Utilizando o bloco with (forma pythônica de manipular arquivos):

with open('texto.txt') as arquivo:
    print(arquivo.readline())
    print(arquivo.closed)  # false -> o arquivo ainda está aberto já que está no with

print(arquivo.closed)