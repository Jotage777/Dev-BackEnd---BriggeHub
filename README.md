# Dev-BackEnd---BridgeHub

## 👤Desenvolvedor


| Nome                                              | GitHub                                           | Ativo | Atribuições                   |
| ------------------------------------------------- | -------------------------------------------      | ----- | ----------------------------- |
| João Gabriel                                      | [João Gabriel](https://github.com/Jotage777)     | 🔥    | BackEnd                       |

## ⚓ Links

👉 [Git do backend](https://github.com/Jotage777/Dev-BackEnd---BriggeHub) <br />

## Sobre o projeto

O objetivo desse projeto é desenvolver uma api em flask para realização do teste pratico da empressa Bridgehub

## Tecnologias que serão utilizadas
- Python
- SqLlite
- Flask
- Regex

## Banco de dados e suas versões

Estou usando o banco de dados sql que é criado localmente assim que iniciamos a api.

Primeira versão
- Usuario -- (Nome, email e telefone)

Segunda versão

Essa versão contamos com o upgrade do banco de dados para o adicionar o endereço do usuário
- Usuario -- (Nome, email e telefone)
- Endereco -- (cep, lougradoro, complemento, bairro, localidade,uf,ibge,gia,ddd,siafi) -> Upgrade

Terceira versão

Essa versão vamos adicionar uma tabela TESTE ao banco de dados para em seguida removela e assim realizar o downgrade no banco de dados

- Usuario -- (Nome, email e telefone)
- Endereco -- (cep, lougradoro, complemento, bairro, localidade,uf,ibge,gia,ddd,siafi) -> Upgrade
- Teste -- (ID) upgrade/downgrade

Menu para a realização das migrations

👉 [Menu](https://github.com/Jotage777/Dev-BackEnd---BriggeHub/blob/main/Menu_migrations.py) <br />

## Endpoints

## Adicionar Usuario
- http://127.0.0.1:5000/bridgehub/add_user
- Json = {
            "nome":"",
            "email":"",
            "telefone":""
	      }
## Consultar todos os usuários do banco de dados
- http://127.0.0.1:5000/bridgehub/users
- Obs: Quando a tabela Endereço for adicionada ao banco de dados, vai ser retornado o endereço do usuário

## Consultar dados de um usuário especifico
- http://127.0.0.1:5000/bridgehub/users/<int:id>
- id = id do usuário disponivel no banco de dados
- Obs: Quando a tabela Endereço for adicionada ao banco de dados, vai ser retornado o endereço do usuário

## Editar dados do usuário
- http://127.0.0.1:5000/bridgehub/edit_user/<int:id>
- Json = {
            "nome":"",
            "email":"",
            "telefone":""
	      }
- id = id do usuário disponivel no banco de dados

## Deletar usuário
- http://127.0.0.1:5000/bridgehub/delete_user/<int:id>

## Enviar email
- http://127.0.0.1:5000/bridgehub/send_email
- Json = {
          "assunto":"",
          "destinatario":"",
          "mensagem":""
	          }
- A variável mensagem deve ser algum endpoint de consulta
- id = id do usuário disponivel no banco de dados
- É necessario que utilize um email do gmail e a senha criada para aplicativos.
- Como obter a senha para aplicativo: Segurança -> Como fazer login do google -> senha de app
- O email e a senha devem ser colocados nas variáveis EMAIL_ADDRESS e EMAIL_PASSWORD no .py abaixo
- 👉 [Arquivo](https://github.com/Jotage777/Dev-BackEnd---BriggeHub/blob/main/Api_BridgeHub.py) <br />

## Adicionar cep
- http://127.0.0.1:5000/bridgehub/cep/<int:id>
- Json = {
          "cep":""
        }
- id = id do usuário disponivel no banco de dados

## Editar cep
- http://127.0.0.1:5000/bridgehub/editar_cep/<int:id>
- Json = {
          "cep":""
        }
 - id = id do usuário disponivel no banco de dados

## Obrigado pela oportunidade 
