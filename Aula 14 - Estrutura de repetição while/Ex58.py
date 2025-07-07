#Jogo da Adivinhação v2.0

from random import randint

r = 11
p = 0

#Numero que o pc vai pensar
num = randint(0, 10)

while r != num:
    r = int(input('Digite um valor entre 0 e 10: '))
    p += 1
    if r == num:
        print('Você acertou!')
    else:
        if r < num:
            print('Mais...')
        elif r > num:
            print('Menos...')
print(f'Você tentou {p} vezes')
