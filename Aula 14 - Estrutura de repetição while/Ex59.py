#Criando um Menu de Opções

from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

r = 0

while r != 5:
    print("""O que você deseja fazer?
    [1] para SOMAR
    [2] para MULTIPLICAR
    [3] para MAIOR
    [4] para NOVOS NUMEROS
    [5] para SAIR""")
    r = int(input())
    if r == 1:
        soma = n1 + n2
        print(f'A soma dos números é {soma}')
        print('-'* 25)
        sleep(1)
    elif r == 2:
        mult = n1 * n2
        print(f'A multiplicação dos números é {mult}')
        print('-' * 25)
        sleep(1)
    elif r == 3:
        if n1 > n2:
            print('O primeiro número é maior!')
        elif n2 > n2:
            print('O segundo número é maior!')
        else:
            print('Os números são iguais!')
        print('-' * 25)
        sleep(1)
    elif r == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print('-' * 25)
        sleep(1)
    elif r == 5:
        print('-' * 25)
        sleep(0.5)
        print('Obrigado por usar o programa!')
        break

