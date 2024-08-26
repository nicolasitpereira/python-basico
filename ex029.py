vel = int(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('ACIMA DO LIMITE!! VOCÊ FOI MULTADO!!')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Prossiga! Dirija com segurança.')
