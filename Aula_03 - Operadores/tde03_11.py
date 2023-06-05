num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))

mult = num1 * num2 * num3 * num4 * num5
soma = num1 + num2 + num3 + num4 + num5
sub = num1 - num2 - num3 - num4 - num5
tot_soma = soma + mult + sub

print("Produto da multiplicação = " + str(mult) + ", resultado da soma = " + str(soma) + ", resultado da subtração = ", sub,", soma de todos os resultados = ", tot_soma,".")