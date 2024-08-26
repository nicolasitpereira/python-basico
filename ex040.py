nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))

if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0 or nota3 > 10 or nota3 < 0 or nota4 > 10 or nota4 < 0:
    print('Nota invalida! Todas as notas precisam estar entre 0 e 10.')
else:
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print('Sua media foi {}'.format(media))
    if media >= 7:
        print('Você foi APROVADO! parabens.')
    elif media >= 4:
        print('Você está de RECUPERAÇÃO!')
    else:
        print('Você está REPROVADO!')

