from validadores.tipo_validador import validar_string, validar_decimal

def validar_id(id, msg="ID inválido!"):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
    except ValueError:
        raise Exception(msg)

def validar_pegar_feedback_por_id(id):
    validar_id(id)

def validar_feedback(cultura_id, message_feedback, tips, percent_input):
    validar_id(cultura_id, "ID da cultura inválido!")
    if not validar_string(message_feedback) or not message_feedback.strip():
        raise Exception("A mensagem do feedback não pode estar vazia")
    if not validar_string(tips) or not tips.strip():
        raise Exception("As dicas não podem estar vazias")
    if not percent_input.strip():
        raise Exception("A porcentagem não pode estar vazia")
    try:
        percent = float(percent_input)
        if not validar_decimal(percent) or percent < 0 or percent > 100:
            raise Exception("A porcentagem deve ser um número entre 0 e 100")
    except ValueError:
        raise Exception("A porcentagem deve ser um número válido")

def validar_atualizar_feedback(id, cultura_id, message_feedback, tips, percent_input):
    validar_id(id)
    validar_feedback(cultura_id, message_feedback, tips, percent_input)

def validar_deletar_feedback(id):
    return validar_id(id)