from validadores.tipo_validador import validar_string, validar_decimal
from datetime import datetime
from repositorios import plantio_repositorio

def validar_id_irrigacao(id):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
        return None
    except ValueError:
        return "ID inválido!"

def validar_pegar_irrigacao_por_id(id):
    return validar_id_irrigacao(id)

def validar_criar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input):
    if not validar_string(plantio_id) or not plantio_id.strip():
        return "O ID do plantio não pode estar vazio"
    
    plantio = plantio_repositorio.pegar_por_id(plantio_id)
    if plantio is None:
        return "O plantio especificado não existe"
    
    if not validar_string(data_irrigacao_input) or not data_irrigacao_input.strip():
        return "A data de irrigação não pode estar vazia"
    
    try:
        datetime.strptime(data_irrigacao_input, '%Y-%m-%d')
    except ValueError:
        return "A data de irrigação deve estar no formato YYYY-MM-DD"
    
    if not volume_agua_l_input.strip():
        return "O volume de água não pode estar vazio"
    try:
        volume_agua_l = float(volume_agua_l_input)
        if not validar_decimal(volume_agua_l) or volume_agua_l <= 0:
            return "O volume de água deve ser um número positivo"
    except ValueError:
        return "O volume de água deve ser um número válido"
    
    return None

def validar_atualizar_irrigacao(id, plantio_id, data_irrigacao_input, volume_agua_l_input):
    erro_id = validar_id_irrigacao(id)
    if erro_id:
        return erro_id
    
    return validar_criar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input)

def validar_deletar_irrigacao(id):
    return validar_id_irrigacao(id)