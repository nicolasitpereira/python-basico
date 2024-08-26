km = float(input('Quantos KM foram percorridos? '))
d = int(input('Qunatidade de dias nos quais ele foi alugado? '))
calc = (0.15 * km) + (60 * d)
print('Você pagará R${:.2f} pelo aluguel do carro.'.format(calc))
