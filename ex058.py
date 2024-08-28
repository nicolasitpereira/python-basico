from random import randint
computador = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Tente adivinhar...')
tent = 0
acertou = False
while not acertou:
    num = int(input('Qual seu palpite? '))
    if num > 10 or num < 0:
        print('Por favor, digite numeros entre 0 e 10')
    else:
        tent += 1
        if num > computador:
            print('Menos... tente novamente.')
        elif num < computador:
            print('Mais... tente novamente.')
        else:
            print('Acertou com {} tentativas. Parabéns.'.format(tent))
            break
