from time import sleep
opcao = 0
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
while opcao != 5:

    print('[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'          #opcoes ////
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa')

    opcao = int(input('>>>>> Qual é sua opção? '))   #user option

    if opcao == 1:   #soma ////
        soma = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, soma))

    elif opcao == 2:   #multiplicação ////
        mult = v1 * v2
        print('A multiplicação entre {} x {} é {}'.format(v1, v2, mult))

    elif opcao == 3:   #verificar maior ////
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior é {}'.format(v1, v2, maior))

    elif opcao == 4:   #novos nums ////
        print('Digite os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))

    elif opcao == 5:   #finalizar programa ////
        print('Finalizando...')
    else:   #sair ////
        print('Valor invalido. Tente novamente')
    print('='*30)
    sleep(2)

print('Você saiu do programa.')
