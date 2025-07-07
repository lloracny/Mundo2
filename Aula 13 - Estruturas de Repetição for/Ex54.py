#Grupo da Maioridade

from datetime import date

maioridade = 0
menoridade = 0

for i in range(1,8):
    nasc = int(input(f'Insira o {i}ª ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f'{maioridade} pessoas são maiores de idade.')
print(f'{menoridade} pessoas são menores de idade.')

