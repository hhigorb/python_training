"""
POO - Métodos

Métodos (funcões) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no
seu sistema.

Em Python, dividimos os métodos em 2 grupos: Métodos de instância e Métodos de Classe.

Métodos de instância: Método de instância é um método que está dentro da própria classe.

O método dunder init __init__ é um método especial chamado de construtor, sua função é construir o objeto a partir
da classe.

OBS: Qualquer elemento em Python que se inicia e finaliza com duplo underline é chamado de dunder (Double Underline).
Os métodos/funções dunder em Python ssão chamados de métodos mágicos.

ATENÇÃO: Por mais que possamos criar nossos próprios métodos utilizando dunder, não é aconselhado. O Python
possui vários métodos com essa forma de nomenclatura e pode ser que mudemos o comportamento dessas funções
mágicas internas da linguagem. Então, de preferência, nunca o faça.

Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.

Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return self.valor * (100 - porcentagem) / 100


class Usuario:

    usuarios = 5000

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.usuarios} usuários no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__email = email
        self.senha = senha
        print(f'Usuário criado com sucesso: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    # método privado:
    def __gera_usuario(self):
        return self.__email.split('@')[0]


p1 = Produto('Playstation 4', 'Videogame', 2300)
print(p1.desconto(20))

user1 = Usuario('Higor', 'Henrique', 'teste@gmail.com', 12345)
user2 = Usuario('Marcos', 'Paulo', 'teste2@gmail.com', 54321)
print(user1.nome_completo())
print(user2.nome_completo())


# Método de classe:

Usuario.conta_usuarios()