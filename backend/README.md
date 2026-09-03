# 🚀 Projeto Ela — Backend API

Backend profissional desenvolvido em **Python** utilizando **FastAPI**, **SQLAlchemy**, **PostgreSQL** e **Alembic**, estruturado sob os princípios de **Arquitetura em Camadas (Layered Architecture / Clean Architecture)**.

---

## 🏗️ Arquitetura do Projeto

O projeto segue a separação estrita de responsabilidades:

```
[ Cliente (Frontend / Postman) ]
              │
              ▼ (1. Envia Requisição com Dados)
        [ DTOs (pydantic) ]
              │
              ▼ (2. Valida os campos)
       [ Routes (FastAPI) ]
              │
              ▼ (3. Delega para a camada de negócio)
      [ Services (Lógica) ]
              │
              ▼ (4. Solicita persistência ou consulta)
   [ Repositories (SQLAlchemy) ]
              │
              ▼ (5. Comunica com o Banco de Dados)
     [ PostgreSQL / Supabase ]
```

### 📂 Estrutura de Pastas

```text
Projeto ela/
│
├── dtos/                   # Data Transfer Objects (Validação de Entrada com Pydantic)
│   └── UsuarioDto.py
│
├── models/                 # Mapeamento Objeto-Relacional (Entidades do Banco com SQLAlchemy)
│   ├── usuario.py
│   ├── Empresa.py
│   ├── Servicos.py
│   ├── Categoria.py
│   └── Agendamento.py
│
├── repositories/           # Camada de Acesso a Dados (Consultas SQL e Persistência)
│   ├── usuario_repository.py
│   ├── empresa_repository.py
│   ├── servico_repository.py
│   ├── categoria_repository.py
│   └── agendamento_repository.py
│
├── services/               # Camada de Regras de Negócio (Lógica, Validações e Criptografia)
│   ├── usuario_service.py
│   ├── empresa_service.py
│   ├── servico_service.py
│   ├── categoria_service.py
│   ├── agendamento_service.py
│   └── auth_service.py
│
├── routes/                 # Controladores / Endpoints REST (FastAPI APIRouter)
│   ├── usuario_routes.py
│   ├── empresa_routes.py
│   ├── servico_routes.py
│   ├── categoria_routes.py
│   ├── agendamento_routes.py
│   └── auth_routes.py
│
├── alembic/                # Histórico e scripts de Migrações de Banco de Dados
├── alembic.ini             # Configuração do Alembic
├── database.py             # Configuração da Conexão SQLAlchemy e Engine
├── dependecies.py          # Injeção de Dependências (Session do Banco)
├── requirements.txt        # Dependências do Projeto
├── main.py                 # Ponto de entrada da aplicação FastAPI
└── .env                    # Variáveis de Ambiente (Segredos e URL do Banco)
```

---

## 📦 Dependências e Tecnologias

Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`:

| Pacote | Função no Projeto |
| :--- | :--- |
| **`fastapi`** | Framework web moderno, assíncrono e de alta performance. |
| **`uvicorn[standard]`** | Servidor ASGI rápido para rodar a aplicação FastAPI. |
| **`sqlalchemy`** | ORM para mapeamento e manipulação do banco de dados relacional. |
| **`pydantic`** | Validação estrita de tipos e schemas de dados (DTOs). |
| **`bcrypt`** | Criptografia de senhas com hashing seguro e geração de salt. |
| **`psycopg2-binary`** | Driver de comunicação com o banco de dados PostgreSQL. |
| **`alembic`** | Gerenciador de migrações automáticas de esquema do banco. |
| **`python-dotenv`** | Carregamento de variáveis de ambiente a partir do arquivo `.env`. |
| **`python-jose`** | Geração e validação de tokens JWT para autenticação. |
| **`python-multipart`** | Suporte para upload de arquivos e formulários HTTP. |

---

## ⚙️ Pré-requisitos e Instalação

### 1. Clonar o repositório
```bash
git clone <url-do-repositorio>
cd "Projeto ela"
```

### 2. Criar e ativar o Ambiente Virtual (venv)
* **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **Linux / Mac:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração do Arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto (caso não exista) com as seguintes chaves:

```env
DATABASE_URL=postgresql://usuario:senha@host:5432/nome_do_banco
SECRET_KEY=sua_chave_secreta_aqui
```

---

## 🗄️ Migrações de Banco de Dados (Alembic)

Para aplicar as migrações e criar as tabelas no banco de dados:

```bash
# Gerar uma nova migração (caso altere models)
alembic revision --autogenerate -m "criar tabelas"

# Aplicar as migrações no banco
alembic upgrade head
```

---

## ▶️ Como Executar o Servidor

Inicie o servidor de desenvolvimento com recarregamento automático (*live reload*):

```bash
py -m uvicorn main:app --reload
```
*(Ou `uvicorn main:app --reload` dependendo do seu sistema).*

O servidor iniciará em: **`http://127.0.0.1:8000`**

---

## 📖 Documentação Interativa da API (Swagger / OpenAPI)

Com o servidor rodando, acesse a documentação interativa e teste todos os endpoints diretamente no navegador:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
