from datetime import datetime
from decimal import Decimal, InvalidOperation

from .crud import (
    adicionar_item_prescricao,
    agendar_consulta,
    atualizar_status_exame,
    cancelar_consulta,
    concluir_consulta,
    criar_anamnese,
    criar_consultorio,
    criar_convenio,
    criar_endereco,
    criar_especialidade,
    criar_exame,
    criar_medicamento,
    criar_medico,
    criar_pagamento,
    criar_paciente,
    criar_prontuario,
    criar_prescricao,
    criar_agenda,
    deletar_medico,
    deletar_paciente,
    listar_agenda_livre,
    listar_anamneses,
    listar_consultas,
    listar_consultorios,
    listar_convenios,
    listar_especialidades,
    listar_exames,
    listar_medicos,
    listar_medicamentos,
    listar_pagamentos,
    listar_pacientes,
    listar_prontuarios,
    listar_prescricoes,
    listar_itens_prescricao,
    pagamentos_pendentes,
    historico_consultas,
    historico_exames,
    historico_prescricoes,
    resumo_paciente,
    registrar_pagamento,
    formatar_linha,
)


def ler_inteiro(mensagem, minimo=1):
    while True:
        texto = input(mensagem).strip()
        try:
            valor = int(texto)
            if valor >= minimo:
                return valor
        except ValueError:
            pass
        print(f"Digite um número inteiro maior ou igual a {minimo}.")


def ler_texto(mensagem, obrigatorio=True):
    while True:
        texto = input(mensagem).strip()
        if texto or not obrigatorio:
            return texto or None
        print("Este campo é obrigatório.")


