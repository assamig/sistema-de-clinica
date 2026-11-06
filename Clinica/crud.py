from datetime import date, timedelta
from .banco import conectar, consultar, executar
import mysql

#CRUD DE ESPECIALIDADE
def criar_especialidade(especialidade_nome):
    novo_id, _ = executar(
        "INSERT INTO especialidade (nome) VALUES (%s)",
        (especialidade_nome, ))
    return novo_id

def atualizar_especialidade(especialidade_id, nova_especialidade):
    _, linhas = executar(
        "UPDATE especialidade SET nome = %s WHERE id = %s", (nova_especialidade, especialidade_id)
        )
    return linhas

def deletar_especialidade(especialidade_id):
    _, linhas = executar("DELETE FROM especialidade WHERE id = %s", (especialidade_id,))
    return linhas

def listar_especialidades():
    return consultar("SELECT * FROM especialidade")


#CRUD DE CONVENIOS
def criar_convenio(nome, cnpj, tipo_plano):
    novo_id, _ = executar(
        "INSERT INTO convenio (nome, CNPJ, tipo_plano) VALUES (%s, %s, %s)",
        (nome, cnpj, tipo_plano))
    return novo_id

def atualizar_convenio(convenio_id, novo_nome, cnpj, tipo_plano):
    _, linhas = executar(
        "UPDATE convenio SET nome = %s, CNPJ = %s, tipo_plano = %s WHERE id = %s", (novo_nome, cnpj, tipo_plano, convenio_id)
        )
    return linhas


def deletar_convenio(convenio_id):
    _, linhas = executar("DELETE FROM convenio WHERE id = %s", (convenio_id,))
    return linhas

def listar_convenios():
    return consultar("SELECT * FROM convenio")

