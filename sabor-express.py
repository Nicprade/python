import os

restaurants = ['Sabor da Terra', 'Mama mia Massas']



def show_banner():
    print("""
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    """)

def show_menu():
    print('1. Cadastrar Restaurante')
    print('2. Restaurantes Cadastrados')
    print('3. Ativar Restaurante')
    print('4. Sair')

def return_to_menu():
    input('\nPressione ENTER pra voltar ao menu')
    main()

def submenu_title(submenu):
    os.system('cls')
    print('=====================')
    print(submenu)
    print('=====================\n')

def invalid_option():
    print('Opção Inválida!')
    return_to_menu()

def register_restaurant():
    submenu_title('CADASTRAR RESTAURANTE')
    name = input('NOME: ')
    restaurants.append(name)
    print(f'O restaurante {name} foi cadastrado!')
    return_to_menu()

def list_restaurants():
    submenu_title('RESTAURANTES CADASTRADOS')
    for restaurants_name in restaurants:
        print (f'- {restaurants_name}')
    return_to_menu()


def choose_option():
    try:
        menu_option = int(input('\nEscolha uma opção: '))
    
        match menu_option:
            case 1:
                register_restaurant()
            case 2:
                list_restaurants()
            case 3:
                os.system('cls')
                print('Ativar Restaurante')
            case 4:
                close_app()
            case _:
                invalid_option()
    except:
        invalid_option()

def close_app():
    os.system('cls')
    print('Até Logo!\n')



def main():
    os.system('cls')
    show_banner()
    show_menu()
    choose_option()


if __name__ == '__main__':
    main()