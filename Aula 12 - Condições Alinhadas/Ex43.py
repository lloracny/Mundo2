#Índice de Massa Corporal

peso = float(input('Informe seu peso em KG: '))
altura = float(input('Informe sua altura em m: '))

imc  = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc <30:
    print('Você está com sobrepeso!')
elif 30 <= imc <40:
    print('Você está com obesidade!')
elif imc >= 40:
    print('Você está com obesidade mórbida!')

print(f'Seu IMC é {imc:.2f}')