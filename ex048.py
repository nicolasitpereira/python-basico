s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1

print('Aa soma de todos os {} valores solicitados é {}'.format(cont, s))