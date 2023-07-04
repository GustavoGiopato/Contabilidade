# Sistema de Contabilidade

O Sistema de Contabilidade é uma aplicação desenvolvida em Python que permite gerenciar o livro diário de uma empresa. Ele se conecta a um banco de dados PostgreSQL para armazenar e recuperar os lançamentos contábeis.

## Funcionalidades

- Visualizar o livro diário com informações sobre os lançamentos contábeis, incluindo data, número de lançamento, histórico e detalhes de débito e crédito.
- Atualizar o livro diário com novos lançamentos contábeis.

## Requisitos do Sistema

- Python 3.x instalado
- Bibliotecas Python: `psycopg2` e `tkinter`
- Banco de dados PostgreSQL

## Configuração do Banco de Dados

Antes de executar a aplicação, certifique-se de que você tenha um banco de dados PostgreSQL configurado. Siga as etapas a seguir para configurar o banco de dados:

1. Instale o PostgreSQL em seu sistema, se ainda não estiver instalado.
2. Crie um banco de dados chamado "contabilidade" no PostgreSQL.
3. Crie uma tabela chamada "LANCAMENTOS_CONTABEIS" com a seguinte estrutura:

   ```sql
   CREATE TABLE LANCAMENTOS_CONTABEIS (
       COD_LANCAMENTO SERIAL PRIMARY KEY,
       DATA DATE,
       NUMERO_LANCAMENTO INTEGER,
       HISTORICO VARCHAR(255)
   );
   ```

4. Crie uma tabela chamada "LIVRO_DIARIO" com a seguinte estrutura:

   ```sql
   CREATE TABLE LIVRO_DIARIO (
       ID SERIAL PRIMARY KEY,
       COD_LANCAMENTO_CONTABIL INTEGER,
       COD_CONTA_DEBITO INTEGER,
       COD_CONTA_CREDITO INTEGER,
       VALOR NUMERIC(10,2),
       FOREIGN KEY (COD_LANCAMENTO_CONTABIL) REFERENCES LANCAMENTOS_CONTABEIS (COD_LANCAMENTO)
   );
   ```

5. Insira alguns dados de exemplo na tabela "LANCAMENTOS_CONTABEIS" usando os comandos INSERT fornecidos anteriormente.

## Instalação e Execução

Siga as etapas a seguir para executar o Sistema de Contabilidade:

1. Clone o repositório do projeto para o seu sistema.
2. Abra um terminal e navegue até o diretório do projeto.
3. Instale as dependências do Python executando o seguinte comando:

   ```bash
   pip install psycopg2 tkinter
   ```

4. Abra o arquivo `Db.py` e verifique se as informações de conexão com o banco de dados estão corretas (host, porta, nome do banco de dados, nome de usuário e senha).
5. Execute o arquivo `Main.py` usando o seguinte comando:

   ```bash
   python Main.py
   ```

6. A interface gráfica do Sistema de Contabilidade será aberta. Você poderá visualizar os dados do livro diário e atualizá-los clicando no botão "Atualizar".

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma melhoria ou correção para o projeto, sinta-se à vontade para enviar uma solicitação de pull.

## Licença

Este projeto está licenciado sob a [MIT License](https://github.com/seu-usuario/seu-repositorio/blob/main/LICENSE).
