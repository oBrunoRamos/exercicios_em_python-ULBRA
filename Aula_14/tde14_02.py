menor_v = 100*100
maior_v = 0
soma = 0
primos = 0

for c in range(1, 13):
    num = input(f'\n Digite o {c}° número: ')
    while num == '':
        print('\n[ERRO] POR FAVOR DIGITE UM NÚMERO')
        num = input(f' Digite o {c}° número: ')

    num = float(num)
    soma += num

    if num > maior_v:
        maior_v = num

    if num < menor_v:
        menor_v = num

    primo = 0
    for i in range(2, int(num)):
        if num % i == 0:
            primo += 1

    if primo == 0:
        primos += num

    
print(soma)
media = soma / c      
print(f'\nMenor número digitado: {menor_v}')
print(f'\nMaior númeor digitado: {maior_v}')
print(f'\nMédia dos números lidos: {media}')
print(f'\nA soma de todos os números primos digitados é de: {primos}')