vel = int(input("Digite a velocidade do carro: "))

print('Velocidade máxima permitida: 80Km/h')
print(f'Velocidade do carro: {vel}Km/h')

if vel < 80:
    print('Velocidade permitida')
elif vel <= (((80 * 7)/100)+ 80):
    print(f'Velocidade ainda permitida.')
elif vel > (((80 * 7)/100)+ 80) and vel <= (((80 * 20)/100)+ 80):
    print("Velocidade acima do permitido.")
    print("Até 20% acima do limite.")
    print('Multa média. Valor: R$130,16')
elif vel > (((80 * 20)/100)+ 80) and vel <= (((80 * 50)/100)+ 80):
    print("Velocidade acima do permitido.")
    print("De 20% até 50% acima do limite.")
    print('Multa grave. Valor: R$195,23')
else:
    print("Velocidade acima do permitido.")
    print("Até 50% acima do limite.")
    print('Multa gravíssima. Valor: R$880,41')