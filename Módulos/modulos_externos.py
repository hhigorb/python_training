"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

"""

from colorama import(
    init,
    Fore,
    Back,
    Style,
)

init()
print(Fore.RED + 'Higor Henrique da Silva')

