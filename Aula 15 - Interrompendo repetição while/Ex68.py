#Jogo do Par ou Ímpar

from random import randint

vitoria = 0

while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor de 0 a 10: '))
    par_ou_impar = input('Par ou ímpar? [P/I] ').upper()[0]

    soma = computador + jogador

    while par_ou_impar not in ('P', 'I'):
        par_ou_impar = input('Par ou ímpar? [P/I] ').upper()[0]

    if soma % 2 == 0 and par_ou_impar == 'P':
        print(f'Você ganhou!')
        vitoria += 1
        continue

    if soma % 2 == 1 and par_ou_impar == 'I':
        print(f'Você ganhou!')
        vitoria += 1
        continue

    else:
        print('Você perdeu!')
        print(f"Você jogou {jogador} e o computador jogou {computador}.")

        if vitoria > 0:
            print(f'Você venceu {vitoria} vez(es).')
        break




