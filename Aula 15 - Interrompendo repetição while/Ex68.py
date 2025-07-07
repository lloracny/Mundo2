#Jogo do Par ou Ímpar

from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador} e o total é de {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {vitoria} vezes!')