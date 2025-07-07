#Super Progressão Aritmética v3.0

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

termo = a1
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print(termo, end=' -> ')
        termo += r
        contador += 1

    print('pausa')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Fim com {total} termos mostrados')
