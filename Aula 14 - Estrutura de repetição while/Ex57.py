#Validação de Dados

s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite um valor: ')).strip().upper()[0]
    if s == 'M':
        print('Você é do sexo Masculino!')
    if s == 'F':
        print('Você é do sexo Feminino!')