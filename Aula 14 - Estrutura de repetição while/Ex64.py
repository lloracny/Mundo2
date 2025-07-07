#Tratando vários valores v1.0

n = 1
cont = 0
soma = 0

while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        cont += 1
        soma += n


print(f'Foram digitados {cont} números.')
print(f'A soma dos números digitados é de: {soma}')