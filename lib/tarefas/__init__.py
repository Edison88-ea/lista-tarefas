from lib.interface import *

def ler_tarefas(arq):
    """Lê as tarefas do arquivo especificado."""
    try:
        with open(arq, 'r') as arquivo:
            tarefas = [linha.strip() for linha in arquivo]
        return tarefas
    except FileNotFoundError:
        print(f"\033[31mErro: Arquivo '{arq}' não encontrado. Criando novo arquivo.\033[m")
        open(arq, 'w').close()
        return []
    except IOError as e:
        print(f"\033[31mErro ao ler o arquivo '{arq}': {e}\033[m")
        return []

def escrever_tarefas(arq, tarefas):
    """Escreve a lista de tarefas no arquivo especificado."""
    try:
        with open(arq, 'w') as arquivo:
            for tarefa in tarefas:
                arquivo.write(f'{tarefa}\n')
    except IOError as e:
        print(f"\033[31mErro ao escrever no arquivo '{arq}': {e}\033[m")

def inserir_tarefa(arq, tarefas):
    """Adiciona uma nova tarefa à lista e a escreve no arquivo."""
    tarefa = input('\033[33mDigite a tarefa:\033[m ')
    tarefas.append(tarefa)
    escrever_tarefas(arq, tarefas)
    print(f'Tarefa "{tarefa}" adicionada.')
def editar_tarefa(arq, tarefas):
    """Edita uma tarefa existente na lista e atualiza o arquivo."""
    mostrar_tarefa(tarefas)
    try:
        i = int(input('Qual tarefa quer editar? (índice) '))
        if 0 <= i < len(tarefas):
            nova_tarefa = input('Edite a tarefa: ')
            tarefas[i] = nova_tarefa
            escrever_tarefas(arq, tarefas)
            print('Tarefa editada com sucesso!')
        else:
            print('Tarefa não encontrada.')
    except ValueError:
        print('Digite um índice válido.')

def remover_tarefa(arq, tarefas):
    """Remove uma tarefa da lista e atualiza o arquivo."""
    mostrar_tarefa(tarefas)
    try:
        i = int(input('Qual tarefa quer remover? (índice) '))
        if 0 <= i < len(tarefas):
            tarefas.pop(i)
            escrever_tarefas(arq, tarefas)
            print('Tarefa removida com sucesso!')
        else:
            print('Tarefa não encontrada.')
    except ValueError:
        print('Digite um índice válido.')

def mostrar_tarefa(tarefas):
    """Exibe a lista de tarefas no console."""
    if not tarefas:
        print('A lista de tarefas está vazia.')
    else:
        print('\033[36mLista de tarefas:\033[m')
        for i, tarefa in enumerate(tarefas):
            print(f'{i}: {tarefa}')