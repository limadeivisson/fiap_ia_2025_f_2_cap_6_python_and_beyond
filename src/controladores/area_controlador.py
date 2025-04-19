from repositorios import area_repositorio
from controladores.area_controlador_validacao import *
import pandas as pd

def pegar_areas():
    try:
        areas = area_repositorio.pegar()
        if areas is None:
            print('\n\n\033[31mErro ao buscar áreas\033[0m')
            return
        areas_formatadas = [{
            'id': area[0],
            'nome': area[1],
            'localizacao': area[2],
            'hectar': area[3]
        } for area in areas]
        df = pd.DataFrame(areas_formatadas)
        print('\n=== Áreas Cadastradas ===\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao processar áreas: {str(e)}\033[0m')

def pegar_area_por_id(id):
    try:
        erro = validar_pegar_area_por_id(id)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        area = area_repositorio.pegar_por_id(id)
        if area is None:
            print('\n\033[31mÁrea não encontrada\033[0m')
            return
        area_formatada = {
            'id': area[0],
            'nome': area[1],
            'localizacao': area[2],
            'hectar': area[3]
        }
        df = pd.DataFrame([area_formatada])
        print('\nÁrea Encontrada\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao buscar área: {str(e)}\033[0m')

def criar_area(nome, localizacao, hectar_input):
    try:
        erro = validar_criar_area(nome, localizacao, hectar_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
            
        hectar = float(hectar_input)
        id_area = area_repositorio.criar(nome, localizacao, hectar)
        if id_area:
            print('\nÁrea Criada com Sucesso!')
            area = area_repositorio.pegar_por_id(id_area)
            area_formatada = {
                'id': area[0],
                'nome': area[1],
                'localizacao': area[2],
                'hectar': area[3]
            }
            df = pd.DataFrame([area_formatada])
            print('\nÁrea criada:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao criar área\033[0m')
    except ValueError:
        print('\n\033[31mErro: O valor de hectares deve ser um número\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao criar área: {str(e)}\033[0m')

def atualizar_area_por_id(id, nome, localizacao, hectar_input):
    try:
        erro = validar_atualizar_area(id, nome, localizacao, hectar_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        area = area_repositorio.pegar_por_id(id)
        if area is None:
            print('\n\033[31mÁrea não encontrada\033[0m')
            return
        hectar = float(hectar_input)
        if area_repositorio.atualizar_por_id(id, nome, localizacao, hectar):
            print('\nÁrea atualizada com sucesso!')
            area_atualizada = area_repositorio.pegar_por_id(id)
            area_formatada = {
                'id': area_atualizada[0],
                'nome': area_atualizada[1],
                'localizacao': area_atualizada[2],
                'hectar': area_atualizada[3]
            }
            df = pd.DataFrame([area_formatada])
            print('\nÁrea atualizada:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao atualizar área\033[0m')
    except ValueError:
        print('\n\033[31mErro: O valor de hectares deve ser um número\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao atualizar área: {str(e)}\033[0m')

def deletar_area_por_id(id):
    try:
        erro = validar_deletar_area(id)
        if erro:
            print(f'\nErro: {erro}')
            return
        area = area_repositorio.pegar_por_id(id)
        if area is None:
            print('\n\033[31mÁrea não encontrada\033[0m')
            return
        if area_repositorio.deletar_por_id(id):
            print('\nÁrea deletada com sucesso!')
        else:
            print('\n\033[31mErro ao deletar área\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao deletar área: {str(e)}\033[0m')