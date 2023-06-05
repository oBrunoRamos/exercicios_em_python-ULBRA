n1 = float(input("Digite um valor entre 100 e 200: "))

if n1 < 100 or n1 > 200:
    print("Valor digitado invalido, reinicie o programa.")
else:
    c = 0
    while n1 != 0:
        print("Para parar o programa digite '0' ")
        n1 = float(input("Digite um valor entre 100 e 200: "))
        c +=1
    
    print(f"Quantidade de numeros digitados: {c}")