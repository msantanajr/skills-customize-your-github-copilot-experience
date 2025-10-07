# 🚀 Construindo APIs REST com FastAPI

## 🎯 Objetivo
Aprender a criar uma API REST simples utilizando o framework FastAPI em Python, praticando conceitos de rotas, métodos HTTP e manipulação de dados.

## 📝 Tarefas

### 1. Criar uma API de Gerenciamento de Itens
**Descrição:**
Implemente uma API REST que permita cadastrar, listar, atualizar e remover itens de uma lista (ex: produtos, tarefas, livros, etc).

**Requisitos:**
- Utilizar o framework FastAPI
- Implementar rotas para:
  - Listar todos os itens (`GET /items`)
  - Adicionar um novo item (`POST /items`)
  - Atualizar um item existente (`PUT /items/{id}`)
  - Remover um item (`DELETE /items/{id}`)
- Utilizar um dicionário ou lista em memória para armazenar os itens
- Retornar respostas em formato JSON
- Documentação automática disponível em `/docs`

**Exemplo de execução:**
```bash
$ uvicorn main:app --reload
```
Acesse: http://localhost:8000/docs

Exemplo de requisição para adicionar um item:
```json
POST /items
{
  "nome": "Livro de Python",
  "preco": 49.90
}
```

Resposta esperada:
```json
{
  "id": 1,
  "nome": "Livro de Python",
  "preco": 49.90
}
```
