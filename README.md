# Sistema de Gestão de Clínica

Aplicação de linha de comando desenvolvida em Python para gerenciar cadastros e operações de uma clínica, com persistência em MySQL.

## Funcionalidades

- Cadastro, listagem, exclusão e consulta de histórico/resumo de pacientes.
- Cadastro, listagem e exclusão de médicos.
- Cadastro de horários de agenda, consulta de horários livres e agendamento, cancelamento e conclusão de consultas.
- Gestão de prontuários, anamneses, exames e prescrições.
- Criação e acompanhamento de pagamentos.
- Cadastro e listagem de especialidades, convênios, consultórios e medicamentos.

## Tecnologias

- Python
- MySQL
- `mysql-connector-python`
- `python-dotenv`

## Pré-requisitos

- Python instalado.
- MySQL Server em execução e acessível.
- Um cliente MySQL, como o MySQL Workbench, para criar e preparar o banco.

## Instalação e configuração

Execute os comandos a partir da pasta raiz do projeto.

1. (Opcional) Crie e ative um ambiente virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instale as dependências:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Configure o banco de dados usando [`BD2_PROJETO.sql`](./BD2_PROJETO.sql). O script cria o banco `clinica` e as tabelas necessárias, mas **não pode ser executado diretamente em um banco vazio na ordem atual**: os comandos `ALTER TABLE` aparecem antes da criação das tabelas.

   Para preparar uma instalação limpa:

   - Execute `CREATE DATABASE clinica CHARACTER SET utf8mb4;` e `USE clinica;` (ou selecione um banco já criado).
   - Execute os comandos `CREATE TABLE` do script na ordem em que aparecem.
   - Execute os três comandos `ALTER TABLE` que estão no início do arquivo, depois que as tabelas correspondentes existirem.

4. Crie o arquivo local de configuração a partir do exemplo:

   ```powershell
   Copy-Item Clinica\.env.example Clinica\.env
   ```

   Edite `Clinica\.env` e informe as credenciais do seu MySQL:

   ```dotenv
   DB_HOST=localhost
   DB_NAME=clinica
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   ```

   `DB_USER` e `DB_PASSWORD` são obrigatórios. `DB_HOST` e `DB_NAME` são opcionais e, se omitidos, assumem `localhost` e `clinica`. O módulo [`Clinica/banco.py`](./Clinica/banco.py) carrega esse arquivo automaticamente; variáveis já definidas no ambiente do sistema têm precedência. O `.env` real é ignorado pelo Git, enquanto o `.env.example` pode ser compartilhado.

5. Inicie o sistema:

   ```powershell
   python app.py
   ```

## Estrutura do projeto

```text
.
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
├── BD2_PROJETO.sql
└── Clinica/
    ├── .env.example
    ├── banco.py
    ├── crud.py
    ├── init.py
    └── menu.py
```

- `app.py`: ponto de entrada da aplicação.
- `Clinica/banco.py`: carrega a configuração e implementa acesso ao MySQL.
- `Clinica/crud.py`: operações de consulta e manipulação dos dados.
- `Clinica/menu.py`: menus e interação pelo terminal.
- `Clinica/init.py`: módulo de inicialização do pacote.
- `BD2_PROJETO.sql`: criação e ajustes do esquema do banco.
- `requirements.txt`: dependências Python.

## Segurança e privacidade

Não colocar senhas ou credenciais do tipo no código nem em arquivos versionados. Mantenha os valores reais em `Clinica\.env` ou em variáveis de ambiente protegidas. Como o sistema pode armazenar dados pessoais e informações de saúde, é recomendado utilizar dados fictícios em demonstrações e proteger os ambientes com dados reais.
