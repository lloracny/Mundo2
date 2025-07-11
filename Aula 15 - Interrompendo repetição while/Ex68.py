#Jogo do Par ou Ímpar

from random import randint
from time import sleep

vitoria = 0
print('-'*30)
print('JOGO DO PAR OU ÍMPAR'.center(30, '-'))
print('-'*30)
sleep(1)

while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor de 0 a 10: '))
    par_ou_impar = input('Par ou ímpar? [P/I] ').upper()[0]

    soma = computador + jogador

    sleep(0.5)

    if soma % 2 == 0:
        print('-' * 10)
        print('Deu par!')
        print('-' * 10)
        sleep(1)
    else:
        print('-'*10)
        print('Deu ímpar!')
        print('-' * 10)
        sleep(1)

    while par_ou_impar not in ('P', 'I'):
        par_ou_impar = input('Par ou ímpar? [P/I] ').upper()[0]

    if soma % 2 == 0 and par_ou_impar == 'P':
        print(f'Você ganhou!')
        print('-' * 10)
        vitoria += 1
        continue

    if soma % 2 == 1 and par_ou_impar == 'I':
        print(f'Você ganhou!')
        vitoria += 1
        continue

    else:
        print('Você perdeu!')
        print('-' * 10)
        sleep(1)
        if vitoria > 0:
            print(f'Você venceu {vitoria} vez(es).')
            print('-' * 25)
        print('Parando...')


        break




