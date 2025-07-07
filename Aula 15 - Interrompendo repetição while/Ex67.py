#Tabuada v3.0

from time import sleep

num = 1

while num > 0:
    num = int(input('Digite um valor para ver sua tabuada (0 para parar): '))
    if num < 0:
        sleep(0.5)
        break
    for t in range(1, 11):
        print(f'{num} x {t} = {num * t}')

print('Saindo...')
sleep(1)
print('Programa finalizado')




