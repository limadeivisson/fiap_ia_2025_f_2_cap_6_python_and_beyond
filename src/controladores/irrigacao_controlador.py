from repositorios import irrigacao_repositorio
from controladores.irrigacao_controlador_validacao import *
import pandas as pd
from datetime import datetime

def pegar_irrigacoes():
    try:
        irrigacoes = irrigacao_repositorio.pegar()
        if irrigacoes is None:
            print('\n\033[31mErro ao buscar irrigações\033[0m')
            return
        irrigacoes_formatadas = [{
            'id': irrigacao[0],
            'plantio': irrigacao[2],
            'data_irrigacao': irrigacao[3].strftime('%Y-%m-%d'),
            'volume_agua_l': irrigacao[4]
        } for irrigacao in irrigacoes]
        df = pd.DataFrame(irrigacoes_formatadas)
        print('\n=== Irrigações Cadastradas ===\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao processar irrigações: {str(e)}\033[0m')

def pegar_irrigacao_por_id(id):
    try:
        erro = validar_pegar_irrigacao_por_id(id)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        irrigacao = irrigacao_repositorio.pegar_por_id(id)
        if irrigacao is None:
            print('\n\033[31mIrrigação não encontrada\033[0m')
            return
        irrigacao_formatada = {
            'id': irrigacao[0],
            'plantio': irrigacao[2],
            'data_irrigacao': irrigacao[3].strftime('%Y-%m-%d'),
            'volume_agua_l': irrigacao[4]
        }
        df = pd.DataFrame([irrigacao_formatada])
        print('\nIrrigação Encontrada\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao buscar irrigação: {str(e)}\033[0m')

def criar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input):
    try:
        erro = validar_criar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
            
        data_irrigacao = datetime.strptime(data_irrigacao_input, '%Y-%m-%d')
        volume_agua_l = float(volume_agua_l_input)
        
        id_irrigacao = irrigacao_repositorio.criar(plantio_id, data_irrigacao, volume_agua_l)
        if id_irrigacao:
            print('\nIrrigação Registrada com Sucesso!')
            irrigacao = irrigacao_repositorio.pegar_por_id(id_irrigacao[0])
            irrigacao_formatada = {
                'id': irrigacao[0],
                'plantio': irrigacao[2],
                'data_irrigacao': irrigacao[3].strftime('%Y-%m-%d'),
                'volume_agua_l': irrigacao[4]
            }
            df = pd.DataFrame([irrigacao_formatada])
            print('\nIrrigação Registrada:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao criar irrigação\033[0m')
    except ValueError as e:
        print(f'\n\033[31mErro: {str(e)}\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao criar irrigação: {str(e)}\033[0m')

def atualizar_irrigacao_por_id(id, plantio_id, data_irrigacao_input, volume_agua_l_input):
    try:
        erro = validar_atualizar_irrigacao(id, plantio_id, data_irrigacao_input, volume_agua_l_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        irrigacao = irrigacao_repositorio.pegar_por_id(id)
        if irrigacao is None:
            print('\n\033[31mIrrigação não encontrada\033[0m')
            return
            
        data_irrigacao = datetime.strptime(data_irrigacao_input, '%Y-%m-%d')
        volume_agua_l = float(volume_agua_l_input)
        
        if irrigacao_repositorio.atualizar_por_id(id, plantio_id, data_irrigacao, volume_agua_l):
            print('\nIrrigação atualizada com sucesso!')
            irrigacao_atualizada = irrigacao_repositorio.pegar_por_id(id)
            irrigacao_formatada = {
                'id': irrigacao_atualizada[0],
                'plantio': irrigacao_atualizada[2],
                'data_irrigacao': irrigacao_atualizada[3].strftime('%Y-%m-%d'),
                'volume_agua_l': irrigacao_atualizada[4]
            }
            df = pd.DataFrame([irrigacao_formatada])
            print('\nIrrigação atualizada:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao atualizar irrigação\033[0m')
    except ValueError as e:
        print(f'\n\033[31mErro: {str(e)}\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao atualizar irrigação: {str(e)}\033[0m')

def deletar_irrigacao_por_id(id):
    try:
        erro = validar_deletar_irrigacao(id)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        irrigacao = irrigacao_repositorio.pegar_por_id(id)
        if irrigacao is None:
            print('\nIrrigação não encontrada')
            return
        if irrigacao_repositorio.deletar_por_id(id):
            print('\nIrrigação deletada com sucesso!')
        else:
            print('\n\033[31mErro ao deletar irrigação\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao deletar irrigação: {str(e)}\033[0m')