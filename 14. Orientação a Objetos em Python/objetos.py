"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma
classe como variáveis do tipo de definido na classe.

"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False

    def checa_lampada(self):
        return self.ligada

    def ligar_desligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Objetos nada mais são que instâncias da classe. Para instanciar um objeto, é necessário informar os parâmetros
# que foram solicitados no método construtor.

lampada = Lampada('Branca', 110, 'Forte')
print(f'A lâmpada está ligada: {lampada.checa_lampada()}')

lampada.ligar_desligar()

print(f'A lâmpada está ligada: {lampada.checa_lampada()}')

conta = ContaCorrente('12345', 5000, 10000)

usuario = Usuario('Higor', 'teste@gmail.com', 12345)




