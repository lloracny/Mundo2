#Soma ímpares múltiplos de três

soma = 0
cont = 0

for i in range (1, 500):
    if i % 2 != 0 and i % 3 == 0:
        print(i)
        cont += 1
        soma += i

print('-'*10)
print(f'A soma dos {cont} valores é: {soma}')


