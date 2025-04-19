from repositorios import cultura_repositorio
from controladores.cultura_controlador_validacao import *
import pandas as pd

def pegar_culturas():
    try:
        culturas = cultura_repositorio.pegar()
        if culturas is None:
            print('\n\033[31mErro ao buscar culturas\033[0m')
            return
        culturas_formatadas = [{
            'id': cultura[0],
            'nome': cultura[1],
            'consumo_hidrico_diario_l_m2': cultura[2]
        } for cultura in culturas]
        df = pd.DataFrame(culturas_formatadas)
        print('\n=== Culturas Cadastradas ===\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao processar culturas: {str(e)}\033[0m')

def pegar_cultura_por_id(id):
    try:
        erro = validar_pegar_cultura_por_id(id)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        cultura = cultura_repositorio.pegar_por_id(id)
        if cultura is None:
            print('\n\033[31mCultura não encontrada\033[0m')
            return
        cultura_formatada = {
            'id': cultura[0],
            'nome': cultura[1],
            'consumo_hidrico_diario_l_m2': cultura[2]
        }
        df = pd.DataFrame([cultura_formatada])
        print('\nCultura Encontrada\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao buscar cultura: {str(e)}\033[0m')

def criar_cultura(nome, consumo_hidrico_diario_l_m2_input):
    try:
        erro = validar_criar_cultura(nome, consumo_hidrico_diario_l_m2_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        consumo_hidrico_diario_l_m2 = float(consumo_hidrico_diario_l_m2_input)
        id_cultura = cultura_repositorio.criar(nome, consumo_hidrico_diario_l_m2)
        if id_cultura:
            print('\nCultura Criada com Sucesso!')
            cultura = cultura_repositorio.pegar_por_id(id_cultura[0])
            cultura_formatada = {
                'id': cultura[0],
                'nome': cultura[1],
                'consumo_hidrico_diario_l_m2': cultura[2]
            }
            df = pd.DataFrame([cultura_formatada])
            print('\nCultura criada:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao criar cultura\033[0m')
    except ValueError:
        print('\n\033[31mErro: Os valores numéricos devem ser números válidos\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao criar cultura: {str(e)}\033[0m')

def atualizar_cultura_por_id(id, nome, consumo_hidrico_diario_l_m2_input):
    try:
        erro = validar_atualizar_cultura(id, nome, consumo_hidrico_diario_l_m2_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        cultura = cultura_repositorio.pegar_por_id(id)
        if cultura is None:
            print('\n\033[31mCultura não encontrada\033[0m')
            return
        consumo_hidrico_diario_l_m2 = float(consumo_hidrico_diario_l_m2_input)
        if cultura_repositorio.atualizar_por_id(id, nome, consumo_hidrico_diario_l_m2):
            print('\nCultura atualizada com sucesso!')
            cultura_atualizada = cultura_repositorio.pegar_por_id(id)
            cultura_formatada = {
                'id': cultura_atualizada[0],
                'nome': cultura_atualizada[1],
                'consumo_hidrico_diario_l_m2': cultura_atualizada[2]
            }
            df = pd.DataFrame([cultura_formatada])
            print('\nCultura atualizada:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao atualizar cultura\033[0m')
    except ValueError:
        print('\n\033[31mErro: Os valores numéricos devem ser números válidos\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao atualizar cultura: {str(e)}\033[0m')

def deletar_cultura_por_id(id):
    try:
        erro = validar_deletar_cultura(id)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        cultura = cultura_repositorio.pegar_por_id(id)
        if cultura is None:
            print('\n\033[31mCultura não encontrada\033[0m')
            return
        if cultura_repositorio.deletar_por_id(id):
            print('\nCultura deletada com sucesso!')
        else:
            print('\n\033[31mErro ao deletar cultura\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao deletar cultura: {str(e)}\033[0m')