#CRUD DE ENDEREÇO
def criar_endereco(logradouro, numero, complemento, bairro, cidade, estado, CEP, ponto_referencia):
    novo_id, _ = executar(
        "INSERT INTO endereco (logradouro, numero, complemento, bairro, cidade, estado, CEP, ponto_referencia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (logradouro, numero, complemento, bairro, cidade, estado, CEP, ponto_referencia))
    return novo_id

def atualizar_endereco(endereco_id, logradouro, numero, complemento, bairro, cidade, estado, CEP, ponto_referencia ):
    _, linhas = executar(
        "UPDATE endereco SET logradouro = %s, numero = %s, complemento = %s, bairro = %s, cidade = %s, estado = %s, CEP = %s, ponto_referencia = %s WHERE id = %s", (logradouro, numero, complemento, bairro, cidade, estado, CEP, ponto_referencia , endereco_id)
        )
    return linhas

def deletar_endereco(endereco_id):
    _, linhas = executar("DELETE FROM endereco WHERE id = %s", (endereco_id,))
    return linhas

def listar_enderecos():
    return consultar("SELECT * FROM endereco")

#CRUD DE CONSULTORIO

def criar_consultorio(identificacao, nome, andar):
    novo_id, _ = executar(
        "INSERT INTO consultorio (identificacao, nome, andar) VALUES (%s, %s, %s)",
        (identificacao, nome, andar))
    return novo_id

def atualizar_consultorio(consultorio_id, identificacao, nome, andar):
    _, linhas = executar(
        "UPDATE consultorio SET identificacao = %s, nome = %s, andar = %s WHERE id = %s", ( identificacao, nome, andar, consultorio_id)
        )
    return linhas

def deletar_consultorio(consultorio_id):
    _, linhas = executar("DELETE FROM consultorio WHERE id = %s", (consultorio_id,))
    return linhas

def listar_consultorios():
    return consultar("SELECT * FROM consultorio")

#CRUD DE MEDICAMENTO

def criar_medicamento(nome, principio_ativo, fabricante):
    novo_id, _ = executar(
        "INSERT INTO medicamento (nome, principio_ativo, fabricante) VALUES (%s, %s, %s)",
        (nome, principio_ativo, fabricante))
    return novo_id

def atualizar_medicamento(medicamento_id, nome, principio_ativo, fabricante):
    _, linhas = executar(
        "UPDATE medicamento SET nome = %s, principio_ativo = %s, fabricante = %s WHERE id = %s", (nome, principio_ativo, fabricante, medicamento_id)
        )
    return linhas

def deletar_medicamento(medicamento_id):
    _, linhas = executar("DELETE FROM medicamento WHERE id = %s", (medicamento_id,))
    return linhas

def listar_medicamentos():
    return consultar("SELECT * FROM medicamento")

#CRUD DE MÉDICO

def criar_medico(nome, cpf, crm, matricula, telefone, email, especialidade_id):
    novo_id, _ = executar(
        "INSERT INTO medico (nome, cpf, crm, matricula, telefone, email, especialidade_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (nome, cpf, crm, matricula, telefone, email, especialidade_id))
    return novo_id

def atualizar_medico(medico_id, nome, cpf, crm, matricula, telefone, email, especialidade_id):
    _, linhas = executar(
        "UPDATE medico SET nome = %s, cpf = %s, crm = %s, matricula = %s, telefone = %s, email = %s, especialidade_id = %s WHERE id = %s", (nome, cpf, crm, matricula, telefone, email, especialidade_id, medico_id)
        )
    return linhas


def deletar_medico(medico_id):
    _, linhas = executar("DELETE FROM medico WHERE id = %s", (medico_id,))
    return linhas

def listar_medicos():
    return consultar("""
        SELECT m.id, m.nome, m.crm, e.nome AS especialidade
        FROM medico m
        JOIN especialidade e ON e.id = m.especialidade_id
    """)

#CRUD DE PACIENTES


def criar_paciente(nome, cpf, data_nascimento, profissao, telefone, email, carteirinha, convenio_id, endereco_id):
    novo_id, _ = executar(
        "INSERT INTO paciente (nome, cpf, data_nascimento, profissao, telefone, email, carteirinha, convenio_id, endereco_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (nome, cpf, data_nascimento, profissao, telefone, email, carteirinha, convenio_id, endereco_id))
    return novo_id

def atualizar_paciente(paciente_id, nome, cpf, data_nascimento, profissao, telefone, email, carteirinha, convenio_id, endereco_id):
    _, linhas = executar(
        "UPDATE paciente SET nome = %s, cpf = %s, data_nascimento = %s, profissao = %s, telefone = %s, email = %s, carteirinha = %s, convenio_id = %s, endereco_id = %s WHERE id = %s", (nome, cpf, data_nascimento, profissao, telefone, email, carteirinha, convenio_id, endereco_id, paciente_id)
        )
    return linhas


def deletar_paciente(paciente_id):
    _, linhas = executar("DELETE FROM paciente WHERE id = %s", (paciente_id,))
    return linhas

def trocar_convenio_paciente(paciente_id, novo_convenio_id):
    _, linhas = executar(
        "UPDATE paciente SET convenio_id = %s WHERE id  = %s", (novo_convenio_id, paciente_id)
        )
    return linhas

def listar_pacientes():
    return consultar("""
        SELECT p.id, p.nome AS paciente, p.cpf,
               c.nome AS convenio, e.cidade
        FROM paciente p
        LEFT JOIN convenio c ON c.id = p.convenio_id
        JOIN endereco e ON e.id = p.endereco_id
    """)

#AGENDA
def criar_agenda(medico_id, data, hora_inicio, hora_fim):
    if hora_fim <= hora_inicio:
        print("A hora final precisa ser depois da inicial.")
        return None
    novo_id, _ = executar(
        "INSERT INTO agenda (data, hora_inicio, hora_fim, medico_id) VALUES (%s, %s, %s, %s)",
        (data, hora_inicio, hora_fim, medico_id))
    return novo_id

def listar_agenda_livre(medico_id):
    return consultar("""
        SELECT id, data, hora_inicio, hora_fim
        FROM agenda
        WHERE medico_id = %s AND status = 'livre'
        ORDER BY data, hora_inicio
    """, (medico_id,))

# PARTE DE CONSULTA 
def agendar_consulta(paciente_id, agenda_id, consultorio_id, tipo="primeira"):
    conexao = conectar()
    cursor = conexao.cursor(buffered=True)
    try:
        # FOR UPDATE = "cadeado" na linha até o fim da transação
        cursor.execute(
            "SELECT medico_id, data, hora_inicio, status FROM agenda WHERE id = %s FOR UPDATE",
            (agenda_id,))
        horario = cursor.fetchone()
        if horario is None:
            print("Horário não existe.")
            return None
        medico_id, data, hora, status = horario
        if status != "livre":
            print("Horário já está ocupado.")
            return None

        # regra: paciente não pode ter 2 consultas ativas no mesmo dia e hora
        cursor.execute(
            """SELECT COUNT(*) FROM consulta
               WHERE paciente_id = %s AND data = %s AND horario = %s
                 AND status <> 'cancelada'""",
            (paciente_id, data, hora))
        if cursor.fetchone()[0] > 0:
            print("Paciente já tem consulta nesse dia e horário.")
            return None

        cursor.execute(
            """INSERT INTO consulta
               (data, horario, tipo, status, paciente_id, medico_id, consultorio_id, agenda_id)
               VALUES (%s, %s, %s, 'agendada', %s, %s, %s, %s)""",
            (data, hora, tipo, paciente_id, medico_id, consultorio_id, agenda_id))
        consulta_id = cursor.lastrowid

        cursor.execute("UPDATE agenda SET status = 'ocupado' WHERE id = %s", (agenda_id,))
        conexao.commit()          # as DUAS mudanças viram definitivas juntas
        return consulta_id
    except mysql.connector.Error as erro:
        conexao.rollback()
        print("Erro:", erro)
        return None
    finally:
        cursor.close()
        conexao.close()

def cancelar_consulta(consulta_id):
    conexao = conectar()
    cursor = conexao.cursor(buffered=True)
    try:
        cursor.execute(
            "SELECT agenda_id, status FROM consulta WHERE id = %s FOR UPDATE",
            (consulta_id,))
        consulta = cursor.fetchone()
        if consulta is None:
            print("Consulta não existe.")
            return 0
        agenda_id, status = consulta
        if status != "agendada":
            print(f"Só dá pra cancelar consulta agendada (status atual: {status}).")
            return 0

        cursor.execute(
            "UPDATE consulta SET status = 'cancelada', agenda_id = NULL WHERE id = %s",
            (consulta_id,))
        cursor.execute("UPDATE agenda SET status = 'livre' WHERE id = %s", (agenda_id,))
        conexao.commit()
        return 1
    except mysql.connector.Error as erro:
        conexao.rollback()
        print("Erro:", erro)
        return 0
    finally:
        cursor.close()
        conexao.close()

def concluir_consulta(consulta_id):
    _, linhas = executar(
        "UPDATE consulta SET status = 'realizada' WHERE id = %s AND status = 'agendada'",
        (consulta_id,))
    return linhas

def listar_consultas():
    return consultar("""
        SELECT c.id, c.data, c.horario,
               p.nome AS paciente, m.nome AS medico, c.status
        FROM consulta c
        JOIN paciente p ON p.id = c.paciente_id
        JOIN medico m ON m.id = c.medico_id
        ORDER BY c.data, c.horario
    """)


#PRONTUÁRIO
def criar_prontuario(paciente_id, observacoes=None):
    novo_id, _ = executar(
        "INSERT INTO prontuario (data_abertura, observacoes, paciente_id) VALUES (CURDATE(), %s, %s)",
        (observacoes, paciente_id))
    return novo_id

def atualizar_prontuario(prontuario_id, observacoes):
    _, linhas = executar(
        "UPDATE prontuario SET observacoes = %s WHERE id = %s", (observacoes, prontuario_id))
    return linhas

def listar_prontuarios():
    return consultar("""
        SELECT pr.id, p.nome AS paciente, pr.data_abertura, pr.observacoes
        FROM prontuario pr
        JOIN paciente p ON p.id = pr.paciente_id
    """)

#ANAMNESE
def criar_anamnese(consulta_id, queixa, sintomas, historico):
    # o prontuario é descoberto pela consulta, então nunca fica de outro paciente
    novo_id, linhas = executar(
        """INSERT INTO anamnese (queixa, sintomas, historico, prontuario_id, consulta_id)
           SELECT %s, %s, %s, pr.id, c.id
           FROM consulta c
           JOIN prontuario pr ON pr.paciente_id = c.paciente_id
           WHERE c.id = %s""",
        (queixa, sintomas, historico, consulta_id))
    if linhas == 0:
        print("Consulta inexistente ou paciente sem prontuário.")
        return None
    return novo_id

def atualizar_anamnese(anamnese_id, queixa, sintomas, historico):
    _, linhas = executar(
        "UPDATE anamnese SET queixa = %s, sintomas = %s, historico = %s WHERE id = %s",
        (queixa, sintomas, historico, anamnese_id))
    return linhas

def listar_anamneses():
    return consultar("""
        SELECT a.id, p.nome AS paciente, c.data, a.queixa, a.sintomas, a.historico
        FROM anamnese a
        JOIN consulta c ON c.id = a.consulta_id
        JOIN paciente p ON p.id = c.paciente_id
        ORDER BY c.data
    """)

#EXAME
def criar_exame(consulta_id, tipo):
    novo_id, _ = executar(
        "INSERT INTO exame (tipo, data_solicitacao, consulta_id) VALUES (%s, CURDATE(), %s)",
        (tipo, consulta_id))
    return novo_id

def atualizar_status_exame(exame_id, status, resultado=None):
    if status == "resultado_disponivel" and not resultado:
        print("Informe o resultado/laudo.")
        return 0
    _, linhas = executar(
        "UPDATE exame SET status = %s, resultado = %s WHERE id = %s",
        (status, resultado, exame_id))
    return linhas

def listar_exames():
    return consultar("""
        SELECT e.id, p.nome AS paciente, e.tipo, e.data_solicitacao, e.status, e.resultado
        FROM exame e
        JOIN consulta c ON c.id = e.consulta_id
        JOIN paciente p ON p.id = c.paciente_id
    """)

#PRESCRIÇÃO E ITENS 
def criar_prescricao(consulta_id, observacoes=None):
    novo_id, _ = executar(
        "INSERT INTO prescricao (data, observacoes, consulta_id) VALUES (CURDATE(), %s, %s)",
        (observacoes, consulta_id))
    return novo_id

def adicionar_item_prescricao(prescricao_id, medicamento_id, dosagem, frequencia, duracao):
    novo_id, _ = executar(
        """INSERT INTO item_prescricao
           (dosagem, frequencia, duracao, prescricao_id, medicamento_id)
           VALUES (%s, %s, %s, %s, %s)""",
        (dosagem, frequencia, duracao, prescricao_id, medicamento_id))
    return novo_id

def atualizar_prescricao(prescricao_id, observacoes):
    _, linhas = executar(
        "UPDATE prescricao SET observacoes = %s WHERE id = %s", (observacoes, prescricao_id))
    return linhas

def listar_prescricoes():
    return consultar("""
        SELECT pr.id, p.nome AS paciente, pr.data, pr.observacoes
        FROM prescricao pr
        JOIN consulta c ON c.id = pr.consulta_id
        JOIN paciente p ON p.id = c.paciente_id
    """)

def listar_itens_prescricao(prescricao_id):
    return consultar("""
        SELECT i.id, m.nome AS medicamento, i.dosagem, i.frequencia, i.duracao
        FROM item_prescricao i
        JOIN medicamento m ON m.id = i.medicamento_id
        WHERE i.prescricao_id = %s
    """, (prescricao_id,))

#PAGAMENTO 
def criar_pagamento(consulta_id, valor, forma_pagamento):
    novo_id, _ = executar(
        "INSERT INTO pagamento (valor, forma_pagamento, consulta_id) VALUES (%s, %s, %s)",
        (valor, forma_pagamento, consulta_id))
    return novo_id

def registrar_pagamento(pagamento_id):
    _, linhas = executar(
        "UPDATE pagamento SET status = 'pago', data = CURDATE() WHERE id = %s AND status = 'nao_pago'",
        (pagamento_id,))
    return linhas

def listar_pagamentos():
    return consultar("""
        SELECT pg.id, p.nome AS paciente, pg.valor, pg.forma_pagamento, pg.status, pg.data
        FROM pagamento pg
        JOIN consulta c ON c.id = pg.consulta_id
        JOIN paciente p ON p.id = c.paciente_id
    """)

#Função de formatação já que o python devolve os valores de datetime e time do mysql como objetos
#Os valorres são formatados para serem exibidos no terminal como data e hora comum
def formatar_valor(v):
    if isinstance(v, timedelta):                      # hora
        horas, resto = divmod(int(v.total_seconds()), 3600)
        return f"{horas:02d}:{resto // 60:02d}"
    if isinstance(v, date):                           # data
        return v.strftime("%d/%m/%Y")
    if v is None:                                     # vazio
        return "-"
    return v

def formatar_linha(linha):
    return tuple(formatar_valor(v) for v in linha)

#Função que já formata automaticamente as linhas que aparecerem pela chamada da função original
def listar_agendas_livres_formatadas(medico_id):
    return [
        formatar_linha(linha)
        for linha in listar_agenda_livre(medico_id)
    ]
def listar_consultas_formatadas():
    return [formatar_linha(linhas) for linhas in listar_consultas()]

def listar_exames_formatados():
    return [formatar_linha(linhas) for linhas in listar_exames()]

def listar_prescricao_formatada():
    return [formatar_linha(linhas) for linhas in listar_prescricoes()]

def listar_anamneses_formatadas():
    return [formatar_linha(linhas) for linhas in listar_anamneses()]

#Funções de histórico e relatórios

def historico_consultas(paciente_id):
    return consultar("""
        SELECT c.id, c.data, c.horario, m.nome AS medico,
               e.nome AS especialidade, c.tipo, c.status
        FROM consulta c
        JOIN medico m ON m.id = c.medico_id
        JOIN especialidade e ON e.id = m.especialidade_id
        WHERE c.paciente_id = %s
        ORDER BY c.data DESC, c.horario DESC
    """, (paciente_id,))

def historico_consultas_formatado(paciente_id):
    return [formatar_linha(linhas) for linhas in historico_consultas(paciente_id)]

def historico_exames(paciente_id):
    return consultar("""
        SELECT e.id, e.tipo, e.data_solicitacao, e.resultado,
               p.nome AS paciente, e.status
        FROM exame e
        JOIN consulta c ON e.consulta_id = c.id
        JOIN paciente p ON c.paciente_id = p.id
        WHERE p.id = %s
        ORDER BY e.data_solicitacao DESC
    """, (paciente_id,))

def historico_exames_formatados(paciente_id):
    return [formatar_linha(linhas) for linhas in historico_exames(paciente_id)]

def historico_prescricoes(paciente_id):
    return consultar("""
        SELECT pr.id, pr.data, pr.observacoes, m.nome,
        i.dosagem, i.frequencia, i.duracao, p.nome AS paciente
        FROM prescricao pr
        JOIN consulta c ON c.id = pr.consulta_id
        JOIN paciente p ON p.id = c.paciente_id
        JOIN item_prescricao i ON i.prescricao_id = pr.id
        JOIN medicamento m ON m.id = i.medicamento_id
        WHERE p.id = %s
        ORDER BY pr.data DESC
    """, (paciente_id,))

def historico_prescricoes_formatadas(paciente_id):
    return [formatar_linha(linhas) for linhas in historico_prescricoes(paciente_id)]

def pagamentos_pendentes(paciente_id):
    return consultar("""
    SELECT pa.id, pa.status, pa.valor, p.nome, c.data
    FROM pagamento pa
    JOIN consulta c ON c.id = pa.consulta_id
    JOIN paciente p ON p.id = c.paciente_id
    WHERE pa.status = 'nao_pago' AND p.id = %s
    ORDER BY c.data DESC
""", (paciente_id,))


def pagamentos_pendentes_formatados(paciente_id):
    return [formatar_linha(linhas) for linhas in pagamentos_pendentes(paciente_id)]

def resumo_paciente(paciente_id):
    return consultar("""
        SELECT p.id, p.nome, COUNT(DISTINCT c.id), COUNT(DISTINCT e.id)
        FROM paciente p
        LEFT JOIN consulta c ON c.paciente_id = p.id
        LEFT JOIN exame e ON e.consulta_id = c.id
        WHERE p.id = %s
        GROUP BY p.id
        """, (paciente_id, ))
