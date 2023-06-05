NumA = float(input("Digite o valor de A: "))
NumB = float(input("Digite o valor de B: "))

if NumA > NumB:
    s = NumA + 100
else:
    s = NumB + 100

print(f"somando o maior valor à 100 o resultado dá: {s}")