# Ambientes Virtuais em Python

Ambientes virtuais em Python são ferramentas que permitem isolar ambientes de desenvolvimento para diferentes projetos, evitando conflitos entre dependências.
Isso é especialmente útil quando você está trabalhando em vários projetos que podem ter requisitos diferentes de bibliotecas ou versões de bibliotecas.
Os ambientes virtuais permitem que você crie um ambiente isolado para cada projeto, garantindo que as dependências de um projeto não afetem os outros.

Existem várias ferramentas para criar ambientes virtuais em Python, mas uma das mais comuns é o venv (introduzido no Python 3.3) e o virtualenv.
Aqui estão os passos básicos para criar e usar um ambiente virtual usando venv:

1. Procure onde seu Python está instalado:

```bash
which python3
```

2. Crie sua virtualenv com o caminho do Python:

```bash
mkvirtualenv venv --python=/usr/local/bin/python3
```

3. Ative sua virtualenv. Normalmente as virtualenvs ficam na pasta .virtualenvs

```bash
source /Users/higor.silva/.virtualenvs/airflow/bin/activate
```

Outra forma de ativar seria:

```bash
workon nome_da_venv
```

4. Instale as dependências (libs) do arquivo requirements.txt dentro da virtualenv. Dessa forma, você evita conflito de dependências entre projetos.

```bash
pip3 install -r requirements.txt
```

Caso queira desativar a venv, utilize o comando **deactivate** no terminal.


Ao usar ambientes virtuais, você pode manter as dependências de cada projeto isoladas, facilitando a reprodução do ambiente de desenvolvimento
em diferentes máquinas e evitando conflitos entre projetos. Isso é especialmente útil quando você trabalha em projetos com diferentes requisitos de versão de bibliotecas.
