num = float(input("Digite qualquer número. Positivo ou negativo: "))

if num < 0:
    pos = "negativo"
else:
    pos = "positivo"
    
if num % 2 == 0:
    PoI = "par"
else:
    PoI = "ímpar"

print(f"O número {num} é {pos} e é {PoI}!!")