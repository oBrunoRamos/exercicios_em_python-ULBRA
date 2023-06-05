nota = float(input("Digite sua nota final. Entre 0 e 10. = "))

if nota >= 6 and nota <= 10:
    print("Aprovado!!")
elif nota <= 5:
    print("Reprovado.")
else:
    print("Erro!! Valor inválido.")