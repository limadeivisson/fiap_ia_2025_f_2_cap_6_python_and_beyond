from repositorios import irrigacao_repositorio
from controladores.irrigacao_controlador_validacao import *
import pandas as pd
from datetime import datetime

def pegar_irrigacoes():
    try:
        irrigacoes = irrigacao_repositorio.pegar()
        if irrigacoes is None:
            print('\nErro ao buscar irrigações')
            return
        irrigacoes_formatadas = [{
            'id': irrigacao[0],
            'plantio': irrigacao[2],
            'data_irrigacao': irrigacao[3].strftime('%Y-%m-%d'),
            'volume_agua_l': irrigacao[4]
        } for irrigacao in irrigacoes]
        df = pd.DataFrame(irrigacoes_formatadas)
        print('\nIrrigações Cadastradas\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\nErro ao processar irrigações: {str(e)}')

def pegar_irrigacao_por_id(id):
    try:
        erro = validar_pegar_irrigacao_por_id(id)
        if erro:
            print(f'Erro: {erro}')
            return
        irrigacao = irrigacao_repositorio.pegar_por_id(id)
        if irrigacao is None:
            print('\nIrrigação não encontrada')
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
        print(f'\nErro ao buscar irrigação: {str(e)}')

def criar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input):
    try:
        erro = validar_criar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input)
        if erro:
            print(f'\nErro: {erro}')
            return
            
        data_irrigacao = datetime.strptime(data_irrigacao_input, '%Y-%m-%d')
        volume_agua_l = float(volume_agua_l_input)
        
        id_irrigacao = irrigacao_repositorio.criar(plantio_id, data_irrigacao, volume_agua_l)
        if id_irrigacao:
            print('\nIrrigação Criada com Sucesso!')
            irrigacao = irrigacao_repositorio.pegar_por_id(id_irrigacao[0])
            irrigacao_formatada = {
                'id': irrigacao[0],
                'plantio': irrigacao[2],
                'data_irrigacao': irrigacao[3].strftime('%Y-%m-%d'),
                'volume_agua_l': irrigacao[4]
            }
            df = pd.DataFrame([irrigacao_formatada])
            print('\nIrrigação criada:')
            print(df.to_string(index=False))
        else:
            print('\nErro ao criar irrigação')
    except ValueError as e:
        print(f'\nErro: {str(e)}')
    except Exception as e:
        print(f'\nErro ao criar irrigação: {str(e)}')

def atualizar_irrigacao_por_id(id, plantio_id, data_irrigacao_input, volume_agua_l_input):
    try:
        erro = validar_atualizar_irrigacao(id, plantio_id, data_irrigacao_input, volume_agua_l_input)
        if erro:
            print(f'Erro: {erro}')
            return
        irrigacao = irrigacao_repositorio.pegar_por_id(id)
        if irrigacao is None:
            print('\nIrrigação não encontrada')
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
            print('\nErro ao atualizar irrigação')
    except ValueError as e:
        print(f'\nErro: {str(e)}')
    except Exception as e:
        print(f'\nErro ao atualizar irrigação: {str(e)}')

def deletar_irrigacao_por_id(id):
    try:
        erro = validar_deletar_irrigacao(id)
        if erro:
            print(f'Erro: {erro}')
            return
        irrigacao = irrigacao_repositorio.pegar_por_id(id)
        if irrigacao is None:
            print('\nIrrigação não encontrada')
            return
        if irrigacao_repositorio.deletar_por_id(id):
            print('\nIrrigação deletada com sucesso!')
        else:
            print('\nErro ao deletar irrigação')
    except Exception as e:
        print(f'\nErro ao deletar irrigação: {str(e)}')