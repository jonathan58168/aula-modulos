from numeros.soma import somarNumero
from numeros.subitracao import subitrairNumero
from numeros.divisao import dividirNumero
from numeros.multiplicacao import multiplicarNumero


def menu():
    while True:
        print('-----------Bem vindos ao Menu------------')
        print('1 - Somar números')
        print('2 - Subtrair números')
        print('3 - Dividir números')
        print('4 - Multiplicar números')
        print('5 - Sair do sistema')
        opcao = int(input('Digite o número da opção desejada: '))

        if opcao == 1:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            print(f'Resultado: {somarNumero(num1, num2)}')
        elif opcao == 2:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            print(f'Resultado: {subitrairNumero(num1, num2)}')
        elif opcao == 3:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            print(f'Resultado: {dividirNumero(num1, num2)}')
        elif opcao == 4:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            print(f'Resultado: {multiplicarNumero(num1, num2)}')
        elif opcao == 5:
            print('Você saiu do sistema até logo')
            break
        else:
            print('Opção inválida!')
menu()