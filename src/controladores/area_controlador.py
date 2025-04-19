from repositorios import area_repositorio
from controladores.area_controlador_validacao import *
import pandas as pd

def pegar_areas():
    areas = area_repositorio.pegar()
    if areas is None:
        raise Exception('Erro ao buscar áreas')
    areas_formatadas = [{
        'id': area[0],
        'nome': area[1],
        'localizacao': area[2],
        'hectar': area[3]
    } for area in areas]
    df = pd.DataFrame(areas_formatadas)
    return df.to_string(index=False)

def pegar_area_por_id(id):
    validar_pegar_area_por_id(id)
    area = area_repositorio.pegar_por_id(id)
    if area is None:
        raise Exception("Área não encontrada")
    return {
        'id': area[0],
        'nome': area[1],
        'localizacao': area[2],
        'hectar': area[3]
    }

def criar_area(nome, localizacao, hectar_input):
    validar_criar_area(nome, localizacao, hectar_input)
    hectar = float(hectar_input)
    id_area = area_repositorio.criar(nome, localizacao, hectar)
    if id_area:
        area = area_repositorio.pegar_por_id(id_area)
        return {
            'id': area[0],
            'nome': area[1],
            'localizacao': area[2],
            'hectar': area[3]
        }
    else:
        raise Exception("Erro ao criar área!")

def atualizar_area_por_id(id, nome, localizacao, hectar_input):
    validar_atualizar_area(id, nome, localizacao, hectar_input)
    area = area_repositorio.pegar_por_id(id)
    if area is None:
        raise Exception("Área não encontrada")
    hectar = float(hectar_input)
    if area_repositorio.atualizar_por_id(id, nome, localizacao, hectar):
        area_atualizada = area_repositorio.pegar_por_id(id)
        return {
            'id': area_atualizada[0],
            'nome': area_atualizada[1],
            'localizacao': area_atualizada[2],
            'hectar': area_atualizada[3]
        }
    else:
        raise Exception("Erro ao atualizar área!")

def deletar_area_por_id(id):
    validar_deletar_area(id)
    area = area_repositorio.pegar_por_id(id)
    if area is None:
        raise Exception("Área não encontrada")
    if area_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar área!")