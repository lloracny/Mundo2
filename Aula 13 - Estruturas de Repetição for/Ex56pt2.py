#Analisador Completo

somaidade = 0
nomeDoMaisVelho = ''
idadeHomemMaisVelho = 0
contagemMulheresMenos20 = 0

for p in range (1, 5):
    nome = input(f'Digite o {p}° nome: ').capitalize()
    idade = int(input(f'Digite a {p}° idade: '))
    sexo = input(f'Digite o {p}° sexo (M/F): ').upper()

    somaidade += idade

    if p == 1 and sexo == 'M':
        nomeDoMaisVelho = nome
        idadeHomemMaisVelho = idade
    if idade > idadeHomemMaisVelho and sexo == 'M':
        nomeDoMaisVelho = nome
        idadeHomemMaisVelho = idade
    if sexo == 'F' and idade < 20:
        contagemMulheresMenos20 += 1

mediaidade = somaidade / 4

print(f'A média de idade é: {mediaidade}.')
print(f'O homem mais velho se chama {nomeDoMaisVelho} e ele tem {idadeHomemMaisVelho} anos.')
print(f'Há {contagemMulheresMenos20} mulheres com menos de 20 anos.')
