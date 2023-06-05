temp = float(input("Digite o tempo da viagem:(HORAS) "))
velo_media = int(input("Digite a velocidade média do carro durante a viagem: "))

dist = temp * velo_media
litros = dist / 12

print("Em uma viagem de " + str(temp) + " horas, com uma velocidade média de " + str(velo_media) + "Km/h, considerando que o carro gaste um total de 1 litro a cada 12km, você gastará nessa viagem " + str(litros) + "litros.")