def ler_cpf(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto.isdigit() and len(texto) == 11:
            return texto
        print("CPF inválido. Digite os 11 números, sem pontuação.")


def ler_cep(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto.isdigit() and len(texto) == 8:
            return texto
        print("CEP inválido. Digite os 8 números, sem pontuação.")


def ler_data(mensagem):
    while True:
        texto = input(f"{mensagem} (dd/mm/aaaa): ").strip()
        try:
            return datetime.strptime(texto, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print("Data inválida.")


def ler_hora(mensagem):
    while True:
        texto = input(f"{mensagem} (hh:mm): ").strip()
        try:
            return datetime.strptime(texto, "%H:%M").strftime("%H:%M:%S")
        except ValueError:
            print("Horário inválido.")


def ler_valor(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            valor = Decimal(texto)
            if valor > 0:
                return valor
        except InvalidOperation:
            pass
        print("Digite um valor monetário maior que zero.")


def ler_opcao(mensagem, opcoes):
    opcoes_validas = {str(opcao) for opcao in opcoes}
    while True:
        opcao = input(mensagem).strip().lower()
        if opcao in opcoes_validas:
            return opcao
        print("Opção inválida.")


def mostrar_registros(registros):
    if not registros:
        print("Nenhum registro encontrado.")
        return
    for registro in registros:
        print(formatar_linha(registro))


def selecionar_registro(titulo, registros):
    mostrar_registros(registros)
    if not registros:
        return None
    return ler_inteiro(f"{titulo} (digite o ID): ")


def confirmar(mensagem):
    return ler_opcao(f"{mensagem} (s/n): ", ("s", "n")).lower() == "s"


def cadastrar_paciente_tela():
    print("\n--- CADASTRAR PACIENTE ---")
    nome = ler_texto("Nome: ")
    cpf = ler_cpf("CPF: ")
    data_nascimento = ler_data("Data de nascimento")
    profissao = ler_texto("Profissão (opcional): ", obrigatorio=False)
    telefone = ler_texto("Telefone: ")
    email = ler_texto("E-mail (opcional): ", obrigatorio=False)

    convenios = listar_convenios()
    convenio_id = None
    carteirinha = None
    if convenios:
        print("\nConvênios disponíveis:")
        mostrar_registros(convenios)
        escolha = input("ID do convênio (Enter para particular): ").strip()
        if escolha:
            try:
                convenio_id = int(escolha)
                if convenio_id not in {linha[0] for linha in convenios}:
                    print("Convênio não encontrado; cadastro cancelado.")
                    return
                carteirinha = ler_texto("Número da carteirinha: ")
            except ValueError:
                print("ID inválido; cadastro cancelado.")
                return

    print("\nEndereço do paciente:")
    logradouro = ler_texto("Logradouro: ")
    numero = ler_inteiro("Número: ")
    complemento = ler_texto("Complemento (opcional): ", obrigatorio=False)
    bairro = ler_texto("Bairro (opcional): ", obrigatorio=False)
    cidade = ler_texto("Cidade (opcional): ", obrigatorio=False)
    estado = ler_texto("Estado (opcional): ", obrigatorio=False)
    cep = ler_cep("CEP: ")
    ponto_referencia = ler_texto("Ponto de referência (opcional): ", obrigatorio=False)

    endereco_id = criar_endereco(
        logradouro, numero, complemento, bairro, cidade, estado, cep, ponto_referencia
    )
    if endereco_id is None:
        print("Não foi possível cadastrar o endereço; paciente não cadastrado.")
        return

    paciente_id = criar_paciente(
        nome, cpf, data_nascimento, profissao, telefone, email,
        carteirinha, convenio_id, endereco_id,
    )
    if paciente_id is not None:
        print(f"Paciente cadastrado com ID {paciente_id}.")


def menu_pacientes():
    while True:
        print("\n--- PACIENTES ---")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Excluir paciente")
        print("4. Ver histórico e resumo")
        print("0. Voltar")
        opcao = ler_opcao("Escolha: ", ("0", "1", "2", "3", "4"))

        if opcao == "1":
            cadastrar_paciente_tela()
        elif opcao == "2":
            mostrar_registros(listar_pacientes())
        elif opcao == "3":
            paciente_id = selecionar_registro("ID do paciente para excluir", listar_pacientes())
            if paciente_id and confirmar("Confirma a exclusão?"):
                print("Paciente excluído." if deletar_paciente(paciente_id) else "Paciente não encontrado ou não pode ser excluído.")
        elif opcao == "4":
            paciente_id = selecionar_registro("ID do paciente", listar_pacientes())
            if paciente_id:
                print("\nResumo:")
                mostrar_registros(resumo_paciente(paciente_id))
                print("\nConsultas:")
                mostrar_registros(historico_consultas(paciente_id))
                print("\nExames:")
                mostrar_registros(historico_exames(paciente_id))
                print("\nPrescrições:")
                mostrar_registros(historico_prescricoes(paciente_id))
                print("\nPagamentos pendentes:")
                mostrar_registros(pagamentos_pendentes(paciente_id))
        else:
            return


def cadastrar_medico_tela():
    especialidades = listar_especialidades()
    especialidade_id = selecionar_registro("ID da especialidade", especialidades)
    if especialidade_id is None or especialidade_id not in {linha[0] for linha in especialidades}:
        if not especialidades:
            print("Cadastre uma especialidade antes de cadastrar o médico.")
        else:
            print("Especialidade inválida.")
        return

    nome = ler_texto("Nome do médico: ")
    cpf = ler_cpf("CPF: ")
    crm = ler_texto("CRM: ")
    matricula = ler_texto("Matrícula: ")
    telefone = ler_texto("Telefone (opcional): ", obrigatorio=False)
    email = ler_texto("E-mail (opcional): ", obrigatorio=False)
    medico_id = criar_medico(nome, cpf, crm, matricula, telefone, email, especialidade_id)
    if medico_id is not None:
        print(f"Médico cadastrado com ID {medico_id}.")


def menu_medicos():
    while True:
        print("\n--- MÉDICOS ---")
        print("1. Cadastrar médico")
        print("2. Listar médicos")
        print("3. Excluir médico")
        print("0. Voltar")
        opcao = ler_opcao("Escolha: ", ("0", "1", "2", "3"))
        if opcao == "1":
            cadastrar_medico_tela()
        elif opcao == "2":
            mostrar_registros(listar_medicos())
        elif opcao == "3":
            medico_id = selecionar_registro("ID do médico para excluir", listar_medicos())
            if medico_id and confirmar("Confirma a exclusão?"):
                print("Médico excluído." if deletar_medico(medico_id) else "Médico não encontrado ou não pode ser excluído.")
        else:
            return


def menu_agenda_consultas():
    while True:
        print("\n--- AGENDA E CONSULTAS ---")
        print("1. Criar horário na agenda")
        print("2. Listar horários livres de um médico")
        print("3. Agendar consulta")
        print("4. Listar consultas")
        print("5. Cancelar consulta")
        print("6. Marcar consulta como realizada")
        print("0. Voltar")
        opcao = ler_opcao("Escolha: ", ("0", "1", "2", "3", "4", "5", "6"))

        if opcao == "1":
            medico_id = selecionar_registro("ID do médico", listar_medicos())
            if medico_id:
                data = ler_data("Data")
                inicio = ler_hora("Hora inicial")
                fim = ler_hora("Hora final")
                agenda_id = criar_agenda(medico_id, data, inicio, fim)
                if agenda_id is not None:
                    print(f"Horário criado com ID {agenda_id}.")
        elif opcao == "2":
            medico_id = selecionar_registro("ID do médico", listar_medicos())
            if medico_id:
                mostrar_registros(listar_agenda_livre(medico_id))
        elif opcao == "3":
            paciente_id = selecionar_registro("ID do paciente", listar_pacientes())
            if not paciente_id:
                continue
            medico_id = selecionar_registro("ID do médico", listar_medicos())
            if not medico_id:
                continue
            horarios = listar_agenda_livre(medico_id)
            agenda_id = selecionar_registro("ID do horário", horarios)
            if agenda_id is None or agenda_id not in {linha[0] for linha in horarios}:
                if horarios:
                    print("Horário inválido.")
                continue
            consultorios = listar_consultorios()
            consultorio_id = selecionar_registro("ID do consultório", consultorios)
            if consultorio_id is None or consultorio_id not in {linha[0] for linha in consultorios}:
                if consultorios:
                    print("Consultório inválido.")
                continue
            tipo = ler_opcao("Tipo (1 - primeira consulta, 2 - retorno): ", ("1", "2"))
            consulta_id = agendar_consulta(
                paciente_id, agenda_id, consultorio_id,
                "primeira" if tipo == "1" else "retorno",
            )
            if consulta_id is not None:
                print(f"Consulta agendada com ID {consulta_id}.")
        elif opcao == "4":
            mostrar_registros(listar_consultas())
        elif opcao == "5":
            consulta_id = selecionar_registro("ID da consulta", listar_consultas())
            if consulta_id and confirmar("Confirma o cancelamento?"):
                print("Consulta cancelada." if cancelar_consulta(consulta_id) else "Não foi possível cancelar a consulta.")
        elif opcao == "6":
            consulta_id = selecionar_registro("ID da consulta", listar_consultas())
            if consulta_id:
                print("Consulta concluída." if concluir_consulta(consulta_id) else "Consulta não encontrada ou não está agendada.")
        else:
            return


def menu_prontuarios_e_atendimentos():
    while True:
        print("\n--- PRONTUÁRIOS E ATENDIMENTOS ---")
        print("1. Criar prontuário para paciente")
        print("2. Listar prontuários")
        print("3. Registrar anamnese")
        print("4. Listar anamneses")
        print("5. Solicitar exame")
        print("6. Atualizar exame/resultado")
        print("7. Listar exames")
        print("8. Criar prescrição")
        print("9. Adicionar medicamento a uma prescrição")
        print("10. Listar prescrições")
        print("11. Listar itens de prescrição")
        print("0. Voltar")
        opcao = ler_opcao("Escolha: ", tuple(str(i) for i in range(12)))

        if opcao == "1":
            paciente_id = selecionar_registro("ID do paciente", listar_pacientes())
            if paciente_id:
                observacoes = ler_texto("Observações iniciais (opcional): ", obrigatorio=False)
                prontuario_id = criar_prontuario(paciente_id, observacoes)
                if prontuario_id is not None:
                    print(f"Prontuário criado com ID {prontuario_id}.")
        elif opcao == "2":
            mostrar_registros(listar_prontuarios())
        elif opcao == "3":
            consulta_id = selecionar_registro("ID da consulta", listar_consultas())
            if consulta_id:
                queixa = ler_texto("Queixa: ")
                sintomas = ler_texto("Sintomas: ")
                historico = ler_texto("Histórico: ")
                anamnese_id = criar_anamnese(consulta_id, queixa, sintomas, historico)
                if anamnese_id is not None:
                    print(f"Anamnese registrada com ID {anamnese_id}.")
        elif opcao == "4":
            mostrar_registros(listar_anamneses())
        elif opcao == "5":
            consulta_id = selecionar_registro("ID da consulta", listar_consultas())
            if consulta_id:
                exame_id = criar_exame(consulta_id, ler_texto("Tipo de exame: "))
                if exame_id is not None:
                    print(f"Exame solicitado com ID {exame_id}.")
        elif opcao == "6":
            exames = listar_exames()
            exame_id = selecionar_registro("ID do exame", exames)
            if exame_id is not None and exame_id in {linha[0] for linha in exames}:
                status = ler_opcao(
                    "Status (1 - solicitado, 2 - coletado, 3 - resultado disponível): ",
                    ("1", "2", "3"),
                )
                resultado = None
                if status == "3":
                    resultado = ler_texto("Resultado/laudo: ")
                valores = {"1": "solicitado", "2": "coletado", "3": "resultado_disponivel"}
                print("Exame atualizado." if atualizar_status_exame(
                    exame_id, valores[status], resultado
                ) else "Não foi possível atualizar o exame.")
        elif opcao == "7":
            mostrar_registros(listar_exames())
        elif opcao == "8":
            consulta_id = selecionar_registro("ID da consulta", listar_consultas())
            if consulta_id:
                observacoes = ler_texto("Observações (opcional): ", obrigatorio=False)
                prescricao_id = criar_prescricao(consulta_id, observacoes)
                if prescricao_id is not None:
                    print(f"Prescrição criada com ID {prescricao_id}.")
        elif opcao == "9":
            prescricoes = listar_prescricoes()
            prescricao_id = selecionar_registro("ID da prescrição", prescricoes)
            if prescricao_id is None or prescricao_id not in {linha[0] for linha in prescricoes}:
                continue
            medicamentos = listar_medicamentos()
            medicamento_id = selecionar_registro("ID do medicamento", medicamentos)
            if medicamento_id is None or medicamento_id not in {linha[0] for linha in medicamentos}:
                continue
            item_id = adicionar_item_prescricao(
                prescricao_id, medicamento_id,
                ler_texto("Dosagem: "), ler_texto("Frequência: "), ler_texto("Duração: "),
            )
            if item_id is not None:
                print(f"Medicamento adicionado com ID {item_id}.")
        elif opcao == "10":
            mostrar_registros(listar_prescricoes())
        elif opcao == "11":
            prescricoes = listar_prescricoes()
            prescricao_id = selecionar_registro("ID da prescrição", prescricoes)
            if prescricao_id and prescricao_id in {linha[0] for linha in prescricoes}:
                mostrar_registros(listar_itens_prescricao(prescricao_id))
        else:
            return


def menu_pagamentos():
    formas = {
        "1": "dinheiro",
        "2": "cartao_debito",
        "3": "cartao_credito",
        "4": "boleto",
        "5": "pix",
    }
    while True:
        print("\n--- PAGAMENTOS ---")
        print("1. Gerar pagamento para consulta")
        print("2. Listar pagamentos")
        print("3. Registrar pagamento recebido")
        print("0. Voltar")
        opcao = ler_opcao("Escolha: ", ("0", "1", "2", "3"))
        if opcao == "1":
            consulta_id = selecionar_registro("ID da consulta", listar_consultas())
            if consulta_id:
                print("1. Dinheiro  2. Cartão de débito  3. Cartão de crédito  4. Boleto  5. Pix")
                forma = ler_opcao("Forma de pagamento: ", formas)
                pagamento_id = criar_pagamento(consulta_id, ler_valor("Valor: R$ "), formas[forma])
                if pagamento_id is not None:
                    print(f"Pagamento criado com ID {pagamento_id}.")
        elif opcao == "2":
            mostrar_registros(listar_pagamentos())
        elif opcao == "3":
            pagamentos = listar_pagamentos()
            pagamento_id = selecionar_registro("ID do pagamento", pagamentos)
            if pagamento_id and pagamento_id in {linha[0] for linha in pagamentos}:
                print("Pagamento registrado." if registrar_pagamento(pagamento_id) else "Pagamento não encontrado ou já recebido.")
        else:
            return


def menu_cadastros():
    while True:
        print("\n--- CADASTROS DE APOIO ---")
        print("1. Cadastrar/listar especialidades")
        print("2. Cadastrar/listar convênios")
        print("3. Cadastrar/listar consultórios")
        print("4. Cadastrar/listar medicamentos")
        print("0. Voltar")
        opcao = ler_opcao("Escolha: ", ("0", "1", "2", "3", "4"))
        if opcao == "1":
            print("\nEspecialidades:")
            mostrar_registros(listar_especialidades())
            if confirmar("Deseja cadastrar uma especialidade?"):
                especialidade_id = criar_especialidade(ler_texto("Nome: "))
                if especialidade_id is not None:
                    print(f"Especialidade cadastrada com ID {especialidade_id}.")
        elif opcao == "2":
            print("\nConvênios:")
            mostrar_registros(listar_convenios())
            if confirmar("Deseja cadastrar um convênio?"):
                nome = ler_texto("Nome: ")
                cnpj = input("CNPJ (14 dígitos; Enter se não informado): ").strip()
                if cnpj and (not cnpj.isdigit() or len(cnpj) != 14):
                    print("CNPJ inválido.")
                    continue
                tipo_plano = ler_texto("Tipo do plano: ")
                convenio_id = criar_convenio(nome, cnpj or None, tipo_plano)
                if convenio_id is not None:
                    print(f"Convênio cadastrado com ID {convenio_id}.")
        elif opcao == "3":
            print("\nConsultórios:")
            mostrar_registros(listar_consultorios())
            if confirmar("Deseja cadastrar um consultório?"):
                identificacao = ler_texto("Identificação: ")
                nome = ler_texto("Nome: ")
                andar = ler_inteiro("Andar: ", minimo=0)
                consultorio_id = criar_consultorio(identificacao, nome, andar)
                if consultorio_id is not None:
                    print(f"Consultório cadastrado com ID {consultorio_id}.")
        elif opcao == "4":
            print("\nMedicamentos:")
            mostrar_registros(listar_medicamentos())
            if confirmar("Deseja cadastrar um medicamento?"):
                nome = ler_texto("Nome: ")
                principio_ativo = ler_texto("Princípio ativo: ")
                fabricante = ler_texto("Fabricante: ")
                medicamento_id = criar_medicamento(nome, principio_ativo, fabricante)
                if medicamento_id is not None:
                    print(f"Medicamento cadastrado com ID {medicamento_id}.")
        else:
            return


def menu_principal():
    while True:
        print("\n========== SISTEMA DE CLÍNICA ==========")
        print("1. Pacientes")
        print("2. Médicos")
        print("3. Agenda e consultas")
        print("4. Prontuários e atendimentos")
        print("5. Pagamentos")
        print("6. Cadastros de apoio")
        print("0. Sair")
        opcao = ler_opcao("Escolha uma opção: ", ("0", "1", "2", "3", "4", "5", "6"))
        if opcao == "1":
            menu_pacientes()
        elif opcao == "2":
            menu_medicos()
        elif opcao == "3":
            menu_agenda_consultas()
        elif opcao == "4":
            menu_prontuarios_e_atendimentos()
        elif opcao == "5":
            menu_pagamentos()
        elif opcao == "6":
            menu_cadastros()
        else:
            print("Até logo!")
            return


if __name__ == "__main__":
    menu_principal()
