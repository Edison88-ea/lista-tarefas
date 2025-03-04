import os

def limpar_tela():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def linha(tam=40):
    """Gera uma linha horizontal de caracteres."""
    return '-' * tam

def menu(lista):
    """Exibe um menu de opções e retorna a opção escolhida pelo usuário."""
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    try:
        print('-' * 30)
        op = int(input('\033[32mEscolha uma opção:\033[m '))
        print('-' * 30)
        return op
    except ValueError:
        print('Opção inválida!')
        print()
        return None