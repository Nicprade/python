import os

def exercicio_1():
    print('\n-- EXERCÍCIO 1 --\n')
    print('Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.\n\n')
    
    number = int(input('Digite o Número: '))
  
    if number % 2 == 0:
        print(f'O número {number} é par.')
    else:
        print(f'O número {number} é ímpar.')

def exercicio_2():
    print('\n-- EXERCÍCIO 2 --')
    print("""
Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
- Criança: 0 a 12 anos;
- Adolescente: 13 a 18 anos;
- Adulto: acima de 18 anos.
    \n""")

    age = int(input('Digite sua idade: '))

    if 0 <= age <= 12:
        print(f'Você é uma CRIANÇA')
    elif 13 <= age <= 18:
        print(f'Você é um ADOLESCENTE')
    else:
        print(f'Você é um ADULTO')

def exercicio_3():
    print('\n-- EXERCÍCIO 3 --\n')
    print('Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.\n')
    
    USER = 'nicholas.prade'
    PASSWORD = 'abcd12345'

    print (f"""para conferencia:
usuário = {USER}
senha = {PASSWORD}
    """)

    test_user = input('Usuário: ')
    test_password = input('Senha: ')

    if test_user == USER and test_password == PASSWORD:
        print('\nACESSO AUTORIZADO')
    else:
        print('\nUSUÁRIO ou SENHA incorretos')

def exercicio_4():
    print('\n-- EXERCÍCIO 4 --')
    print("""
Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
- Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
- Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
- Terceiro Quadrante: os valores de x e y devem ser menores que zero;
- Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
- Caso contrário: o ponto está localizado no eixo ou origem.
    \n""")

    number_x = int(input('Digite o valor de X: '))
    number_y = int(input('Digite o valor de Y: '))
    
    if number_x > 0 and number_y > 0:
        print('\nEsse ponto está no PRIMEIRO QUADRANTE')
        print("""
                |
                |  aqui
                |
        -------- --------
                |
                |
                |
        """)
    elif number_x < 0 and number_y > 0:
        print('\nEsse ponto está no SEGUNDO QUADRANTE')
        print("""
                |
          aqui  |  
                |
        -------- --------
                |
                |
                |
        """)
    elif number_x < 0 and number_y < 0:
        print('\nEsse ponto está no TERCEIRO QUADRANTE')
        print("""
                |
                |
                |
        -------- --------
                |
          aqui  |
                |
        """)
    elif number_x > 0 and number_y < 0:
        print('\nEsse ponto está no QUARTO QUADRANTE')
        print("""
                |
                |
                |
        -------- --------
                |
                |  aqui
                |
        """)
    elif number_x == 0 and number_y != 0:
        if number_y > 0:
            print('Esse ponto está SOBRE O EIXO Y')
            print("""
                |
               aqui
                |
        -------- --------
                |
                |
                |
        """)
        else:
            print('Esse ponto está SOBRE O EIXO Y')
            print("""
                |
                |
                |
        -------- --------
                |
               aqui
                |
            """)
    elif number_x != 0 and number_y == 0:
        if number_x > 0:
            print('Esse ponto está SOBRE O EIXO X')
            print("""
                |
                |
                |
        -------- --aqui--
                |
                |
                |
            """)
        else:
            print('Esse ponto está SOBRE O EIXO X')
            print("""
                |
                |
                |
        --aqui-- --------
                |
                |
                |
            """)
    else:
        print ('Esse ponto está NA ORIGEM')
        print("""
                |
                |
                |
        ------aqui-------
                |
                |
                |
        """)


def main ():
    print ('\nHora da prática: condicionais')
    print ("""
1. Par ou ímpar?
2. Criança, adolescente ou adulto?
3. Usuário e Senha
4. Plano cartesiano
""")
    choose_test = int(input('Qual exercício você quer testar (1 - 4): '))

    match choose_test:
        case 1:
            os.system('cls')
            exercicio_1()
        case 2:
            os.system('cls')
            exercicio_2()
        case 3:
            os.system('cls')
            exercicio_3()
        case 4:
            os.system('cls')
            exercicio_4()
        case _:
            print('OPÇÃO INVÁLIDA')

if __name__ == '__main__':
    main()
