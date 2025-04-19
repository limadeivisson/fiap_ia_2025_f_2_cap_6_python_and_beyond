from repositorios import feedback_repositorio
from controladores.feedback_controlador_validacao import *
import pandas as pd

def pegar_feedbacks():
    feedbacks = feedback_repositorio.pegar()
    feedbacks_formatados = [{
        'id': feedback[0],
        'cultura_id': feedback[1],
        'message_feedback': feedback[2],
        'tips': feedback[3],
        'percent': feedback[4]
    } for feedback in feedbacks]
    df = pd.DataFrame(feedbacks_formatados)
    return df.to_string(index=False)

def pegar_feedback_por_id(id):
    validar_pegar_feedback_por_id(id)
    feedback = feedback_repositorio.pegar_por_id(id)
    if feedback is None:
        raise Exception("Feedback não encontrado")
    return {
        'id': feedback[0],
        'cultura_id': feedback[1],
        'message_feedback': feedback[2],
        'tips': feedback[3],
        'percent': feedback[4]
    }

def criar_feedback(cultura_id, message_feedback, tips, percent_input):
    validar_feedback(cultura_id, message_feedback, tips, percent_input)
    percent = float(percent_input)
    id_feedback = feedback_repositorio.criar(cultura_id, message_feedback, tips, percent)
    if id_feedback:
        feedback = feedback_repositorio.pegar_por_id(id_feedback)
        return {
            'id': feedback[0],
            'cultura_id': feedback[1],
            'message_feedback': feedback[2],
            'tips': feedback[3],
            'percent': feedback[4]
        }
    else:
        raise Exception("Erro ao criar feedback!")

def atualizar_feedback_por_id(id, cultura_id, message_feedback, tips, percent_input):
    validar_atualizar_feedback(id, cultura_id, message_feedback, tips, percent_input)
    feedback = feedback_repositorio.pegar_por_id(id)
    if feedback is None:
        raise Exception("Feedback não encontrado")
    percent = float(percent_input)
    if feedback_repositorio.atualizar_por_id(id, cultura_id, message_feedback, tips, percent):
        feedback_atualizado = feedback_repositorio.pegar_por_id(id)
        return {
            'id': feedback_atualizado[0],
            'cultura_id': feedback_atualizado[1],
            'message_feedback': feedback_atualizado[2],
            'tips': feedback_atualizado[3],
            'percent': feedback_atualizado[4]
        }
    else:
        raise Exception("Erro ao atualizar feedback!")

def deletar_feedback_por_id(id):
    validar_deletar_feedback(id)
    feedback = feedback_repositorio.pegar_por_id(id)
    if feedback is None:
        raise Exception("Feedback não encontrado")
    if feedback_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar feedback")