peso = float(input('Digite seu peso: (KG) '))
altura= float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO do Peso ideal.')
elif 18.5 <= imc < 25:
    print('Peso IDEAL.')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
