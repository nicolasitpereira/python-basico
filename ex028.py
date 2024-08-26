from random import randint
computador = randint(0, 5)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
n = int(input('Digite um nùmero de 0 a 5: '))
if n == computador:
    print('Parabens! Você acertou.')
else:
    print('Você errou! O numero que pensei foi {}. Tente novamente.'.format(computador))
