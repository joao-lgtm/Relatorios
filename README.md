# Relatórios — API

API em **Django + Django REST Framework** para consulta de relatórios e importação/exportação de planilhas Excel. Serve o front-end [Relatorios-Front](https://github.com/joao-lgtm/Relatorios-Front).

## Funcionalidades

- Autenticação com **JWT** (SimpleJWT)
- Cadastro e listagem de usuários
- Listagem e consulta de relatórios com filtros
- **Upload de Excel** para o banco e **download** dos dados em Excel ou JSON (pandas + openpyxl)

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| POST | `/api/token/` | Gera o token de acesso |
| POST | `/api/token/refresh/` | Renova o token |
| GET | `/api/usuarios/` | Lista usuários |
| POST | `/api/usuarios/cadastrar/` | Cadastra usuário |
| GET | `/api/consultas/listar-relatorios/` | Lista os relatórios disponíveis |
| GET | `/api/consultas/consultar-relatorios/` | Consulta um relatório |
| POST | `/api/excel/upload-excel/` | Importa uma planilha |
| GET | `/api/excel/get-excel/` | Exporta em Excel |
| GET | `/api/excel/get-excel-json/` | Exporta em JSON |

## Tecnologias

Python · Django 5 · Django REST Framework · SimpleJWT · pandas · openpyxl · SQLite

## Estrutura

```
Relatorios/   # configurações do projeto
consultas/    # relatórios (views, service, repository)
excel/        # importação e exportação de planilhas
usuarios/     # cadastro e listagem de usuários
utils/        # conexão com o banco e resposta padrão
```

Cada app segue camadas de **view → service → repository**.

## Como rodar

```bash
git clone https://github.com/joao-lgtm/Relatorios.git
cd Relatorios
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Autor

**João Paulo Cassatti** · [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-paulo-283a551a2/)
