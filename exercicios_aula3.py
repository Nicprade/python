import os

number_of_exercises = ['CRIAR LISTA','MOSTRAR ELEMENTOS','SOMAR NUMEROS IMPARES','ORDENAR DECRESCENTE','TABUADA','SOMAR ELEMENTOS','MEDIA DOS ELEMENTOS']

def return_to_menu():
    input('\nPressione ENTER pra voltar ao menu')
    main()

def title(txt):
    print ('=======')
    print (txt)
    print ('=======\n')

def show_menu():
    number = int(1)
    for exercise in number_of_exercises:
        print(f'{number}. {exercise}')
        number += 1
    print('0. Sair do Programa')

def exercise_1():
    title('CRIAR LISTA')
    print("""Crie uma lista para cada informação a seguir:
- Lista de números de 1 a 10;
- Lista com quatro nomes;
- Lista com o ano que você nasceu e o ano atual.""")
    numbers = [1,2,3,4,5,6,7,8,9,10]
    names = ['Nicholas', 'Daiane', 'Ricardo', 'Shirlei']
    years = [1987, 2024]
    return_to_menu()

def exercise_2():
    title('MOSTRAR ELEMENTOS')
    print('Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.')
    print('\nLista de Países:')
    countries = ['Brasil','Eslováquia','França','Estados Unidos']
    for i in countries:
        print(f'- {i}')
    return_to_menu()

def exercise_3():
    title('SOMAR NUMEROS IMPARES')
    print('Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.')
    numbers = [1,2,3,4,5,6,7,8,9,10]
    add_odd_number = 0
    for i in numbers:
        if (i % 2 == 0):
            add_odd_number += i
    print (f'\nA soma de todos os numeros pares entre 1 e 10 é {add_odd_number}.')
    return_to_menu()

def exercise_4():
    title('ORDENAR DECRESCENTE')
    print('Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente\n')
    numbers = [1,2,3,4,5,6,7,8,9,10]
    counter = len(numbers) - 1
    while counter >= 0:
        print(f'* {numbers[counter]}')
        counter -= 1
    return_to_menu()

def exercise_5():
    title('TABUADA')
    print('Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.\n')
    number = int(input('Digite um número: '))
    i = 1
    while i <= 10:
        print(f'{number} x {i} = ', number * i)
        i += 1
    return_to_menu()

def exercise_6():
    title('SOMAR ELEMENTOS')
    print('Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.\n')
    numbers = []
    value = 1
    sum = 0
    try:
        while value != 0:
            value=int(input('Digite o número (0 para sair): '))
            numbers.append(value)
    except:
        print('Por favor digite apenas números!')
        input('Aperte ENTER para recomeçar')
        os.system('cls')
        exercise_6()

    for i in numbers:
        sum += i
    
    print(f'A soma de todos os numeros digitados é {sum}')
    return_to_menu()

def exercise_7():
    title('MEDIA DOS ELEMENTOS')
    print('Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.\n')
    numbers = []
    value = 1
    sum = 0
    
    try:
        while value != 0:
            value=int(input('Digite o número (0 para sair): '))
            if value != 0:
                numbers.append(value)
                sum += value
    except:
        print('Por favor digite apenas números!')
        input('Pressione ENTER para recomeçar')
        os.system('cls')
        exercise_7()

    try:
        print('A média dos valores digitados é', (sum / len(numbers)))
    except:
        print('Você precisa digitar ao menos 1 valor!')
        input('Pressione ENTER para recomeçar')
        os.system('cls')
        exercise_7()
    return_to_menu()

def main ():
    os.system('cls')
    show_menu()
    
    try:
        choose_test = int(input('Qual exercício você quer testar (1 - 7): '))

        match choose_test:
            case 1:
                os.system('cls')
                exercise_1()
            case 2:
                os.system('cls')
                exercise_2()
            case 3:
                os.system('cls')
                exercise_3()
            case 4:
                os.system('cls')
                exercise_4()
            case 5:
                os.system('cls')
                exercise_5()
            case 6:
                os.system('cls')
                exercise_6()
            case 7:
                os.system('cls')
                exercise_7()
            case 0:
                os.system('cls')
                print('Até logo!')
            case _:
                os.system('cls')
                print('OPÇÃO INVÁLIDA')
                input('Pressione ENTER para voltar ao menu')
                main()
    except:
        os.system('cls')
        print('OPÇÃO INVÁLIDA')
        input('Pressione ENTER para voltar ao menu')
        main()

if __name__ == '__main__':
    main()