# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprender a criar uma API REST simples utilizando o framework FastAPI em Python. O estudante irá praticar conceitos de rotas, métodos HTTP, manipulação de dados e execução de servidor local.

## 📝 Tasks

### 🛠️ Criar estrutura básica de API

#### Description
Implemente um servidor FastAPI com pelo menos duas rotas: uma rota GET que retorna uma mensagem de boas-vindas e uma rota POST que recebe dados em formato JSON.

#### Requirements
Completed program should:

- Iniciar um servidor FastAPI local
- Ter uma rota GET `/` que retorna um JSON com mensagem de boas-vindas
- Ter uma rota POST `/items` que recebe um item (ex: nome e preço) e retorna o mesmo item com um campo extra `id`

### 🛠️ Manipular lista de itens na memória

#### Description
Permita que a API armazene itens recebidos em uma lista na memória e forneça uma rota para listar todos os itens cadastrados.

#### Requirements
Completed program should:

- Armazenar itens recebidos via POST em uma lista
- Ter uma rota GET `/items` que retorna todos os itens cadastrados
- Cada item deve ter um campo `id` único

