import math
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

if num1 >= 0:
    raiz = math.sqrt(num1)
    print(f"\nA raiz quadrada de {num1} é {raiz}.")
else:
    quad = num1 ** 2
    print(f"O número {num1} elevado na segunda potência é {quad}.")

if num2 > 10 and num2 < 100:
    print(f"O número {num2} está entre 10 e 100 - INTERVALO PERMITIDO.")

if num3 < num2:
    s = num2 - num3
    print(f"A diferença entre os números {num2} e {num3} é de {s}.")
else:
    s = num3 + num2
    print(f"A noma dos númeors {num2} e {num3} é {s}.") 
