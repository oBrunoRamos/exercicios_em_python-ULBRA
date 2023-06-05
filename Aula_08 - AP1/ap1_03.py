fatu = float(input("Digite o faturamento da empresa: "))
cust = float(input("Digite os custos da empresa: "))

pis = fatu * 0.065
cof = fatu * 0.3

lucro = fatu - (pis+cof+cust)

print(f"Imposto (PIS): R${pis}")
print(f"Imposto (COFINS): R${cof}")
print(f"Lucro total da empresa: R${lucro}")