num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if  num1 > num2:
    res = num1 - num2
else:
    res = num2 - num1

print(f"A diferença desses números é de {res}")