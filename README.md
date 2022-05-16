# Desafio Resale

Autor: Pedro Morais (pedrolukasmorais@gmail.com, https://www.linkedin.com/in/pedrolmorais/)

## Motivação

Esse é um software desenvolvido para o desafio. O programa foi desenvolvido utilizando a linguagem python juntamente com o framework Flask. O framework foi escolhido pois é facilmente manipulado para aplicações web e para banco de dados foi utilizado o MONGODB.

## Requisitos

- docker (versão recomendada: 19.03)
- docker-compose (versão recomendada: 1.27)

## Instalação

```bash
docker-compose up --build
```

### Servidor: 
```bash
localhost:8083
```

## Pendências e melhorias
- Lógica e agregração de listagem portal <- Pendências
- Inclusão de testes <- Pendências
- Utilizar SQL <- Melhoria
- Refatoração de códigos duplicatos <- Melhoria


# Documentação da API

#### Criar novo imóvel

```http
  POST /property/create
```

| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `property_id` | `int` |
| `name` | `str` |
| `address` | `str` |
| `description` | `str` |
| `status` | `bool` |
| `type` | `str` |
| `purpose` | `str` |
| `evaluated_value` | `float` |
| `property_value` | `float` |


#### Atualizar imóvel

```http
  PUT property/update/<property_id>"
```

| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `property_id` | `int` |
| `name` | `str` |
| `address` | `str` |
| `description` | `str` |
| `status` | `bool` |
| `type` | `str` |
| `purpose` | `str` |
| `evaluated_value` | `float` |
| `property_value` | `float` |


#### Pegar Imovel por ID

```http
  GET /property/<property_id>
```

#### Deletar Imovel por ID

```http
  DELETE property/delete/<property_id>
```

====================================================================================

#### Criar novo canal de venda

```http
  POST /sales_channel/create
```

| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `sales_channel_id` | `int` |
| `name` | `str` |
| `type_sales_channel` | `str` |

#### Atualizar canal de venda

```http
  PUT /sales_channel/update/<sales_channel_id>
```

| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `name` | `str` |
| `type_sales_channel` | `str` |

#### Pegar Canal de venda por ID

```http
  GET /sales_channel/<sales_channel_id>
```

#### Deletar Imovel por ID

```http
  DELETE /sales_channel/delete/<sales_channel_id>
```
====================================================================================

#### Criar nova carteira
```http
  POST /wallet_listing/create
```

| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `wallet_listing_id` | `int` |
| `name` | `str` |
| `type` | `str` |
| `commission` | `float` |
| `sales_channel_id` | `int` |

#### Atualizar carteira

```http
  PUT /wallet_listing/update/<wallet_listing_id>
```

| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `name` | `str` |
| `type` | `str` |
| `commission` | `float` |
| `sales_channel_id` | `int` |

#### Pegar carteira por ID

```http
  GET /wallet_listing/<wallet_listing_id>
```

#### Deletar carteira ID

```http
  DELETE /wallet_listing/delete/<wallet_listing_id>
```

====================================================================================

#### Associar carteira x imóvel
```http
  POST /portal/associate
```

| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `property_id` | `int` |
| `wallet_listing_id` | `int` |

#### Pegar Listagem Portal
```http
  GET /portal/list
```
