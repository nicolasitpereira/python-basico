print('-'*26)
print('Sequência de Fibonacci')
print('-'*26)
numero = int(input('Qunatos termos Você quer mostrar? '))
termo1 = 0
termo2 = 1
print('_'*24)
print('{}  -->  {}'.format(termo1, termo2), end='')
cont = 3

while cont <= numero:
    termo3 = termo1 + termo2
    print('  -->  {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('FIM')
