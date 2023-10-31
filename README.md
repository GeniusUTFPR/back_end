# Genius - Sistema de Monitorias da UTFPR

Bem-vindo ao repositório do **Genius**, um sistema de monitorias para a matéria de Projeto Integrador da Universidade Tecnológica Federal do Paraná (UTFPR)! Este projeto foi desenvolvido por nossa equipe de desenvolvedores back-end:

- **Eduardo Riki**
- **Milena Churata**

## Sobre o Projeto

O **Genius** é uma plataforma web desenvolvida com o intuito de auxiliar os discentes da UTFPR com mais informações sobre as monitorias e palunos fornecidos dentro da instituição, além de oferecer monitorias pagas sobre determinadas disciplinas e até idiomas.

Foram utilizadas tecnologias modernas para facilitar e melhorar a usabilidade dos usuários, sendo elas:

- **Python**: Uma linguagem de programação versátil e poderosa.
- **Django**: Um framework web Python de alto nível que facilita o desenvolvimento rápido e seguro.
- **Django Rest Framework (DRF)**: Uma extensão para o Django que simplifica a criação de APIs RESTful.
- **SQLite**: Um sistema de gerenciamento de banco de dados leve e embutido.

## Instruções para execução

Siga as instruções abaixo para executar o backend em sua máquina local:

1. **Clone o repositório:**

```bash
git clone https://github.com/GeniusUTFPR/back_end.git 
```

2. **Crie um ambiente virtual para isolar localmente as dependências de pacotes**

```bash
python -m venv env
source env/bin/activate # No Windows usa `env\Scripts\activate`
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute as migrações do banco de dados:**

```bash
python manage.py migrate
```

5. **Inicie o servidor do Django:**

```bash
python manage.py runserver
```

6. **O backend estará disponível em [http://localhost:8000](http://localhost:8000).**

### Dicas de desenvolvimento:

1. **Caso esteja no Linux, utilize os comandos com `python3`**.


2. **Removendo temporários, migrations e o banco de dados:**

```bash
find . -name "__pycache__" -type d -exec rm -r {} +
find . -path "*/migrations/*.pyc" -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
rm db.sqlite3
```
