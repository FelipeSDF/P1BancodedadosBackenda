# API de Filmes (FastAPI + MongoDB)

Um sistema de backend CRUD (Create, Read, Update, Delete) com FastAPI focado em listagem e gestão de filmes, sendo servido junto a um banco de dados não-relacional utilizando conteinerização Docker.

## 🚀 Tecnologias Utilizadas
- **FastAPI**: Framework web focado em agilidade e performance.
- **MongoDB**: Banco de dados NoSQL.
- **Docker & Docker Compose**: Gerenciamento de containers para o ambiente do banco.
- **PyMongo**: Driver oficial do Python para conversar com o MongoDB.
- **Pydantic**: Responsável pela tipagem, validação e serialização de dados (Schemas).

## 🏗️ Arquitetura Modular
Este projeto emprega a arquitetura modular em camadas, a fim de separar obrigações e facilitar a manutenção do código:
- `routers/`: Define as rotas/endpoints da API. É a principal via de entrada HTTP.
- `services/`: Camada que trata as lógicas e regras de negócio e eventuais tratativas de erro.
- `repositories/`: Camada que se comunica diretamente de maneira pura com o banco de dados.
- `schemas/`: Camada responsável pela validação do formato exigido (4 atributos).
- `database.py`: Instancia o MongoClient.

## 🛠️ Como rodar o projeto localmente

1. Certifique-se de que o **Docker** está aberto no seu computador e suba o contêiner do MongoDB:
```bash
docker compose up -d
```

2. (Recomendado) Crie e ative o ambiente virtual para as bibliotecas de Python:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Instale as bibliotecas necessárias declaradas:
```bash
pip install -r requirements.txt
```

4. Dispare o servidor local:
```bash
uvicorn app.main:app --reload
```

## 📚 Documentação interativa
A documentação da API e as rotas de testes ficam atreladas via [Swagger UI](http://127.0.0.1:8000/docs). Lá você consegue disparar POST, GET, PUT e DELETE nativamente.
