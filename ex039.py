from datetime import date
atual = date.today().year
print('-=-'*10)
print('ALISTAMENTO MILITAR')
print('-=-'*10)
sexo = int(input('Qual seu Sexo? (1 para masculino) ou (2 para feminino) : '))
if sexo == 1:
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade < 18:
        restam = 18 - idade
        print('Ainda faltam {} ano(s)  para o seu alistamento.'.format(restam))
        print('Seu alistamento será em {}.'.format(atual + restam))
    elif idade > 18:
        restam = idade - 18
        print('Você ja deveria ter se alistado a {} ano(s).'.format(restam))
        print('Seu ano de alistamento foi em {}.'.format(atual - restam))
    else: #se for == a 18
        print('Você tem que se alistar IMEDIATAMENTE!')
elif sexo == 2:
    print('Alistamento opcional!')
    optional = int(input('Deseja se alistar? (1 para SIM) (2 para NÃO) : '))
    if optional == 1:
        nasc = int(input('Ano de nascimento: '))
        idade = atual - nasc
        print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
        if idade < 18:
            restam = 18 - idade
            print('Ainda faltam {} ano(s)  para o seu alistamento.'.format(restam))
            print('Seu alistamento será em {}.'.format(atual + restam))
        elif idade > 18:
            restam = idade - 18
            print('Você ja deveria ter se alistado a {} ano(s).'.format(restam))
            print('Seu ano de alistamento foi em {}.'.format(atual - restam))
        else:  # se for == a 18
            print('Você tem que se alistar IMEDIATAMENTE!')
    elif optional == 2:
        print('Ok! tenha um Bom Dia!')
    else:
        print('Por favor Digite um valor Valido!')
else:
    print('Número invalido. Tente novamente.')
