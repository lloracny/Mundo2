#Classificando Atletas

from datetime import date
nasc = int(input('Insira o ano de nascimento: '))

atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('Você está na categoria MIRIM!')
elif idade <= 14:
    print('Você está na categoria JUNIOR!')
elif idade <= 19:
    print('Você está na categoria SENIOR!')
else:
    print('Você está na categoria MASTER!')

    