#Simulador de Caixa Eletrônico

cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0

valor = int(input('Informe o valor a ser secado: '))

while valor != 0:
    while valor >= 50:
        valor -= 50
        cont50 += 1
    while 20 <= valor < 50:
        valor -= 20
        cont20 += 1
    while 10 <= valor < 20:
        valor -= 10
        cont10 += 1
    while 1 <= valor < 10:
        valor -= 1
        cont1 += 1


print(f'Você receberá:')
print(f'{cont50} notas de R$50.')
print(f'{cont20} notas de R$20.')
print(f'{cont10} notas de R$10.')
print(f'{cont1} notas de R$1.')





