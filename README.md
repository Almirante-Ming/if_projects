api rest feita em fastapi com sqlachemy e pgsql

para executar o projeto:

-poetry env activate
-pip install

comandos para execucao:

run = 'fastapi dev tinto/app.py --host 0.0.0.0'

test = 'pytest -s -x --cov=bordeux -vv'
post_test = 'coverage html'
lint = 'ruff check . && ruff check . --diff'
format = 'ruff check . --fix && ruff format .'