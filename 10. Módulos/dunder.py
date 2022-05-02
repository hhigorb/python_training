"""
Dunder Name e Dunder Main
Dunder -> Double Under

Dunder Name -> __name__
Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos/propriedades/etc utilizando Double Under
para não gerar conflito com os nomes desses elementos na programação.

Se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá à variável
__name__ o valor __main__ indicando que este é o módulo de execução principal.

Pra que serve o if __name__ == '__main__'?

Caso o módulo que esteja sendo importado possua algum tipo de execução, como por exemplo print(), você estará
importando o módulo inteiro, juntamente os prints. Isso fará com que todos os prints do módulo sejam executados em
seu programa principal.

Para evitar isso, é necessário adicionar o name main:

if __name__ == '__main__':
    print(execucoes)
    print(execucoes2)

Essas execuções só aparecerão no módulo, onde será executado diretamente. Em seu programa será importado apenas as
funções.

Name Main é normalmente utilizado quando você cria algum módulo e precisa realizar alguns testes dentro dele. E para
não aparecer no import de outra pessoa, executa os testes dentro do name main.


"""

