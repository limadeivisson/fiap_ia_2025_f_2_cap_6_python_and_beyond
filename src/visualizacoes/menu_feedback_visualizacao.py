from controladores.feedback_controlador import pegar_feedbacks, pegar_feedback_por_id, criar_feedback, atualizar_feedback_por_id, deletar_feedback_por_id
import os

def exibir_menu_principal():
    print('\n=== Menu Feedback ===\n')
    print('1. Listar todos os feedbacks')
    print('2. Buscar feedback por ID')
    print('3. Criar novo feedback')
    print('4. Atualizar feedback')
    print('5. Deletar feedback')
    print('0. Sair')
    print('\nEscolha uma opção: ', end='')

def menu_feedbacks():
    while True:
        try:
            os.system("cls")
            exibir_menu_principal()
            opcao = input().strip()
            os.system("cls")
            match opcao:
                case '1':
                    print('\n=== Feedbaks Cadastrados ===\n')
                    feedbacks = pegar_feedbacks()
                    print('\nFeedback Encontradas\n')
                    print(feedbacks)
                case '2':
                    print('\n=== Buscar Feedback Por ID ===')
                    id = input('\nDigite o ID do feedback: ')
                    feedback = pegar_feedback_por_id(id)
                    print('\nFeedback Encontrado\n')
                    print("ID:", feedback['id'])
                    print("ID da Cultura:", feedback['cultura_id'])
                    print("Mensagem:", feedback['message_feedback'])
                    print("Dicas:", feedback['tips'])
                case '3':
                    print('\n=== Cadastrar Novo Feedback ===')
                    cultura_id = input('\nDigite o ID da cultura: ')
                    message_feedback = input('\nDigite a mensagem do feedback: ')
                    tips = input('\nDigite as dicas: ')
                    percent = input('\nDigite a porcentagem: ')
                    feedback = criar_feedback(cultura_id, message_feedback, tips, percent)
                    print('\nFeedback Criado com Sucesso!')
                    print('\nFeedback criado:')
                    print("ID:", feedback['id'])
                    print("ID da Cultura:", feedback['cultura_id'])
                    print("Mensagem:", feedback['message_feedback'])
                    print("Dicas:", feedback['tips'])
                case '4':
                    print('\n=== Alterar Feedback ===')
                    id = input('\nDigite o ID do feedback: ')
                    cultura_id = input('\nDigite o novo ID da cultura: ')
                    message_feedback = input('\nDigite a nova mensagem do feedback: ')
                    tips = input('\nDigite as novas dicas: ')
                    percent = input('\nDigite a nova porcentagem: ')
                    feedback = atualizar_feedback_por_id(id, cultura_id, message_feedback, tips, percent)
                    print('\nFeedback atualizado com sucesso!')
                    print('\nFeedback atualizado:')
                    print("ID:", feedback['id'])
                    print("ID da Cultura:", feedback['cultura_id'])
                    print("Mensagem:", feedback['message_feedback'])
                    print("Dicas:", feedback['tips'])
                case '5':
                    print('\n=== Deletar Feedback ===')
                    id = input('\nDigite o ID do feedback: ')
                    deletar_feedback_por_id(id)
                    print('\nFeedback deletado com sucesso!')
                case '0':
                    print('\nSaindo do menu de feedbacks...')
                    break
                case _:
                    raise Exception("Opção inválida!")
        except Exception as e:
            os.system("cls")
            print(f'\nERRO')
            print(f'\n\033[31m{str(e)}\033[0m')
        finally:
            input("\nPressione ENTER")