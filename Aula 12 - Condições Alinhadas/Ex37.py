#Conversor de Bases Numéricas

num = int(input('Informe um número inteiro: '))
print('Qual será a base de conversão?')
print("""[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL""")
conversao = input()

if conversao == '1':
    binario = bin(num)
    print(f'O número {num} digitado em binário é: {binario[2:]}')
elif conversao == '2':
    octal = oct(num)
    print(f'O número {num} digitado em octal é: {octal}')

elif conversao == '3':
    hexadecimal = hex(num)
    print(f'O número {num} digitado em hexadecimal é: {hexadecimal}')

else:
    print('Valor inválido. Deve ser um número inteiro.')
    