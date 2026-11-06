create DATABASE clinica character set utf8mb4;
use clinica;
ALTER TABLE consulta
MODIFY agenda_id INT NULL;

ALTER TABLE paciente MODIFY email VARCHAR(100) unique;
ALTER TABLE medico MODIFY email VARCHAR(100) unique;

create TABLE ESPECIALIDADE (
	id int auto_increment primary key,
    nome varchar(80) not null unique
    );
    
create TABLE MEDICO (
id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cpf CHAR(11) NOT NULL UNIQUE,
  crm VARCHAR(20) NOT NULL UNIQUE,
  matricula VARCHAR(20) NOT NULL UNIQUE,
  telefone VARCHAR(20),
  email VARCHAR(100),
  especialidade_id INT NOT NULL,
  FOREIGN KEY (especialidade_id) references ESPECIALIDADE(id)
);

create TABLE ENDERECO (
id int AUTO_INCREMENT PRIMARY KEY,
logradouro varchar(80) not null,
numero int not null,
complemento varchar(40), 
bairro VARCHAR(80), 
cidade VARCHAR(80), 
estado VARCHAR(40), 
CEP char(8), 
ponto_referencia VARCHAR (80)
);

create TABLE CONVENIO (
id int AUTO_INCREMENT PRIMARY KEY,
nome varchar(80) not null, 
CNPJ char(14) unique, 
tipo_plano varchar(80) not null
);

create TABLE PACIENTE (
id int AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(80) NOT NULL, 
CPF char(11) NOT NULL UNIQUE, 
data_nascimento DATE,
profissao varchar(80), 
telefone varchar(20) not null,
email varchar(100),
carteirinha varchar(30), 
convenio_id INT,
  FOREIGN KEY (convenio_id) references CONVENIO(id),
endereco_id INT NOT NULL UNIQUE,
  FOREIGN KEY (endereco_id) references ENDERECO(id)
  );
  
  
CREATE TABLE consultorio (
  id INT AUTO_INCREMENT PRIMARY KEY,
  identificacao VARCHAR(20) NOT NULL UNIQUE,
  nome VARCHAR(60) NOT NULL,
  andar INT
);

CREATE TABLE AGENDA (
	id INT AUTO_INCREMENT PRIMARY KEY,
	data date not null,
    hora_inicio time not null,
    hora_fim time not null ,
    status ENUM('livre','ocupado') NOT NULL DEFAULT 'livre',
    medico_id int NOT NULL,
    foreign key (medico_id) references MEDICO(id),
    unique (medico_id, data, hora_inicio)
    );
    
CREATE TABLE CONSULTA (
id INT AUTO_INCREMENT PRIMARY KEY,
data date not null,
horario time not null,
tipo ENUM('primeira','retorno') NOT NULL DEFAULT 'primeira',
status ENUM('agendada','realizada', 'cancelada') NOT NULL,
paciente_id int NOT NULL,
foreign key (paciente_id) references PACIENTE(id),
medico_id int NOT NULL,
    foreign key (medico_id) references MEDICO(id),
consultorio_id int NOT NULL,
foreign key (consultorio_id) references CONSULTORIO(id),
agenda_id int NOT NULL unique,
    foreign key (agenda_id) references AGENDA(id),
unique (paciente_id, data, horario)
);

CREATE TABLE PRONTUARIO (
id INT AUTO_INCREMENT PRIMARY KEY,
data_abertura date,
observacoes text,
paciente_id int NOT NULL unique,
foreign key (paciente_id) references PACIENTE(id)
);

CREATE TABLE ANAMNESE (
id INT AUTO_INCREMENT PRIMARY KEY,
queixa text,
sintomas text,
historico text,
prontuario_id int not null,
foreign key (prontuario_id) references PRONTUARIO(id),
consulta_id int not null unique,
foreign key (consulta_id) references CONSULTA(id)
);

CREATE TABLE EXAME (
id INT AUTO_INCREMENT PRIMARY KEY,
tipo varchar(100) not null,
data_solicitacao date not null,
status ENUM('solicitado','coletado', 'resultado_disponivel') NOT NULL DEFAULT 'solicitado',
consulta_id int not null,
foreign key (consulta_id) references CONSULTA(id),
resultado text
);

CREATE TABLE MEDICAMENTO (
id INT AUTO_INCREMENT PRIMARY KEY,
nome varchar(50) not null, 
principio_ativo varchar(50) not null,
fabricante varchar(50) not null
);

CREATE TABLE PRESCRICAO (
id INT AUTO_INCREMENT PRIMARY KEY,
data date not null,
observacoes text,
consulta_id int not null,
foreign key (consulta_id) references CONSULTA(id)
);

CREATE TABLE ITEM_PRESCRICAO (
id INT AUTO_INCREMENT PRIMARY KEY,
dosagem varchar(50) not null,
frequencia varchar(50) not null,
duracao varchar(50) not null,
prescricao_id int not null,
foreign key (prescricao_id) references PRESCRICAO(id),
medicamento_id int not null,
foreign key (medicamento_id) references MEDICAMENTO(id),
UNIQUE (medicamento_id, prescricao_id)
);

CREATE TABLE PAGAMENTO (
id INT AUTO_INCREMENT PRIMARY KEY,
data date,
valor DECIMAL(10,2) NOT NULL,
status ENUM('pago','nao_pago') NOT NULL DEFAULT 'nao_pago',
consulta_id int not null,
foreign key (consulta_id) references CONSULTA(id),
forma_pagamento ENUM('dinheiro', 'cartao_debito', 'cartao_credito', 'boleto', 'pix') NOT NULL
);





