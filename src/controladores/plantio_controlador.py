from repositorios import plantio_repositorio
from controladores.plantio_controlador_validacao import *
import pandas as pd
from datetime import datetime

def pegar_plantios():
    plantios = plantio_repositorio.pegar()
    if plantios is None:
        raise Exception("Erro ao buscar plantios")
    plantios_formatados = [{
        'id': plantio[0],
        'nome': plantio[1],
        'observacao': plantio[2],
        'area': plantio[4],
        'cultura': plantio[6],
        'data_plantio': plantio[7].strftime('%Y-%m-%d')
    } for plantio in plantios]
    df = pd.DataFrame(plantios_formatados)
    return df.to_string(index=False)

def pegar_plantio_por_id(id):
    validar_pegar_plantio_por_id(id)
    plantio = plantio_repositorio.pegar_por_id(id)
    if plantio is None:
        raise Exception("Plantio não encontrado")
    plantio_formatado = {
        'id': plantio[0],
        'nome': plantio[1],
        'observacao': plantio[2],
        'area': plantio[4],
        'cultura': plantio[6],
        'data_plantio': plantio[7].strftime('%Y-%m-%d')
    }
    df = pd.DataFrame([plantio_formatado])
    return df.to_string(index=False)

def criar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input):
    validar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input)
    data_plantio = datetime.strptime(data_plantio_input, '%Y-%m-%d')
    id_plantio = plantio_repositorio.criar(nome, observacao, area_id, cultura_id, data_plantio)
    if id_plantio:
        plantio = plantio_repositorio.pegar_por_id(id_plantio[0])
        plantio_formatado = {
            'id': plantio[0],
            'nome': plantio[1],
            'observacao': plantio[2],
            'area': plantio[4],
            'cultura': plantio[6],
            'data_plantio': plantio[7].strftime('%Y-%m-%d')
        }
        df = pd.DataFrame([plantio_formatado])
        return df.to_string(index=False)
    else:
        raise Exception("Erro ao criar plantio")

def atualizar_plantio_por_id(id, nome, observacao, area_id, cultura_id, data_plantio_input):
    validar_atualizar_plantio(id, nome, observacao, area_id, cultura_id, data_plantio_input)
    plantio = plantio_repositorio.pegar_por_id(id)
    if plantio is None:
        raise Exception("Plantio não encontrado")
    data_plantio = datetime.strptime(data_plantio_input, '%Y-%m-%d')
    if plantio_repositorio.atualizar_por_id(id, nome, observacao, area_id, cultura_id, data_plantio):
        plantio_atualizado = plantio_repositorio.pegar_por_id(id)
        plantio_formatado = {
            'id': plantio_atualizado[0],
            'nome': plantio_atualizado[1],
            'observacao': plantio_atualizado[2],
            'area': plantio_atualizado[4],
            'cultura': plantio_atualizado[6],
            'data_plantio': plantio_atualizado[7].strftime('%Y-%m-%d')
        }
        df = pd.DataFrame([plantio_formatado])
        return df.to_string(index=False)
    else:
        raise Exception("Erro ao atualizar plantio")

def deletar_plantio_por_id(id):
    validar_deletar_plantio(id)
    plantio = plantio_repositorio.pegar_por_id(id)
    if plantio is None:
        raise Exception("Plantio não encontrado")
    if plantio_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar plantio")