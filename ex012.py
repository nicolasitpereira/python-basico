preco = float(input('Qual o preço do produto? '))
calc = 5 / 100 * preco
npreco = preco - calc
print('Valor do produto SEM desconto: R${}\nValor do produto COM desconto de 5%: R${}'.format(preco, npreco))