from validadores.tipo_validador import validar_string, validar_decimal

def validar_id_cultura(id):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
    except ValueError:
        raise Exception("ID inválido!")

def validar_pegar_cultura_por_id(id):
    validar_id_cultura(id)

def validar_criar_cultura(nome, consumo_hidrico_diario_l_m2_input):
    if not validar_string(nome) or not nome.strip():
        raise Exception("O nome da cultura não pode estar vazio")
    if not consumo_hidrico_diario_l_m2_input.strip():
        raise Exception("O consumo hídrico diário não pode estar vazio")
    try:
        consumo_hidrico_diario_l_m2 = float(consumo_hidrico_diario_l_m2_input)
        if not validar_decimal(consumo_hidrico_diario_l_m2) or consumo_hidrico_diario_l_m2 <= 0:
            raise Exception("O consumo hídrico diário deve ser um número positivo")
    except ValueError:
        raise Exception("O consumo hídrico diário deve ser um número válido")

def validar_atualizar_cultura(id, nome, consumo_hidrico_diario_l_m2_input):
    validar_id_cultura(id)
    validar_criar_cultura(nome, consumo_hidrico_diario_l_m2_input)

def validar_deletar_cultura(id):
    validar_id_cultura(id)