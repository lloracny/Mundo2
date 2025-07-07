nome = str(input('Digite seu nome: '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem normal!')
elif nome in 'Ana Juliana Mariana':
    print('Que nome lindo!')
else:
    print('Seu nome é feio!')

print(f'Tenha um bom dia {nome}')