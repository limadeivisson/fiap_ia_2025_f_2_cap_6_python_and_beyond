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
                    pegar_feedbacks()
                case '2':
                    print('\n=== Buscar Feedback ===')
                    id = input('\nDigite o ID do feedback: ')
                    pegar_feedback_por_id(id)
                case '3':
                    print('\n=== Cadastrar Novo Feedback ===')
                    cultura_id = input('\nDigite o ID da cultura: ')
                    message_feedback = input('\nDigite a mensagem do feedback: ')
                    tips = input('\nDigite as dicas: ')
                    percent = input('\nDigite a porcentagem: ')
                    criar_feedback(cultura_id, message_feedback, tips, percent)
                case '4':
                    print('\n=== Alterar Feedback ===')
                    id = input('\nDigite o ID do feedback: ')
                    cultura_id = input('\nDigite o novo ID da cultura: ')
                    message_feedback = input('\nDigite a nova mensagem do feedback: ')
                    tips = input('\nDigite as novas dicas: ')
                    percent = input('\nDigite a nova porcentagem: ')
                    atualizar_feedback_por_id(id, cultura_id, message_feedback, tips, percent)
                case '5':
                    print('\n=== Deletar Feedback ===')
                    id = input('\nDigite o ID do feedback: ')
                    deletar_feedback_por_id(id)
                case '0':
                    print('\nSaindo do menu de feedbacks...')
                    break
                case _:
                    os.system("cls")
                    print('\nOpção inválida!')
                    print('\nPor favor, escolha uma opção válida.')
        except Exception as e:
            print(f'\nErro: {str(e)}')
            print('Por favor, tente novamente.')
        finally:
            input("\nPressione ENTER")