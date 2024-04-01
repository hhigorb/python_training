# Dependências em Python


Em Python, bibliotecas ou dependências (também conhecidas como "libs") são componentes essenciais para estender as funcionalidades básicas da linguagem.
Essas bibliotecas podem variar desde pacotes simples até frameworks robustos, e são fundamentais para a criação de uma ampla gama de aplicações,
desde scripts simples até sistemas complexos.

### Instalando as dependências

Para instalar uma dependência em Python, geralmente utilizamos o gerenciador de pacotes pip, que é amplamente utilizado e vem pré-instalado com a maioria
das distribuições Python. Basta executar o seguinte comando no terminal:

```terminal
pip install nome_da_dependencia
```

Isso baixará e instalará a dependência especificada no ambiente Python.

### Criando um arquivo de requisitos

Para manter um registro das dependências do seu projeto e facilitar a instalação em diferentes ambientes, é recomendável criar um arquivo de requisitos
(normalmente chamado de requirements.txt). Este arquivo contém uma lista das dependências e suas versões correspondentes. Você pode gerar esse arquivo
manualmente ou usando o comando pip freeze:

```terminal
pip freeze > requirements.txt
```

### Instalando dependências a partir de um arquivo de requisitos

Para instalar todas as dependências listadas em um arquivo de requisitos, basta executar:

```terminal
pip install -r requirements.txt
```

Isso instalará todas as dependências especificadas no arquivo de requisitos.

É importante sempre instalar essas dependências dentro de um ambiente virtual (venv) para isolar as dependências para cada projeto.

### Lidando com versões de dependências

É importante garantir que as versões das dependências do seu projeto sejam compatíveis e atualizadas regularmente.
Você pode especificar intervalos de versões no arquivo de requisitos, por exemplo:

```terminal
requests>=2.0.0,<3.0.0
pandas==2.0.0
numpy==1.26.1
duckdb==0.2
```

Isso significa que o projeto requer a biblioteca requests com uma versão igual ou superior a 2.0.0, mas inferior a 3.0.0.

Além disso, é uma boa prática atualizar regularmente suas dependências para garantir que você esteja aproveitando as últimas
correções de bugs e melhorias de desempenho.

