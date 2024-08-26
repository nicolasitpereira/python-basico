from datetime import date
maior = 0
menor = 0
for x in range(1, 8):
    ano = int(input('Ano de nascimento {}° pessoa: '.format(x)))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E {} pessoas menores de idade.'.format(menor))
