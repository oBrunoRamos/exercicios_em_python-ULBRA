totVelo = 0
totVeic = 0

somaValor = 0
veicSemMulta = 0
veicMultMed = 0
veicMultGrav = 0
veicMultGravss = 0

for i in range(1, 100**100):
    velocidade = input('\nDigite a velocidade do veículo: ')

    if velocidade == '':
        print('\nDigite um velocidade válida.')
        continue

    if int(velocidade) < 0:
        break

    velocidade = int(velocidade)
    totVeic += 1
    totVelo += velocidade
    if velocidade < 80 and velocidade > 40:
        print('Sem multa, diríja com cuidado')
        veicSemMulta +=1

    elif velocidade < 40:
        print('Transitar em velocidade inferior à metade da velocidade máxima da rodovia.  R$130,16. Multa média.')
        veicMultMed +=1
        somaValor += 130.16

    elif velocidade > 80 and velocidade < 85:
        print('Dentro da margem de erro, sem multa.')
        veicSemMulta +=1        

    elif velocidade <= 80 + (80*0.20):
        print('Acima do limite permitido: R$130,16. Multa média')
        veicMultMed +=1
        somaValor +=130.16

    elif velocidade < 80 + (80*0.50):
        print('Acima do limite permitido: R$195,23. Multa grave.')
        veicMultGrav += 1
        somaValor += 195.23

    elif velocidade >= 80 + (80*0.50):
        print('Acima do limite permitido: R$880,41. Multa gravíssima.')
        veicMultGravss += 1
        somaValor += 880.41

media = totVelo / totVeic


print(f'\nVeiculos sem multas: {veicSemMulta}')
print(f'Veiculos com multa média: {veicMultMed}')
print(f'Veículos xom multa grave: {veicMultGrav}')
print(f'Veículos com multa gravíssima: {veicMultGravss}')
print(f'Total de todas as multas: R${somaValor}')
print(f'Velocidade média na rodovia: {media}')