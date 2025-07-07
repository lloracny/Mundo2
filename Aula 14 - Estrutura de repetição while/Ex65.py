#Maior e Menor valores

r = 'S'
somanum = 0
maior = 0
menor = 0
cont = 0

while r == 'S':
    num = float(input('Informe um número: '))
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    cont += 1
    somanum += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


media = somanum / cont
print(f'A média dos números informados é: {media}')

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')