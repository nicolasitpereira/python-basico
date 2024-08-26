from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
option = int(input('Qual é sua jogada? '))
print('O computador escolheu {}.'.format(itens[computador ]))
print('Jogador escolheu {}.'.format(itens[option]))
if computador == 0:
    if option == 0:
        print('EMPATE')
    elif option == 1:
        print('VOCÊ GANHOU')
    elif option == 2:
        print('VOCÊ PERDEU')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if option == 0:
        print('VOCÊ PERDEU')
    elif option == 1:
        print('EMPATE')
    elif option == 2:
        print('VOCÊ GANHOU')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if option == 0:
        print('VOCÊ GANHOU')
    elif option == 1:
        print('VOCÊ PERDEU')
    elif option == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
