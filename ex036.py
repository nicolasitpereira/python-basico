valorCasa = float(input('Valor da casa: R$'))
renda = float(input('Sua renda mensal: R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = valorCasa / (anos * 12)
calc = renda * 30 / 100
print('Para financiar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valorCasa, anos, prest))
if prest <= calc:
    print('EMPRÉSTIMO CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!!')
