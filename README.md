
#Documentação do Sistema de Contabilidade
#Introdução
O Sistema de Contabilidade é uma aplicação desenvolvida em Python que permite gerenciar o livro diário de uma empresa. Ele se conecta a um banco de dados PostgreSQL para armazenar e recuperar os lançamentos contábeis.

A aplicação consiste em uma interface gráfica implementada usando a biblioteca Tkinter, onde o usuário pode visualizar e atualizar os dados do livro diário.

#Requisitos do Sistema
Python 3.x instalado
Bibliotecas Python: psycopg2 e tkinter
Banco de dados PostgreSQL
Configuração do Banco de Dados
Antes de executar a aplicação, certifique-se de que você tenha um banco de dados PostgreSQL configurado. Siga as etapas a seguir para configurar o banco de dados:

Instale o PostgreSQL em seu sistema, se ainda não estiver instalado.

Crie um banco de dados chamado "contabilidade" no PostgreSQL.

Crie uma tabela chamada "LANCAMENTOS_CONTABEIS" com a seguinte estrutura:

sql
Copy code
CREATE TABLE LANCAMENTOS_CONTABEIS (
    COD_LANCAMENTO SERIAL PRIMARY KEY,
    DATA DATE,
    NUMERO_LANCAMENTO INTEGER,
    HISTORICO VARCHAR(255)
);
Crie uma tabela chamada "LIVRO_DIARIO" com a seguinte estrutura:

sql
Copy code
CREATE TABLE LIVRO_DIARIO (
    ID SERIAL PRIMARY KEY,
    COD_LANCAMENTO_CONTABIL INTEGER,
    COD_CONTA_DEBITO INTEGER,
    COD_CONTA_CREDITO INTEGER,
    VALOR NUMERIC(10,2),
    FOREIGN KEY (COD_LANCAMENTO_CONTABIL) REFERENCES LANCAMENTOS_CONTABEIS (COD_LANCAMENTO)
);
Insira alguns dados de exemplo na tabela "LANCAMENTOS_CONTABEIS" usando os comandos INSERT fornecidos anteriormente.

#Instalação e Execução
Siga as etapas a seguir para executar o Sistema de Contabilidade:

Clone o repositório do projeto para o seu sistema.

Abra um terminal e navegue até o diretório do projeto.

Instale as dependências do Python executando o seguinte comando:

bash
Copy code
pip install psycopg2 tkinter
Abra o arquivo Db.py e verifique se as informações de conexão com o banco de dados estão corretas (host, porta, nome do banco de dados, nome de usuário e senha).

Execute o arquivo Main.py usando o seguinte comando:

bash
Copy code
python Main.py
A interface gráfica do Sistema de Contabilidade será aberta. Você poderá visualizar os dados do livro diário e atualizá-los clicando no botão "Atualizar".

#Funcionalidades
Visualizar Livro Diário
Ao abrir o Sistema de Contabilidade, a interface gráfica exibirá os dados do livro diário obtidos do banco de dados.
Os dados são exibidos em uma listbox na janela principal da aplicação.
Atualizar Livro Diário
O usuário pode clicar no botão "Atualizar" para atualizar os dados do livro diário.
A função obter_livro_diario é chamada para recuperar os dados atualizados do banco de dados.
Os dados são exibidos na listbox após a atualização.
Estrutura do Código Fonte
Arquivo Db.py
Este arquivo contém a função create_connection para estabelecer a conexão com o banco de dados PostgreSQL. Ele retorna a conexão e o cursor para uso posterior.

Arquivo Main.py
Este arquivo contém a classe LivroDiarioApp que implementa a interface gráfica da aplicação usando a biblioteca Tkinter. Ele possui os seguintes métodos:

__init__(): Inicializa a aplicação, cria os elementos da interface e estabelece a conexão com o banco de dados.
atualizar_livro_diario(): Atualiza os dados do livro diário chamando a função obter_livro_diario e exibe os dados na listbox.
obter_livro_diario(): Recupera os dados do livro diário do banco de dados usando a conexão e o cursor fornecidos como argumentos.
main(): Função principal que cria a instância da classe LivroDiarioApp e inicia o loop principal da interface gráfica.
Considerações Finais
O Sistema de Contabilidade é uma aplicação simples que permite visualizar e atualizar os dados do livro diário de uma empresa. Ele fornece uma interface gráfica intuitiva para facilitar o uso. Você pode personalizar e expandir a funcionalidade da aplicação de acordo com suas necessidades específicas.

Lembre-se de manter as informações de conexão com o banco de dados atualizadas e protegidas, especialmente em um ambiente de produção.
