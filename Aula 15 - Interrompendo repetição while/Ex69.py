#Análise de dados do grupo

resp = 'S'
maior18 = 0
homem = 0
mulherMenos20 = 0

while resp == 'S':
    print('-'*20)
    print('CADASTRAMENTO')
    print('-' * 20)
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M/F): ').strip().upper()[0]
    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulherMenos20 += 1

print(f'Existem {maior18} pessoas com mais de 18 anos cadastradas.')
print(f'Existem {homem} homens cadastrados.')
print(f'Existem {mulherMenos20} mulheres com menos de 20 anos.')