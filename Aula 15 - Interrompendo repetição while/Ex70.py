#Estatísticas em produtos

from time import sleep
total_gasto = 0
maior1000 = 0
cont = 0
nome_barato = ''
preco_barato = 0
while True:
    print('-'*20)
    print('CADASTRO DE PRODUTOS')
    print('-' * 20)
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto informado: '))
    cont += 1
    total_gasto += preco
    resp = ' '
    if preco > 1000:
        maior1000 += 1
    if cont == 1:
        nome_barato = nome
        preco_barato = preco
    else:
        if preco < preco_barato:
            preco_barato = preco
            nome_barato = nome


    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print('-'*30)
print('Fim do Programa')
print('-'*30)
sleep(1)
print(f'Você gastou R${total_gasto:.2f} em suas compras.')
print(f'{maior1000} produto(s) custam mais de R$1000.')
print(f'O produto mais barato é: {nome_barato}, no valor de R${preco_barato:.2f}')





