altura = float(input("Digite a altura do triângulo: "))
base = float(input("Digite a base do triângulo: "))

if base == altura:
    area = (1,732050807568877 * base ** 2) / 4

elif base != altura:
    area = (altura * base) / 2

print("A área de um triângulo com esses catetos é: " + str(area))