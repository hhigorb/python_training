"""
POO - Métodos Mágicos

Métodos mágicos são todos os métodos que utilizam dunder (Double Underscore)

dunder init -> __init__ -> Inicializa o método construtor

dunder rapr -> __repr__ -> O __repr__ serve para exibir o objeto para o programador, usada pelo console do Python
e pela funçao repr.

dunder str -> __str__ -> O __str__ serve para exibir o objeto para usuário final, usada pelo comando print e pela
função str

dunder del -> __del__ -> Apaga um objeto da memória


"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'Um objeto do tipo Livro foi deletado da memória!')

    def __add__(self, outro):
        return f'{self} - {outro}'


livro1 = Livro('Python Rocks', 'Higor', 400)
livro2 = Livro('Python IA', 'Higor', 500)

print(livro1)
print(len(livro1))