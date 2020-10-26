"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos

Pacote -> É um diretório contendo uma coleção de módulos

OBS: Nas versões 2.x do Python, um pacote deveria conter dentro dele um arquivo chamado
__init__.py

Nas versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas normalmente
ainda é utilizado para manter compatibilidade.

from meu_pacote import pacote_1, pacote_2
from meu_pacote.sub_pacote import pacote_3, pacote_4

print(pacote_1.pi)

print(pacote_1.funcao1(4, 6))

print(pacote_2.curso)

print(pacote_2.funcao2())

print(pacote_3.funcao3())

print(pacote_4.funcao4())


"""

from meu_pacote.pacote_1 import funcao1
from meu_pacote.sub_pacote.pacote_3 import funcao3

print(funcao1(3, 4))
print(funcao3())

