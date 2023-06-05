numcont = int(input("Digite o número da sua conta: "))
saldo = float(input("Digite seu saldo: "))

if saldo < 0:
    print(f"Conta número {numcont} esta com o saldo negativo.")
elif saldo >= 0:
    print(f"Conta com o número {numcont} está com saldo normal.")