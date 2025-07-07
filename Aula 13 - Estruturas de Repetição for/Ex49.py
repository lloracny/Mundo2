#Tabuada v.2.0

tabuada = int(input('Informe um número de 1 a 10 para visualizar sua tabuada: '))
print(f'Tabuada do {tabuada}:')

for t in range (1, 11):
    print(f'{tabuada} x {t} = {tabuada * t}')