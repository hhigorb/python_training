"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os

os -> Operating System

# realizar o import
import os

# getcwd() -> pega o current work directory
# retorna o path (caminho) absoluto
print(os.getcwd())

# para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')
print(os.getcwd())

# podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs("C:\\Users\\hhigo\\PycharmProjects\\Python"))

# podemos identificar o sistema operacional com o modulo os

print(os.name)  # posix (linux, Mac) e nt (windows)

# podemos ter mais detalhes do sistema operacional:

print(os.uname())


"""

import os

# podemos ter mais detalhes do sistema operacional:

print(os.uname())
