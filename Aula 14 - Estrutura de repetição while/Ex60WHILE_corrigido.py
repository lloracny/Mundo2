#Cálculo do Fatorial com WHILE

n = int(input('Digite um valor para calcular seu fatorial: '))
f = 1

print(f'Calculando {n}!', end='')
print()
while n > 0:
    print(f'{n}', end="")
    print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1

print(f'{f}')