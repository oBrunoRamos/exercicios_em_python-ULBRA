
sup50inf60 = 0

idades150 = 0
altura150 = 0

OlhosAzuisCabcast = 0

ruivNVerd = 0

for c in range(1, 4):
    print('\n')
    print(f'\nPessoa n° {c}')
    idade = input(f'Digite sua idade: ')
    while (idade == '') or (int(idade) <= 0) or (int(idade) > 120):
        print('\n[ERRO] POR FAVOR DIGITE UMA IDADE VÁLIDA')
        idade = input(f'Digite sua idade: ')

    altura = input(f'Digite sua altura: ')
    while (altura == '') or (float(altura) < 0.70) or (float(altura) > 2.50):
        print('\n[ERRO] POR FAVOR DIGITE UMA ALTURA VÁLIDA')
        altura = input(f'Digite sua altura: ')

    peso = input(f'Digite seu peso: ')
    while (peso == '') or (float(peso) <= 0) or (float(peso) > 595):
        print('\n[ERRO] POR FAVOR DIGITE UM PESO VÁLIDO')
        peso = input(f'Digite seu peso: ')

    cor_olhos = str(input('Digite a cor de seus olhos (A-azul, P-preto,V-verde e C-castanho): '))
    while (cor_olhos == '') or (cor_olhos != ''):
        if (cor_olhos == 'a' or cor_olhos == 'A') or (cor_olhos == 'p' or cor_olhos == 'P') or (cor_olhos == 'v' or cor_olhos == 'V') or (cor_olhos == 'c' or cor_olhos == 'C'):
            break

        print('\n[ERRO] POR FAVOR DIGITE UMA RESPOSTA VÁLIDA')
        cor_olhos = str(input('Digite a cor de seus olhos (A-azul, P-preto,V-verde e C-castanho): '))        

    cor_cabelo = str(input('Digite a cor de seus cabelos (P-preto, C-castanho, L-louro e R-ruivo): '))
    while (cor_cabelo == '') or (cor_cabelo != ''): 

        if (cor_cabelo == 'p' or cor_cabelo == 'P') or (cor_cabelo == 'l' or cor_cabelo == 'L') or (cor_cabelo == 'c' or cor_cabelo == 'C') or (cor_cabelo == 'r' or cor_cabelo == 'R'):
            break

        print('\n[ERRO] POR FAVOR DIGITE UMA RESPOSTA VÁLIDA')
        cor_cabelo = str(input('\nDigite a cor de seus cabelos (P-preto, C-castanho, L-louro e R-ruivo): '))

    idade = int(idade)
    peso = float(peso)
    altura = float(altura)
    
    if idade > 50 and peso < 60:
        sup50inf60 += 1

    if altura < 1.5:
        idades150 += idade
        altura150 += 1

    if (cor_olhos == 'a' or cor_olhos == 'A' and cor_cabelo == 'c' or cor_cabelo == 'C'):
        OlhosAzuisCabcast += 1

    if (cor_cabelo == 'r' or cor_cabelo == 'R') and (cor_olhos != 'v' or cor_olhos != 'V'):
        ruivNVerd += 1



    

print(f'\n O total de pessoas com idade superior a cinquenta que possuem menos de 60kg é de {sup50inf60} pessoas.')
print(f'\n A média das idades de pessoas com a altura inferior a 1,50m é: {idades150/altura150}')
print(f'\n A percentagem de pessoas com olhos azuis entre todas as pessoas analizadas é de: {(OlhosAzuisCabcast / c) * 100}% ')
print(f'\n A quantidade de pessoas ruivas anlaizadas que não possui olhos azuis é de: {ruivNVerd}\n')