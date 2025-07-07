#Soma dos pares

pares = 0
soma = 0

for i in range (1,7):
    num = int(input(f'Informe o {i}ª numero: '))
    if num % 2 == 0:
        pares += 1
        soma += num

print(f'A soma dos valores pares é: {soma}')
print(f'Dentre os 6 valores, {pares} são valores pares')




