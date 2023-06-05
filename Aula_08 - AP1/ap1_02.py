velo = int(input("Digite a velocidade do veículo(Km/h): "))

if velo < 100:
    if velo <= 80:
        print(f"Velocidade {velo}Km/h. Dentro da velocidade permitida.")
    elif velo > 80 and velo < 87:
        print(f"Velocidade {velo}Km/h.Margem de erro localizada, multa não aplicada")
    elif velo > 87 and velo <= 80 + (80*0.2):
        print(f"Velocidade {velo}Km/h.Acima do limite permitido: R$130,16. Multa média.")
    elif velo < 100 and velo >= 80 + (80*0.2):
        print(f"Velocidade {velo}Km/h.Acima do limite permitido: R$195,23. Multa grave.")
else: 
    if velo < 107:
        print(f"Velocidade {velo}Km/h.Margem de erro localizada, multa não aplicada")
    elif velo > 107 and velo < 120:
        print(f"Velocidade {velo}Km/h.Acima do limite permitido: R$195,23. Multa grave.")
    else:
        print(f"Velocidade {velo}Km/h.Acima do limite permitido: R$880,41. Multa gravíssima.")