from validadores.tipo_validador import validar_string
from datetime import datetime
from repositorios import area_repositorio, cultura_repositorio

def validar_id(id, msg = "ID inválido!"):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
    except ValueError:
        raise ValueError(msg)

def validar_pegar_plantio_por_id(id):
    validar_id(id)

def validar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input):
    validar_id(area_id, "O ID da área é inválido!")
    validar_id(cultura_id, "O ID da cultura é inválido!")
    if not validar_string(nome) or not nome.strip():
        raise Exception("O nome do plantio não pode estar vazio")
    if not validar_string(observacao) or not observacao.strip():
        raise Exception("A observação do plantio não pode estar vazia")
    area = area_repositorio.pegar_por_id(area_id)
    if area is None:
        raise Exception("A área especificada não existe")
    cultura = cultura_repositorio.pegar_por_id(cultura_id)
    if cultura is None:
        raise Exception("A cultura especificada não existe")
    if not validar_string(data_plantio_input) or not data_plantio_input.strip():
        raise Exception("A data de plantio não pode estar vazia")
    try:
        datetime.strptime(data_plantio_input, '%Y-%m-%d')
    except ValueError:
        raise Exception("A data de plantio deve estar no formato YYYY-MM-DD")

def validar_atualizar_plantio(id, nome, observacao, area_id, cultura_id, data_plantio_input):
    validar_id(id)
    validar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input)

def validar_deletar_plantio(id):
    validar_id(id)