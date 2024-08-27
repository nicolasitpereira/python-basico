maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
soma = 0

for x in range(1, 5):
    print('---- {}° Pessoa ----'.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if x == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    elif idade > maioridadehomem and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = soma / 4
print('A media de idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
