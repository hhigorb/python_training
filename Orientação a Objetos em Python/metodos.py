"""
POO - Métodos

Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar
no seu sistema.

Em Python, dividimos os métodos em 2 grupos:
    - Métodos de instância
    - Métodos de classe

Métodos de instância

O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto
a partir da classe.

Todos elementos em Python que iniciam e finalizam com duplo underline são chamados de dunder (double underline)

Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO: Por mais que possamos criar nossos próprios métodos utilizando dunder, não é aconselhado. O Python
possui vários métodos com essa forma de nomenclatura e pode ser que mudemos o comportamento dessas funções
mágicas internas da linguagem. Então, de preferência, nunca o faça.

Métodos são escritos em letras minúsculas. Se for nome composto, o nome terá as palavras separadas por underline.

from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.numero = ContaCorrente.contador + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.contador = self.id

    def desconto(self, porcentagem):
        """"""Retorna o valor do produto com o desconto aplicado""""""
        return self.valor * (100 - porcentagem) / 100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'Seu nome completo é: {self.nome} {self.sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.senha):
            return True
        return False


p1 = Produto('Playstation 4', 'Videogame', 4000)
print(p1.desconto(10))

usuario1 = Usuario('Higor', 'Silva', 'higor@gmail.com', '123456')
usuario2 = Usuario('Larissa', 'Bussamara', 'larissa@gmail.com', '654321')

print(usuario1.nome_completo())
print(usuario2.nome_completo())

nome1 = input('Digite seu nome: ')
sobrenome1 = input('Digite seu sobrenome: ')
email1 = input('Digite seu e-mail: ')
senha1 = input('Digite sua senha: ')

user1 = Usuario(nome1, sobrenome1, email1, senha1)
print(user1.senha)




"""

from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.numero = ContaCorrente.contador + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.contador = self.id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto aplicado"""
        return self.valor * (100 - porcentagem) / 100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = cryp.hash(senha)

    def nome_completo(self):
        return f'Seu nome completo é: {self.nome} {self.sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.senha):
            return True
        return False


# Métodos de Classe:







