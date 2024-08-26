salario = float(input('Qual é o salário atual?'))
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Salario atual: R${:.2f}\nNovo salario R${:.2f}'.format(salario, novo))
