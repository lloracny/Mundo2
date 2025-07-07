#Cálculo do Fatorial com WHILE

from math import factorial

valor = int(input('Digite um valor: '))
while valor != 0:
    fatorial = factorial(valor)
    valor -= 1
    print(fatorial)
