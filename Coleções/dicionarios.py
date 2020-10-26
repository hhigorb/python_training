"""
Dicionários

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chave {}

OBS: Sobre dicionários:
    - Chave e valor são separados por dois pontos: 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados.

Criação de dicionários:

Forma 1 (mais comum):

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

Forma 2 (menos comum):

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

Acessando elementos:

Forma 1: Acessando via chave, da mesma forma que lista/tupla:

print(paises['br'])
print(paises['py'])

Forma 2: Acessando via get (recomendado):

print(paises.get('br'))
print(paises.get('ru')) -> Caso o get não encontre o objeto com a chave informada será retornado 'None'

Verificando se existe tal país com if else:

pais = paises.get('br')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print(f'Não encontrei o país')


Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada:

pais = paises.get('br', 'Não encontrado')
print(f'Encontrei o país {pais}')

Verificar se determinada chave está contida no dicionário:

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionários como
chaves de um dicionário

Exemplo de tupla como chave:

localidades = {
    (32.4532, 39.3422): 'Escritório em Tóquio',
    (39.3232, 32.3232): 'Escritório em Nova York',
    (40.2332, 32.2322): 'Escritório em São Paulo',
}

print(localidades)
print(localidades.get((32.4532, 39.3422)))

Adicionar elementos em um dicionário:

receita = {
    "Janeiro": 100,
    "Fevereiro": 200,
    "Março": 300,
}


Forma 1:

receita["Abril"] = 400
print(receita)

Forma 2:

receita.update({"Maio": 500})
print(receita)

Atualizar dados em um dicionário:

receita.update({"Maio": 600})
print(receita)

CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
CONCLUSÃO 2: Em dicionários NÃO podemos ter chaves repetidas.

Remover dados de um dicionário:

Forma 1:

retorno = receita.pop("Março")
print(receita)
print(retorno)

OBS 1: Em dicionários, precisamos SEMPRE informar a chave.
OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

Forma 2:

del receita['Fevereiro']
print(receita)

OBS: Neste caso ele deleta o elemento e não retorna nenhum valor.

Imagine que você tem um comércio eletrônico onde temos um carrinho de compras no qual adicionamos produtos.


Carrinho de compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;


1 - Poderíamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstion 4', 1, '2300.00']
produto2 = ['God of War 4', 1, '230.00']

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

O problema é que teríamos que saber qual o índice de cada informação no produto.

2 - Poderíamos utilizar uma tupla para isso? Sim

produto1 = ('Playstion 4', 1, '2300.00')
produto2 = ('God of War 4', 1, '230.00')

carrinho = (produto1, produto2)
print(carrinho)

Aqui também problema é que teríamos que saber qual o índice de cada informação no produto.

3 - Poderíamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {
    "nome": "Playstation 4",
    "quantidade": 1,
    "preço": 2300.00
}

produto2 = {
    "nome": "God of War 4",
    "quantidade": 1,
    "preço": 230.00

}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto, além de podermos
ter certeza sobre cada informação.

Métodos para dicionários:

dicionario = {
    "a": 1,
    "b": 2,
    "c": 3,
}

Limpar o dicionário (zerar dados):

dicionario.clear()
print(dicionario)

Copiando um dicionário para outro:

Forma 1 (Deep Copy):

novo = dicionario.copy()
print(novo)

Forma 2 (Shallow Copy):

novo = dicionario
print(novo)
novo.update({"d": 4})

print(novo)
print(dicionario)

A diferença entre Deep Copy e Shallow Copy é que a cópia da Deep Copy não afeta o valor original,
já a Shallow Copy se houver alguma mudança em qualquer dado será revertido na original e na cópia

Forma não usual de criação de dicionários:

teste1 = {}.fromkeys('a', 'b')
print(teste1)

usuario = {}.fromkeys(['nome', 'pontos', 'profile'], 'desconhecido')
print(usuario)

O método fromkeys recebe dois parâmetros, um iterável e um valor.
Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

teste2 = {}.fromkeys('teste', 'valor') -> O "te" do final não aparece pois não há repetição de chave em dicionários
print(teste2)

teste3 = {}.fromkeys(range(0, 11), 'novo')
print(teste3)

"""


