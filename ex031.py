dist = float(input('Qual a distância da sua viagem? '))
if dist <= 200:
    calc = 0.50 * dist
else:
    calc = 0.45 * dist
    print('DESCONTO PARA VIAGENS ACIMA DE 200KM')
print('Você pagará R${:.2f} em sua passagem.'.format(calc))
