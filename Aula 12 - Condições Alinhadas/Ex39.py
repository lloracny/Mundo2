#Alistamento Militar

from datetime import date
nasc = int(input('Informe seu ano de nascimento: '))

atual = date.today().year
idade = atual - nasc

if idade < 18:
    print('Você ainda vai se alistar ao serviço militar!')
    tempo = 18 - idade
    print(f'Faltam {tempo} anos para você se alistar!')
elif idade == 18:
    print('Já é hora de você de alistar!')
else:
    print('Você já passou do tempo de se alistar!')
    tempo = idade - 18
    print(f'Já se passaram {tempo} anos do ideal!')
