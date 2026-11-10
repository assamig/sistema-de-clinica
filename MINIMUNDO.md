# Mini-mundo do projeto: Sistema de Gestão de Clínica

## Visão geral
Este projeto simula o funcionamento de uma clínica médica digital, onde pacientes, médicos, consultas e pagamentos são registrados em um banco de dados MySQL. A aplicação em Python oferece um menu no terminal para controlar o dia a dia da clínica.

## Personagens e entidades do sistema

### 1. Paciente
- É o cliente da clínica.
- Possui dados pessoais, endereço, telefone, e-mail, profissão e convênio.
- Pode ter histórico de consultas e prontuário.
- Exemplo: João da Silva, que marca uma consulta com um cardiologista.

### 2. Médico
- É o profissional responsável pelo atendimento.
- Possui nome, CPF, CRM, matrícula, telefone, e-mail e especialidade.
- Cada médico trabalha em uma especialidade, como clínica geral, ortopedia ou cardiologia.
- Exemplo: Dra. Ana Souza, especialista em cardiologia.

### 3. Especialidade
- Define a área de atuação do médico.
- Exemplo: cardiologia, pediatria, dermatologia, ginecologia.

### 4. Consultório
- Local físico onde a consulta acontece.
- Possui identificação, nome, andar e relação com o atendimento.
- Exemplo: Consultório 201, bloco A.

### 5. Agenda
- Representa os horários disponíveis do médico.
- Pode estar em status "livre" ou "ocupado".
- A agenda impede conflito de horários para o mesmo médico.
- Exemplo: Dr. Carlos tem agenda em 15/11 às 09:00.

### 6. Consulta
- É o evento principal do sistema.
- Relaciona paciente, médico, consultório e agenda.
- Possui data, horário, tipo (primeira ou retorno), status (agendada, realizada, cancelada).
- Exemplo: consulta do paciente João com a Dra. Ana em 15/11 às 10:00.

### 7. Prontuário
- Guarda o histórico clínico do paciente.
- Contém observações gerais e é único por paciente.
- Exemplo: o prontuário de Maria registra alergias e tratamentos anteriores.

### 8. Anamnese
- Descreve queixa, sintomas e histórico do paciente.
- Está vinculada a um prontuário e a uma consulta específica.
- Exemplo: queixa de febre e dor abdominal.

### 9. Exame
- É solicitado durante a consulta.
- Pode estar em status "solicitado", "coletado" ou "resultado_disponivel".
- Exemplo: exame de sangue solicitado na consulta do paciente.

### 10. Medicamento e prescrição
- Medicamentos são cadastrados com nome, princípio ativo e fabricante.
- A prescrição reúne medicamentos, dosagem, frequência e duração.
- Exemplo: "Amoxicilina 500mg, 1 cápsula de 12 em 12 horas por 7 dias".

### 11. Pagamento
- Registra o valor da consulta e o status do pagamento.
- Tempo de espera e formas de pagamento: dinheiro, cartão, boleto e pix.
- Exemplo: pagamento em pix da consulta do paciente.

### 12. Convênio
- Representa o plano de saúde ou instituição responsável.
- Pode ser associado ao paciente.
- Exemplo: Unimed, SulAmérica, Bradesco Saúde.

## Fluxo principal do sistema

1. O paciente entra na clínica e realiza cadastro.
2. O médico é cadastrado com sua especialidade.
3. A clínica cria a agenda e horários do médico.
4. O paciente agenda uma consulta.
5. O médico atende o paciente e registra dados da consulta.
6. O prontuário, a anamnese e os exames são atualizados.
7. O médico pode prescrever medicamentos.
8. O paciente paga pela consulta.
9. O sistema gera histórico para consultas futuras.

## Regras de negócio importantes
- Cada paciente deve ter um endereço único.
- Cada médico deve ter uma especialidade obrigatória.
- Um médico não pode ter dois horários iguais na mesma data.
- Uma consulta não pode ter o mesmo paciente no mesmo horário e data.
- Cada prontuário pertence a apenas um paciente.
- O pagamento está ligado diretamente à consulta.

## Estrutura do projeto
O projeto é organizado em camadas:

- `app.py`: ponto de entrada da aplicação.
- `Clinica/banco.py`: conexão com o banco MySQL.
- `Clinica/crud.py`: operações de cadastro, leitura e manipulação.
- `Clinica/menu.py`: interface textual do sistema.
- `BD2_PROJETO.sql`: criação do banco e tabelas.

## Mundo em uma frase
A clínica é um pequeno ecossistema em que pacientes buscam cuidados, médicos organizam atendimentos, consultas geram registros e pagamentos fecham o ciclo de atendimento.

## Exemplo de cenário
- Paciente: Lucas Pereira
- Médico: Dr. Eduardo Rocha
- Especialidade: cardiologia
- Consulta: 20/11, 14:00, retorno
- Exame: eletrocardiograma
- Pagamento: cartão de crédito

Esse cenário representa um fluxo real dentro do sistema da clínica.
