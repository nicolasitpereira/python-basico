num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print('\nO número {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('NÚMERO PRIMO')
else:
    print('NÃO É PRIMO')
