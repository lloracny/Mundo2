#Analisando Triângulos v2.0

comp1 = float(input('Informe o 1º comprimento: '))
comp2 = float(input('Informe o 2º comprimento: '))
comp3 = float(input('Informe o 3º comprimento: '))

if comp1 + comp2 > comp3 and comp1 + comp3 > comp2 and comp2 + comp3 > comp1:
    print('\033[32mÉ possível formar um triângulo!\033[m')
    if comp1 == comp2 == comp3:
        print('O triâgulo a ser formado é equilátero!')
    elif comp1 == comp2 or comp1 == comp3 or comp2 == comp3:
        print('O triângulo a ser formado é isósceles!')
    elif comp1 != comp2 and comp1 != comp3 and comp2 != comp3:
        print('O triângulo a ser formado é escaleno!')

else:
    print('\033[31mNão é possível formar um triângulo!\033[m')
    