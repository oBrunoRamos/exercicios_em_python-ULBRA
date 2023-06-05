i = int(input("Digite um número entre um e três: "))
a = float(input("Digite um número qualquer: "))
b = float(input("Digite um número qualquer: "))
c = float(input("Digite um número qualquer: "))

if i == 1:
    if a > b and a > c:
        n3 = a
        if b > c:
            n2 = b
            n1 = c
        else:
            n2 = c
            n1 = b
    elif b > a and b > c:
        n3 = b
        if a > c:
            n2 = a
            n1 = c
        else:
            n2 = c
            n1 = a
    else:
        n3 = c
        if b > a:
            n2 = b
            n1 = a
        else:
            n2 = a
            n1 = b
    print(f"{n1}, {n2}, {n3}")
elif i == 2:
    if a > b and a > c:
        n3 = a
        if b > c:
            n2 = b
            n1 = c
        else:
            n2 = c
            n1 = b
    elif b > a and b > c:
        n3 = b
        if a > c:
            n2 = a
            n1 = c
        else:
            n2 = c
            n1 = a
    else:
        n3 = c
        if b > a:
            n2 = b
            n1 = a
        else:
            n2 = a
            n1 = b
    print(f"{n3}, {n2}, {n1}")
elif i == 3:
    if a > b and a > c:
        n3 = a
        if b > c:
            n2 = b
            n1 = c
        else:
            n2 = c
            n1 = b
    elif b > a and b > c:
        n3 = b
        if a > c:
            n2 = a
            n1 = c
        else:
            n2 = c
            n1 = a
    else:
        n3 = c
        if b > a:
            n2 = b
            n1 = a
        else:
            n2 = a
            n1 = b
    print(f"{n1}, {n3}, {n2}")
else:
    print('[ERRO]')