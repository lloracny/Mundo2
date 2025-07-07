#Gerenciador de Pagamentos

valor = float(input('Digite o valor do produto: '))
print("""Qual será a condição de pagamento?
[1] Á VISTA DINHEIRO/CHEQUE
[2] Á VISTA NO CARTÃO
[3] EM ATÉ 2X NO CARTÃO
[4] EM 3X OU MAIS NO CARTÃO""")
condicao = input()

if condicao == '1':
    pgto = valor * 0.90
    print('Você ganhou 10% de desconto!')
    print(f'Você pagará R${pgto:.2f} pelo produto!')
elif condicao == '2':
    pgto = valor * 0.95
    print('Você ganhou 5% de desconto!')
    print(f'Você pagará R${pgto:.2f} pelo produto!')
elif condicao == '3':
    print(f'Você pagará R${valor:.2f} pelo produto!')
    print(f'Sua compra será parcelada em 2x de R${valor/2}')
elif condicao == '4':
    pgto = valor * 1.20
    print('Você pagará 20% de juros!')
    print(f'Você pagará R${pgto:.2f} pelo produto!')
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    print(f'Sua compra de R${pgto:.2f} será parcelada em {parcela}x de R${pgto/parcela:.2f} ')