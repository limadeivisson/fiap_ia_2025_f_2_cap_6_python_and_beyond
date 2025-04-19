from repositorios import plantio_repositorio
from controladores.plantio_controlador_validacao import *
import pandas as pd
from datetime import datetime

def pegar_plantios():
    try:
        plantios = plantio_repositorio.pegar()
        if plantios is None:
            print('\n\033[31mErro ao buscar plantios\033[0m')
            return
        plantios_formatados = [{
            'id': plantio[0],
            'nome': plantio[1],
            'observacao': plantio[2],
            'area': plantio[4],
            'cultura': plantio[6],
            'data_plantio': plantio[7].strftime('%Y-%m-%d')
        } for plantio in plantios]
        df = pd.DataFrame(plantios_formatados)
        print('\n=== Plantios Cadastrados ===\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao processar plantios: {str(e)}\033[0m')

def pegar_plantio_por_id(id):
    try:
        erro = validar_pegar_plantio_por_id(id)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        plantio = plantio_repositorio.pegar_por_id(id)
        if plantio is None:
            print('\n\033[31mPlantio não encontrado\033[0m')
            return
        plantio_formatado = {
            'id': plantio[0],
            'nome': plantio[1],
            'observacao': plantio[2],
            'area': plantio[4],
            'cultura': plantio[6],
            'data_plantio': plantio[7].strftime('%Y-%m-%d')
        }
        df = pd.DataFrame([plantio_formatado])
        print('\nPlantio Encontrado\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao buscar plantio: {str(e)}\033[0m')

def criar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input):
    try:
        erro = validar_criar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
            
        data_plantio = datetime.strptime(data_plantio_input, '%Y-%m-%d')
        
        id_plantio = plantio_repositorio.criar(nome, observacao, area_id, cultura_id, data_plantio)
        if id_plantio:
            print('\nPlantio Criado com Sucesso!')
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
            print('\nPlantio criado:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao criar plantio\033[0m')
    except ValueError as e:
        print(f'\n\033[31mErro: {str(e)}\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao criar plantio: {str(e)}\033[0m')

def atualizar_plantio_por_id(id, nome, observacao, area_id, cultura_id, data_plantio_input):
    try:
        erro = validar_atualizar_plantio(id, nome, observacao, area_id, cultura_id, data_plantio_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        plantio = plantio_repositorio.pegar_por_id(id)
        if plantio is None:
            print('\n\033[31mPlantio não encontrado\033[0m')
            return
            
        data_plantio = datetime.strptime(data_plantio_input, '%Y-%m-%d')
        
        if plantio_repositorio.atualizar_por_id(id, nome, observacao, area_id, cultura_id, data_plantio):
            print('\nPlantio atualizado com sucesso!')
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
            print('\nPlantio atualizado:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao atualizar plantio\033[0m')
    except ValueError as e:
        print(f'\n\033[31mErro: {str(e)}\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao atualizar plantio: {str(e)}\033[0m')

def deletar_plantio_por_id(id):
    try:
        erro = validar_deletar_plantio(id)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        plantio = plantio_repositorio.pegar_por_id(id)
        if plantio is None:
            print('\nPlantio não encontrado')
            return
        if plantio_repositorio.deletar_por_id(id):
            print('\nPlantio deletado com sucesso!')
        else:
            print('\n\033[31mErro ao deletar plantio\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao deletar plantio: {str(e)}\033[0m')