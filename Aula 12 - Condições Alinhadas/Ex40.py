#Aquele clássico da Média

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Você está reprovado!')
elif 5 >= media < 7:
    print('Você está de recuperação!')
elif media >= 7:
    print('Você está aprovado!')

print(f'Sua media foi de {media}')
