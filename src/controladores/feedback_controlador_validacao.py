from validadores.tipo_validador import validar_string, validar_decimal

def validar_id_feedback(id):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
        return None
    except ValueError:
        return "ID inválido!"

def validar_cultura_id(cultura_id):
    try:
        int(cultura_id)
        if not cultura_id.strip() or len(cultura_id.strip()) > 50:
            raise ValueError()
        return None
    except ValueError:
        return "ID da cultura inválido!"

def validar_pegar_feedback_por_id(id):
    return validar_id_feedback(id)

def validar_criar_feedback(cultura_id, message_feedback, tips, percent_input):
    erro_cultura = validar_cultura_id(cultura_id)
    if erro_cultura:
        return erro_cultura

    if not validar_string(message_feedback) or not message_feedback.strip():
        return "A mensagem do feedback não pode estar vazia"

    if not validar_string(tips) or not tips.strip():
        return "As dicas não podem estar vazias"
        
    if not percent_input.strip():
        return "A porcentagem não pode estar vazia"
        
    try:
        percent = float(percent_input)
        if not validar_decimal(percent) or percent < 0 or percent > 100:
            return "A porcentagem deve ser um número entre 0 e 100"
    except ValueError:
        return "A porcentagem deve ser um número válido"
    
    return None

def validar_atualizar_feedback(id, cultura_id, message_feedback, tips, percent_input):
    erro_id = validar_id_feedback(id)
    if erro_id:
        return erro_id

    return validar_criar_feedback(cultura_id, message_feedback, tips, percent_input)

def validar_deletar_feedback(id):
    return validar_id_feedback(id)