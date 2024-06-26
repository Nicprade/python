import os

print("""
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
""")

print('1. Cadastrar Restaurante')
print('2. Listar Restaurantes')
print('3. Ativar Restaurante')
print('4. Sair')

menu_option = int(input('\nEscolha uma opção: '))
print(f'Você escolheu a opção {menu_option}')

def close_app():
    os.system('cls')
    print('Até Logo!')

def menu():
    

if menu_option == 1:
    print('Cadastrar Restaurante')
elif menu_option == 2:
    print('Listar Restaurantes')
elif menu_option == 3:
    print('Ativar Restaurante')
else:
    close_app
    
