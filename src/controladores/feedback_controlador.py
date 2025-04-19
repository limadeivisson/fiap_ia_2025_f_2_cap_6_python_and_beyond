from repositorios import feedback_repositorio
from controladores.feedback_controlador_validacao import *
import pandas as pd

def pegar_feedbacks():
    try:
        feedbacks = feedback_repositorio.pegar()
        if feedbacks is None:
            print('\n\n\033[31mErro ao buscar feedbacks\033[0m')
            return
        feedbacks_formatados = [{
            'id': feedback[0],
            'cultura_id': feedback[1],
            'message_feedback': feedback[2],
            'tips': feedback[3],
            'percent': feedback[4]
        } for feedback in feedbacks]
        df = pd.DataFrame(feedbacks_formatados)
        print('\n=== Feedbacks Cadastrados ===\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao processar feedbacks: {str(e)}\033[0m')

def pegar_feedback_por_id(id):
    try:
        erro = validar_pegar_feedback_por_id(id)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        feedback = feedback_repositorio.pegar_por_id(id)
        if feedback is None:
            print('\n\033[31mFeedback não encontrado\033[0m')
            return
        feedback_formatado = {
            'id': feedback[0],
            'cultura_id': feedback[1],
            'message_feedback': feedback[2],
            'tips': feedback[3],
            'percent': feedback[4]
        }
        df = pd.DataFrame([feedback_formatado])
        print('\nFeedback Encontrado\n')
        print(df.to_string(index=False))
    except Exception as e:
        print(f'\n\033[31mErro ao buscar feedback: {str(e)}\033[0m')

def criar_feedback(cultura_id, message_feedback, tips, percent_input):
    try:
        erro = validar_criar_feedback(cultura_id, message_feedback, tips, percent_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
            
        percent = float(percent_input)
        id_feedback = feedback_repositorio.criar(cultura_id, message_feedback, tips, percent)
        if id_feedback:
            print('\nFeedback Criado com Sucesso!')
            feedback = feedback_repositorio.pegar_por_id(id_feedback)
            feedback_formatado = {
                'id': feedback[0],
                'cultura_id': feedback[1],
                'message_feedback': feedback[2],
                'tips': feedback[3],
                'percent': feedback[4]
            }
            df = pd.DataFrame([feedback_formatado])
            print('\nFeedback criado:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao criar feedback\033[0m')
    except ValueError:
        print('\n\033[31mErro: O valor da porcentagem deve ser um número\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao criar feedback: {str(e)}\033[0m')

def atualizar_feedback_por_id(id, cultura_id, message_feedback, tips, percent_input):
    try:
        erro = validar_atualizar_feedback(id, cultura_id, message_feedback, tips, percent_input)
        if erro:
            print(f'\n\033[31mErro: {erro}\033[0m')
            return
        feedback = feedback_repositorio.pegar_por_id(id)
        if feedback is None:
            print('\n\033[31mFeedback não encontrado\033[0m')
            return
        percent = float(percent_input)
        if feedback_repositorio.atualizar_por_id(id, cultura_id, message_feedback, tips, percent):
            print('\nFeedback atualizado com sucesso!')
            feedback_atualizado = feedback_repositorio.pegar_por_id(id)
            feedback_formatado = {
                'id': feedback_atualizado[0],
                'cultura_id': feedback_atualizado[1],
                'message_feedback': feedback_atualizado[2],
                'tips': feedback_atualizado[3],
                'percent': feedback_atualizado[4]
            }
            df = pd.DataFrame([feedback_formatado])
            print('\nFeedback atualizado:')
            print(df.to_string(index=False))
        else:
            print('\n\033[31mErro ao atualizar feedback\033[0m')
    except ValueError:
        print('\n\033[31mErro: O valor da porcentagem deve ser um número\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao atualizar feedback: {str(e)}\033[0m')

def deletar_feedback_por_id(id):
    try:
        erro = validar_deletar_feedback(id)
        if erro:
            print(f'\nErro: {erro}')
            return
        feedback = feedback_repositorio.pegar_por_id(id)
        if feedback is None:
            print('\n\033[31mFeedback não encontrado\033[0m')
            return
        if feedback_repositorio.deletar_por_id(id):
            print('\nFeedback deletado com sucesso!')
        else:
            print('\n\033[31mErro ao deletar feedback\033[0m')
    except Exception as e:
        print(f'\n\033[31mErro ao deletar feedback: {str(e)}\033[0m')