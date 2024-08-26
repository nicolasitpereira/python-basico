print('===== SIMULADOR LOJA =====')
valor = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
option = int(input('Qual é sua opção? '))
if option == 1:
    desc = valor - (10 * valor / 100)
    print('Pagamento será: R${:.2f}'.format(desc))
elif option == 2:
    desc = valor - (5 * valor / 100)
    print('Pagamento será: R${:.2f}'.format(desc))
elif option == 3:
    print('Pagamento será: R${:.2f}'.format(valor))
elif option == 4:
    valor = valor + (20 * valor / 100)
    print('Pagamento será: R${:.2f}'.format(valor))
else:
    print('Por favor, Digite uma opção válida.')