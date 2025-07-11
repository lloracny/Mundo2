cont = 0
soma = 0

while True:
    num = int(input('Informe um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Foram digitados {cont} números')
print(f'A soma dos números digitados é {soma}')
