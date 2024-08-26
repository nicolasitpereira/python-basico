from random import choice
p1 = input('Primeira pessoa: ')
p2 = input('Segunda pessoa: ')
p3 = input('Terceira pessoa: ')
p4 = input('Quarta pessoa: ')
lista = [p1, p2, p3, p4]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))
