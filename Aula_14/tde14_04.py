sup30 = 0

entr10e25 = 0
soma_alt = 0

menor18 = 0
soma_peso = 0

menos_50 = 0

for c in range(1, 21):

    
    idade = input(f'\nDigite a idade da {c}° pessoa: ')
    while (idade == '') or (int(idade) <= 0) or (int(idade) > 120):
        print('\n[ERRO] POR FAVOR DIGITE UMA IDADE VÁLIDA')
        idade = input(f'Digite a idade da {c}° pessoa: ')

    altura = input(f'\nDigite a altura da {c}° pessoa: ')
    while (altura == '') or (float(altura) < 0.70) or (float(altura) > 2.50):
        print('\n[ERRO] POR FAVOR DIGITE UMA ALTURA VÁLIDA')
        altura = input(f'Digite a altura da {c}° pessoa: ')

    peso = input(f'\nDigite a peso da {c}° pessoa: ')
    while (peso == '') or (float(peso) <= 0) or (float(peso) > 595):
        print('\n[ERRO] POR FAVOR DIGITE UM PESO VÁLIDO')
        peso = input(f'Digite a peso da {c}° pessoa: ')



    idade = int(idade)
    altura = float(altura)
    peso = float(peso)

    if idade > 30: 
        sup30 += 1

    if idade > 10 and idade < 25: 
        entr10e25 += 1 
        soma_alt += altura

    if idade < 18:
        menor18 += 1
        soma_peso += peso

    if peso < 50:
        menos_50 += 1
print('\n')
print(f'\nA quantidade de pessoas analisadas superior a 30 anos é de: {sup30}')
print(f'\nA média das alturas das pessoas com idade entre 10 e 25 anos é de: {soma_alt / entr10e25}')
print(f'\nA média de peso das pessoas menores de idade é de: {soma_peso/menor18}')
print(f'\nA percentagem de pessoas com peso inferior a 50 quilos entre todas as pessoas analisadas é de: {(menos_50/20)*100}%')