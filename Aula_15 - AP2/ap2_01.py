valorCarro = input('\nDigite o valor do carro: ')
for c in range(100**100):
    if valorCarro != '':
        break
    else:
        print('\n VAlor de carro não reconhecido.')
        valorCarro = input('Digite o valor do carro: ')

valorCarro = float(valorCarro)

pagamento = str(input('A forma de pagamenento será à vista ou parcelado? '))
acrescimo = 0
desconto = 0

for i in range(1, 100**100):
    if pagamento == 'a vista' or pagamento == 'à vista' or pagamento == 'parcelado':
       break

    else:
        print('\n não entedi, digite novamente')
        print('Digite "a vista" ou "parcelado".')
        pagamento = str(input('A forma de pagamenento será à vista ou parcelado? '))

        continue
   
if pagamento == 'a vista' or pagamento == 'à vista':
    desconto = valorCarro * 0.20
    
elif pagamento == 'parcelado':
    parcelas = int(input('Digite em quantas parcelas voce deseja fazer: opções(6, 12, 18 24, 30, 36, 42, 48, 54, 60) '))

    for c in range(100**100):

        if parcelas == 6:
            acrescimo = valorCarro * 0.03
            break

        elif parcelas == 12:
            acrescimo = valorCarro * 0.06
            break

        elif parcelas == 18:
            acrescimo = valorCarro * 0.09
            break

        elif parcelas == 24:
            acrescimo = valorCarro * 0.12
            break

        elif parcelas == 30:
            acrescimo = valorCarro * 0.15
            break

        elif parcelas == 36:
            acrescimo = valorCarro * 0.18
            break

        elif parcelas == 42:
            acrescimo = valorCarro * 0.21
            break

        elif parcelas == 48:
            acrescimo = valorCarro * 0.24
            break

        elif parcelas == 54:
            acrescimo = valorCarro * 0.27
            break

        elif parcelas == 60:
            acrescimo = valorCarro * 0.30
            break
          
        else:
            print('\nDigite um número de parcelas válido.')
            parcelas = int(input('Digite em quantas parcelas voce deseja fazer: opções(6, 12, 18 24, 30, 36, 42, 48, 54, 60) '))

            continue
        
if desconto == 0 and acrescimo == 0:
    print('[erro]')
    print('Reinicie o programa')
elif desconto > 0 and acrescimo == 0:
    print(f'\nO valor a total a pagar será de: R${valorCarro-desconto} .')
elif desconto == 0 and acrescimo > 0:
    print(f'\nO valor a total a pagar será de: R${valorCarro+acrescimo} .')
