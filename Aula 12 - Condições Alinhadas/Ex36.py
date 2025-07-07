#Aprovando Empréstimo

valor_casa = float(input('Qual o valor da casa? ' ))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos o comprador irá pagar a casa? '))

meses = anos * 12

prestacao = valor_casa / meses

if prestacao > salario * 0.3:
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aceito!')
    