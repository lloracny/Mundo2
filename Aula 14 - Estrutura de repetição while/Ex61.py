#Progressão Aritmética v2.0

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

contador = 0

while contador < 10:
    termo = a1 + contador * r
    contador += 1
    print(termo, end=' ')
