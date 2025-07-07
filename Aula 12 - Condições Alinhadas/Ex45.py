#GAME: Pedra Papel e Tesoura

import random

palavras = ['pedra', 'papel', 'tesoura']
opcao_pc = random.choice(palavras).upper()

print('Escolha qual irá jogar:')
opcao_jogador = input().upper()


if opcao_pc == opcao_jogador:
    print('EMPATE')
elif opcao_jogador == "PAPEL" and opcao_pc == "PEDRA" or opcao_jogador == "PEDRA" and opcao_pc == "TESOURA" or opcao_jogador == 'TESOURA' and opcao_pc == "PAPEL":
    print('Você ganhou!')
else:
    print('Você perdeu!')
print(f'O computador escolheu {opcao_pc}')
print(f'O jogador escolheu {opcao_jogador}')

