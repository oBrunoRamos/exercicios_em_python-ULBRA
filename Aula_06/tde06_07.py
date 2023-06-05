func = str(input("Digite o nome do funcionário: "))
sal = float(input("Digite o salário atual do funcionário: "))

if sal >= 0 and sal <= 400:
    aum = (sal * 15) / 100
    print(f"Funcionário: {func}")
    print(f"Você terá um aumeto de 15%. Seu salário ficará {sal + aum} reais.")
elif sal > 400 and sal <= 700:
    aum = (sal * 12) / 100
    print(f"Funcionário: {func}")
    print(f"Você terá um aumeto de 12%. Seu salário ficará {sal + aum} reais.")
elif sal > 700 and sal <= 1000:
    aum = (sal * 10) / 100
    print(f"Funcionário: {func}")
    print(f"Você terá um aumeto de 10%. Seu salário ficará {sal + aum} reais.")
elif sal > 1000 and sal <= 1800:
    aum = (sal * 7) / 100
    print(f"Funcionário: {func}")
    print(f"Você terá um aumeto de 7%. Seu salário ficará {sal + aum} reais.")
elif sal > 1800 and sal <= 2500:
    aum = (sal * 4) / 100
    print(f"Funcionário: {func}")
    print(f"Você terá um aumeto de 4%. Seu salário ficará {sal + aum} reais.")
else: 
    print(f"Funcionário: {func}")
    print("Sem aumento.")