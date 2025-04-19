from repositorios import cultura_repositorio
from controladores.cultura_controlador_validacao import *
import pandas as pd

def pegar_culturas():
    culturas = cultura_repositorio.pegar()
    if culturas is None:
        raise Exception("Erro ao buscar culturas!")
    culturas_formatadas = [{
        'id': cultura[0],
        'nome': cultura[1],
        'consumo_hidrico_diario_l_m2': cultura[2]
    } for cultura in culturas]
    df = pd.DataFrame(culturas_formatadas)
    return df.to_string(index=False)

def pegar_cultura_por_id(id):
    validar_pegar_cultura_por_id(id)
    cultura = cultura_repositorio.pegar_por_id(id)
    if cultura is None:
        raise Exception("Cultura não encontrada")
    return {
        'id': cultura[0],
        'nome': cultura[1],
        'consumo_hidrico_diario_l_m2': cultura[2]
    }

def criar_cultura(nome, consumo_hidrico_diario_l_m2_input):
    validar_criar_cultura(nome, consumo_hidrico_diario_l_m2_input)
    consumo_hidrico_diario_l_m2 = float(consumo_hidrico_diario_l_m2_input)
    id_cultura = cultura_repositorio.criar(nome, consumo_hidrico_diario_l_m2)
    if id_cultura:
        cultura = cultura_repositorio.pegar_por_id(id_cultura[0])
        return {
            'id': cultura[0],
            'nome': cultura[1],
            'consumo_hidrico_diario_l_m2': cultura[2]
        }

def atualizar_cultura_por_id(id, nome, consumo_hidrico_diario_l_m2_input):
    validar_atualizar_cultura(id, nome, consumo_hidrico_diario_l_m2_input)
    cultura = cultura_repositorio.pegar_por_id(id)
    if cultura is None:
        raise Exception("Cultura não encontrada")
    consumo_hidrico_diario_l_m2 = float(consumo_hidrico_diario_l_m2_input)
    if cultura_repositorio.atualizar_por_id(id, nome, consumo_hidrico_diario_l_m2):
        cultura_atualizada = cultura_repositorio.pegar_por_id(id)
        return {
            'id': cultura_atualizada[0],
            'nome': cultura_atualizada[1],
            'consumo_hidrico_diario_l_m2': cultura_atualizada[2]
        }
    else:
        raise Exception("Erro ao atualizar cultura!")

def deletar_cultura_por_id(id):
    validar_deletar_cultura(id)
    cultura = cultura_repositorio.pegar_por_id(id)
    if cultura is None:
        raise Exception("Cultura não encontrada")
    if cultura_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar cultura!")