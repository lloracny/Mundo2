#Tabuada v3.0

while True:
    valor = int(input('Digite o valor que deseja ver a tabuada (Número negativo para parar:'))
    if valor < 0:
        print('Parando...')
        break

    for t in range(1, 11):
        print(f'{t:2} x {valor} = {t * valor}')



