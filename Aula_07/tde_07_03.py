n1 = float(input("Digite um número qualquer: "))
n2 = float(input("Digite um número qualquer: "))
n3 = float(input("Digite um número qualquer: "))

if n1 < n2 and n1 > n3:
    print(f"O numero {n1} está entre {n3} e {n2}")
elif n1 > n2 and n1 < n3:
    print(f"O número {n1} está entre {n2} e {n3}")

if n2 < n1 and n2 > n3:
    print(f"O numero {n2} está entre {n3} e {n1}")
elif n2 > n1 and n2 < n3:
    print(f"O número {n2} está entre {n1} e {n3}")

if n3 < n2 and n3 > n1:
    print(f"O numero {n3} está entre {n1} e {n2}")
elif n3 > n2 and n3 < n1:
    print(f"O número {n3} está entre {n2} e {n1}")