num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num1 == num2:
    print("Esses números são iguais")
elif num1 > num2:
    print(f"O {num1} é maior que o {num2}")
else:
    print(f"O {num2} é maior que o {num1}")