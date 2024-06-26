import os

def show_banner():
    print("""
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    """)

def show_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair')

def choose_option():
    menu_option = int(input('\nEscolha uma opção: '))
    
    match menu_option:
        case 1:
            os.system('cls')
            print('Cadastrar Restaurante')
        case 2:
            os.system('cls')
            print('Listar Restaurantes')
        case 3:
            os.system('cls')
            print('Ativar Restaurante')
        case 4:
            close_app()
        case _:
            os.system('cls')
            print('Opção Inválida!')


def close_app():
    os.system('cls')
    print('Até Logo!\n')

def main():
    show_banner()
    show_menu()
    choose_option()


if __name__ == '__main__':
    main()