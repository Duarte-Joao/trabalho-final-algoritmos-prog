# IA recomendou usar __init__ como construtor da class e o .self para não criar elementos vazios

proximo_id = 1  #Váriavel global, para ser usada e controlada dentro das funções, sim foi uma recomendação da IA para não depender de array

#Inicializando a class Tarefa
class Tarefa:
    def __init__(self, id_unico, desc, prioridade):
        self.id = id_unico              #Está recebendo o ID gerado automaticamente, o usuario não entra com nada
        self.desc = desc                #Descrição
        self.prioridade = prioridade    #Prioridade da tarefa, o usuario escohe entre: Alta, media e baixa
        self.situacao = "Ativa"         #Todas as tarefas começam com o status de "ativa" até que o usuario conclua ela

#FUNÇÃO PARA CADASTRAR UMA NOVA TAREFA
def cadastrar_tarefa(agenda):
    global proximo_id #Inicializando a variavel
    print("\n--- Cadastrar Tarefa ---")
    id_unico = proximo_id

    desc = input("Digite a descrição da tarefa: ")

    print("Escolha qual a prioridade da tarefa: ")
    print("1 - Alta \n 2 - Média \n 3 - Baixa")
    while True:
        prioridade = input("Qual a prioridade da tarefa: ").lower()
        if prioridade == '1' or prioridade == 'alta':
            prioridade = "Alta"
            break
        if prioridade == '2' or prioridade == 'media' or prioridade == 'média':
            prioridade = "Média"
            break
        if prioridade == '3' or prioridade == 'baixa':
            prioridade = "Baixa"
            break
        else:
            print("Digite um valor válido!")

    #criando objeto e mandando atributos
    nova_tarefa = Tarefa (id_unico, desc, prioridade)

    #add nova tarefa na agenda
    agenda.append(nova_tarefa)
    print(f"\nTarefa cadastrada com sucesso! Ela recebeu o número {id_unico} como identificador.")
    proximo_id += 1 #isso aq vai fazer que a próxima tarefa tenha um id diferente

#VISUALIZAR TODAS AS TAREFAS
def mostra_agenda(agenda):
    print("\n--- Tarefas Cadastradas ---")

    #verificar se a lista de tarefas (agenda) não está vazia
    if not agenda:
        print("Nenhuma tarefa cadastrada até o momento.")
        return
    
    #se tiver tarefas, roda os for's
    #primeiro for para printar apenas as tarefas ativas
    print("\n -- TAREFAS ATIVAS --")
    tem_ativa = False 
    for tarefa in agenda:
        if tarefa.situacao == "Ativa" and tarefa.prioridade == "Alta":
            print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Prioridade: {tarefa.prioridade} | Situação: {tarefa.situacao}")
            tem_ativa = True
    for tarefa in agenda:
            if tarefa.situacao == "Ativa" and tarefa.prioridade == "Média":
                print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Prioridade: {tarefa.prioridade} | Situação: {tarefa.situacao}")
                tem_ativa = True
    for tarefa in agenda:
            if tarefa.situacao == "Ativa" and tarefa.prioridade == "Baixa":
                print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Prioridade: {tarefa.prioridade} | Situação: {tarefa.situacao}")
                tem_ativa = True
    if not tem_ativa:
        print("Nenhuma tarefa ativa no momento.")

    #segundo for para printar as concluidas
    print("\n -- TAREFAS CONCLUÍDAS --")
    tem_concluida = False
    for tarefa in agenda:
        if tarefa.situacao == "Concluída":
            print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Situação: {tarefa.situacao}")
            tem_concluida = True
    if not tem_concluida:
        print("Nenhuma concluída no momento.")

#CONCLUIR A TAREFA
def conclui_tarefa(agenda):
    print("\n--- Concluir uma Tarefa ---")

    #verificar se a agenda não ta vazia
    if not agenda:
            print("Nenhuma tarefa cadastrada até o momento.")
            return
    
    id_conclui = int(input("Digite o número identificador da tarefa que foi concluída: "))
    encontrada = False #flag para saber se achou a tarefa ou não

    for tarefa in agenda:
        if id_conclui == tarefa.id: #vai verificar se o id digitado existe na agenda
            tarefa.situacao = "Concluída"
            encontrada = True
            print("Status alterado com sucesso!")
            print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Prioridade: {tarefa.prioridade} | Situação: {tarefa.situacao}")
            break
    
    if not encontrada: #só vai entrar nesse if caso a flag continuar como "False", pois a negação de False é True, daí força entrar no if
        print(f"Erro: O identificador {id_conclui} não existe ou não foi encontrado.")

#REABRIR UMA TAREFA
def reabre_tarefa(agenda):
    print("\n--- Reabrir uma Tarefa ---")

    if not agenda:
        print("Nenhuma tarefa cadastrada até o momento.")
        return
    #Printa primeiro só as tarefas concluídas (reaproveitamento de código)
    print("\n -- TAREFAS CONCLUÍDAS --")
    tem_concluida = False
    for tarefa in agenda:
        if tarefa.situacao == "Concluída":
            print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Prioridade: {tarefa.prioridade} | Situação: {tarefa.situacao}")
            tem_concluida = True

    if not tem_concluida:
        print("Nenhuma concluída no momento.")
    #Daqui pra baixo é um reaproveitamento de código da última função, só que ao invés de mudar o status para "Conluído", muda para "Ativa"
    id_reabre = int(input("Digite o ID da Tarefa que você quer reabrir: "))
    encontrada = False
    
    for tarefa in agenda:
        if id_reabre == tarefa.id:
            tarefa.situacao = "Ativa"
            encontrada = True
            print("Status alterado com sucesso!")
            print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Prioridade: {tarefa.prioridade} | Situação: {tarefa.situacao}")
            break

    if not encontrada:
            print(f"Erro: O identificador {id_reabre} não existe ou não foi encontrado.")

