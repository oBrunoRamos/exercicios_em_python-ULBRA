num_1_e_50 = 0
div_4 = 0

tot40 = 0
soma_40 = 0


for c in range(1, 100 ** 100):

    num = input(f'\nDigite o {c}° número (Digite "0" para parar o loop): ')

    while num == '':
        print('\n[ERRO] POR FAVOR DIGITE UM NÚMERO')
        num = input(f'Digite o {c}° número (Digite "0" para parar o loop): ')


    num = float(num)

    if num == 0:
        break
    
    if num >= 50 and num <= 150: 
        num_1_e_50 += 1

    if num % 4 == 0:
        div_4 += 1

    if num < 40:
        soma_40 += num
        tot40 += 1

media = soma_40 / tot40

print(f'\n Quantos números entre 50 e 150 foram digitados: {num_1_e_50}')
print(f'\n Quantos números divisíveis por 4 foram digitados: {div_4}')
print(f'\n A média dos números menores que 40: {media}')