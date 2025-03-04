from time import sleep
from lib.interface import *
from lib.tarefas import *

arq = 'lista.txt'
tarefas = ler_tarefas(arq)

while True:
    limpar_tela()
    print(linha(30))
    print('\033[31mLista de tarefas\033[m'.center(30))
    print(linha(30))
    opcao = menu(['Adicionar tarefa', 'Editar tarefa', 'Remover tarefa', 'Ver lista', 'SAIR'])

    if opcao == 1:
        inserir_tarefa(arq, tarefas)
    elif opcao == 2:
        editar_tarefa(arq, tarefas)
    elif opcao == 3:
        remover_tarefa(arq, tarefas)
    elif opcao == 4:
        mostrar_tarefa(tarefas)
    elif opcao == 5:
        break
    elif opcao is not None:
        print('Opção inválida.')
    sleep(1)
    

print('\033[36mEncerrando...\033[m')
sleep(1)
print('\033[36mFim do programa.\033[m')