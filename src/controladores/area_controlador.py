from repositorios import area_repositorio
from controladores.area_controlador_validacao import *
import pandas as pd

def pegar_areas():
    try:
        areas = area_repositorio.pegar()
        if areas is None:
            print('\nErro ao buscar áreas')
            return
        areas_formatadas = [{
            'id': area[0],
            'nome': area[1],
            'localizacao': area[2],
            'hectar': area[3]
        } for area in areas]
        df = pd.DataFrame(areas_formatadas)
        print('\nÁreas Cadastradas\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\nErro ao processar áreas: {str(e)}')

def pegar_area_por_id(id):
    try:
        erro = validar_pegar_area_por_id(id)
        if erro:
            print(f'Erro: {erro}')
            return
        area = area_repositorio.pegar_por_id(id)
        if area is None:
            print('\nÁrea não encontrada')
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
        print(f'\nErro ao buscar área: {str(e)}')

def criar_area(nome, localizacao, hectar_input):
    try:
        erro = validar_criar_area(nome, localizacao, hectar_input)
        if erro:
            print(f'\nErro: {erro}')
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
            print('\nErro ao criar área')
    except ValueError:
        print('\nErro: O valor de hectares deve ser um número')
    except Exception as e:
        print(f'\nErro ao criar área: {str(e)}')

def atualizar_area_por_id(id, nome, localizacao, hectar_input):
    try:
        erro = validar_atualizar_area(id, nome, localizacao, hectar_input)
        if erro:
            print(f'Erro: {erro}')
            return
        area = area_repositorio.pegar_por_id(id)
        if area is None:
            print('\nÁrea não encontrada')
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
            print('\nErro ao atualizar área')
    except ValueError:
        print('\nErro: O valor de hectares deve ser um número')
    except Exception as e:
        print(f'\nErro ao atualizar área: {str(e)}')

def deletar_area_por_id(id):
    try:
        erro = validar_deletar_area(id)
        if erro:
            print(f'\nErro: {erro}')
            return
        area = area_repositorio.pegar_por_id(id)
        if area is None:
            print('\nÁrea não encontrada')
            return
        if area_repositorio.deletar_por_id(id):
            print('\nÁrea deletada com sucesso!')
        else:
            print('\nErro ao deletar área')
    except Exception as e:
        print(f'\nErro ao deletar área: {str(e)}')