from validadores.tipo_validador import validar_string
from datetime import datetime
from repositorios import area_repositorio, cultura_repositorio

def validar_id_plantio(id):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
        return None
    except ValueError:
        return "ID inválido!"

def validar_pegar_plantio_por_id(id):
    return validar_id_plantio(id)

def validar_criar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input):
    if not validar_string(nome) or not nome.strip():
        return "O nome do plantio não pode estar vazio"
    
    if not validar_string(observacao) or not observacao.strip():
        return "A observação do plantio não pode estar vazia"
    
    if not validar_string(area_id) or not area_id.strip():
        return "O ID da área não pode estar vazio"
    
    if not validar_string(cultura_id) or not cultura_id.strip():
        return "O ID da cultura não pode estar vazio"
    
    # Verificar se a área existe
    area = area_repositorio.pegar_por_id(area_id)
    if area is None:
        return "A área especificada não existe"
    
    # Verificar se a cultura existe
    cultura = cultura_repositorio.pegar_por_id(cultura_id)
    if cultura is None:
        return "A cultura especificada não existe"
    
    if not validar_string(data_plantio_input) or not data_plantio_input.strip():
        return "A data de plantio não pode estar vazia"
    
    try:
        datetime.strptime(data_plantio_input, '%Y-%m-%d')
    except ValueError:
        return "A data de plantio deve estar no formato YYYY-MM-DD"
    
    return None

def validar_atualizar_plantio(id, nome, observacao, area_id, cultura_id, data_plantio_input):
    erro_id = validar_id_plantio(id)
    if erro_id:
        return erro_id
    
    return validar_criar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input)

def validar_deletar_plantio(id):
    return validar_id_plantio(id)