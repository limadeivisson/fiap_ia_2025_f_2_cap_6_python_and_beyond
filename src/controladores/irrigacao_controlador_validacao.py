from validadores.tipo_validador import validar_string, validar_decimal
from datetime import datetime
from repositorios import plantio_repositorio

def validar_id(id, msg = "ID inválido!"):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
    except ValueError:
        raise Exception(msg)

def validar_pegar_irrigacao_por_id(id):
    validar_id(id)

def validar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input):
    validar_id(plantio_id, "O ID do plantio inválido!")
    plantio = plantio_repositorio.pegar_por_id(plantio_id)
    if plantio is None:
        raise Exception("O plantio especificado não existe")
    if not validar_string(data_irrigacao_input) or not data_irrigacao_input.strip():
        raise Exception("A data de irrigação não pode estar vazia")
    try:
        datetime.strptime(data_irrigacao_input, '%Y-%m-%d')
    except ValueError:
        raise Exception("A data de irrigação deve estar no formato YYYY-MM-DD")
    if not volume_agua_l_input.strip():
        raise Exception("O volume de água não pode estar vazio")
    try:
        volume_agua_l = float(volume_agua_l_input)
        if not validar_decimal(volume_agua_l) or volume_agua_l <= 0:
            raise Exception("O volume de água deve ser um número positivo")
    except ValueError:
        raise Exception("O volume de água deve ser um número válido")
    
def validar_atualizar_irrigacao(id, plantio_id, data_irrigacao_input, volume_agua_l_input):
    validar_id(id)
    validar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input)

def validar_deletar_irrigacao(id):
    validar_id(id)