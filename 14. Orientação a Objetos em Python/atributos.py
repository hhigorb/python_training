"""
POO - Atributos

Atributos representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python, divimos os atributos em 3 grupos:
    - Atributos de instância
    - Atributos de classe
    - Atributos dinâmicos

Atributos de instância: São atributos declarados dentro do método construtor.

Método construtor: É um método especial utilizado para a construção do objeto.

Em Python, por convenção, ficou estabelecido que todos os atributo de uma classe são públicos.
Ou seja, pode ser acessado em qualquer parte do projeto.
Caso queira demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado
somente dentro da própria classe onde está declarado, utiliza-se como __ (duplo underscore) no início de seu nome.
Isso é conhecido também como Name Mangling.


"""

# classes com atributo de Instância Público:


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# classe com atributo de instãncia privado:

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# exemplo:


user = Acesso('higor', '123456')
print(user.email)
# print(user.senha)  # gera um AttributeError, já que o atributo está privado

# mas é possível acessa-lo da seguinte forma:
print(user._Acesso__senha)  # temos acesso mas não deveríamos fazer este acesso (Name Mangling)


user.mostra_email()
user.mostra_senha()


# O que significa atributos de instância?

# Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')


# Atributos de Classe:

# atributos de classe são atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente
# já inicializamos um valor e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de
# cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de
# classe todas as instâncias terão o mesmo valor para esse atributo

# Refatorando a classe Produto:


class Produto:

    # atributo de classe:
    imposto = 1.05  # 5% de imposto

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto


p1 = Produto('Playstation 4', 'Videogame', 4000)
p2 = Produto('Xbox One', 'Videogame', 3000)

print(p1.valor)
print(p2.valor)
print(Produto.imposto)


# Atributos dinâmicos -> Um atributo de instância que pode ser criado em tempo de execucão.
# O atributo dinâmico será exclusivo da instância que o criou.

p3 = Produto('Geladeira', 'Eletrodoméstico', 5000)
p4 = Produto('Fogão', 'Eletrodoméstico', 1000)

# criando um atributo dinâmico em tempo de execução:

p4.peso = '5kg'

print(f'Produto: {p4.nome}, Descrição: {p4.descricao}, Valor: {p4.valor}, Peso: {p4.peso}')

# deletando atributos:

del p4.peso
del p4.valor
del p4.descricao

print(p4.__dict__)