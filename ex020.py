from random import shuffle
p1 = input('Primeira pessoa: ')
p2 = input('Segunda pessoa: ')
p3 = input('Terceira pessoa: ')
p4 = input('Quarta pessoa: ')
lista = [p1, p2, p3, p4]
shuffle(lista)
print('A ordem será: {}'.format(lista))