#EDITAR UMA TAREFA
def edita_tarefa(agenda):
    print("\n--- Editar uma tarefa ---")

    #Primeiro, printa as tarefas ativas
    print("\n -- TAREFAS ATIVAS --")
    tem_ativa = False 
    for tarefa in agenda:
        if tarefa.situacao == "Ativa":
            print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Prioridade: {tarefa.prioridade} | Situação: {tarefa.situacao}")
            tem_ativa = True
    if not tem_ativa:
        print("Nenhuma tarefa ativa no momento.")
        return
    #Buscar pelo id qual tarefa quer editar
    busca_id = int(input("Digite o ID da tarefa a ser editada: "))
    encontrada = False
    for tarefa in agenda:
        if tarefa.id == busca_id:
            encontrada = True #atualiza a flag para garantir que a tarefa foi encontrada
            print(f"\n Tarefa número {tarefa.id} encontrada")
            #ATUALIZAÇÃO DOS VALORES
            #Nesse ponto, pedi ajuda pra IA para saber de que forma eu poderia fazer para caso o usuário quisesse manter a mesma descrição
            print(f"Descrição atual: {tarefa.desc}")
            nova_desc = input("Digite a descrição da tarefa (ou aperte Enter para manter a mesma): ") 

            if nova_desc != "":
                tarefa.desc = nova_desc #caso o valor seja diferente de vazio, atualiza os valores

            print(f"Prioridade atual: {tarefa.prioridade}")
            nova_prioridade = input("Digite a nova prioridade da tarefa (ou aperte Enter para manter a mesma): ").lower()
            if nova_prioridade != "":
                tarefa.prioridade = nova_prioridade
                if tarefa.prioridade == '1' or tarefa.prioridade == 'alta':
                    tarefa.prioridade = "Alta"
                    break
                if tarefa.prioridade == '2' or tarefa.prioridade == 'media' or tarefa.prioridade =='média':
                    tarefa.prioridade = "Média"
                    break
                if tarefa.prioridade == '3' or tarefa.prioridade == 'baixa':
                    tarefa.prioridade = "Baixa"
                    break
        #caso não ache o id
        if not encontrada:
            print(f"Erro: O identificador {busca_id} não existe ou não foi encontrado.")

#REMOVER UMA TAREFA - FUNCIONALIDADE EXTRA (ideia própria, fora dos requisitos do trabalho)
def remove_tarefa(agenda):
    print("\n --- Excluir Tarefa ---")

    if not agenda:
        print("Nenhuma tarefa cadastrada até o momento.")
        return
        
    print("\n -- TAREFAS ATIVAS --")
    tem_ativa = False 
    for tarefa in agenda:
        if tarefa.situacao == "Ativa":
            print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Prioridade: {tarefa.prioridade} | Situação: {tarefa.situacao}")
            tem_ativa = True
    if not tem_ativa:
        print("Nenhuma tarefa ativa no momento.")
    
    print("\n -- TAREFAS CONCLUÍDAS --")
    tem_concluida = False
    for tarefa in agenda:
        if tarefa.situacao == "Concluída":
            print(f"\n ID - Tarefa: {tarefa.id} | Descrição: {tarefa.desc} | Prioridade: {tarefa.prioridade} | Situação: {tarefa.situacao}")
            tem_concluida = True
    if not tem_concluida:
        print("Nenhuma concluída no momento.")

    id_exclui = int(input("\nQual tarefa deseja remover (digite o ID)?"))
    encontrada = False
    for tarefa in agenda:
        if tarefa.id == id_exclui:
            encontrada = True
            print(f"\nTarefa {id_exclui} encontrada!")
            while True:
                confirma = int(input(" Deseja excluir ela? (Digite 1 para SIM ou 2 para NÃO): "))
                if confirma != 1 and confirma != 2:
                    print("Digite um valor válido.")
                if confirma == 1:
                    agenda.remove(tarefa)
                    print("Tarefa removida com sucesso!")
                    break
                else:
                    print("Ok! Tarefa mantida")
                    break
    if not encontrada:
        print(f"Erro: O identificador {id_exclui} não existe ou não foi encontrado")              
def main():
    agenda = [] #por padrão a agenda vai ser iniciada vazia

    while True:
        print("\n========== AGENDA DE TAREFAS ==========")
        print("1 - Cadastrar Tarefa")
        print("2 - Mostrar todas as tarefas")
        print("3 - Concluir Tarefa")
        print("4 - Reabrir Tarefa")
        print("5 - Editar Tarefa")
        print("6 - Excluir Tarefa")
        print("0 - Sair")
        print("=========================================")

        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == '1':
            cadastrar_tarefa(agenda)
        elif opcao == '2':
            mostra_agenda(agenda)
        elif opcao == '3':
            conclui_tarefa(agenda)
        elif opcao == '4':
            reabre_tarefa(agenda)
        elif opcao == '5':
            edita_tarefa(agenda)
        elif opcao == '6':
            remove_tarefa(agenda)
        elif opcao == '0':
            print("\nEncerrando agenda.")
            break
        else:
            print("Digite um número entre 1 e 6 (ou 0 para sair)")

main()