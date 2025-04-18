from validadores.tipo_validador import validar_string, validar_decimal

def validar_id_cultura(id):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
        return None
    except ValueError:
        return "ID inválido!"

def validar_pegar_cultura_por_id(id):
    return validar_id_cultura(id)

def validar_criar_cultura(nome, consumo_hidrico_diario_l_m2_input):
    if not validar_string(nome) or not nome.strip():
        return "O nome da cultura não pode estar vazio"
    if not consumo_hidrico_diario_l_m2_input.strip():
        return "O consumo hídrico diário não pode estar vazio"
    try:
        consumo_hidrico_diario_l_m2 = float(consumo_hidrico_diario_l_m2_input)
        if not validar_decimal(consumo_hidrico_diario_l_m2) or consumo_hidrico_diario_l_m2 <= 0:
            return "O consumo hídrico diário deve ser um número positivo"
    except ValueError:
        return "O consumo hídrico diário deve ser um número válido"
    return None

def validar_atualizar_cultura(id, nome, consumo_hidrico_diario_l_m2_input):
    erro_id = validar_id_cultura(id)
    if erro_id:
        return erro_id
    return validar_criar_cultura(nome, consumo_hidrico_diario_l_m2_input)

def validar_deletar_cultura(id):
    return validar_id_cultura(id)