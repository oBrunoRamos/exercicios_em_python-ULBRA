num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num1 > num2:
    c = "soma"
    s = num1 + num2
else:
    c = "subtração"
    s = num1 - num2

print(f"Com esses dos valores a {c} é de resultado {s}")