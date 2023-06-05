totNumeros = 0
for c in range(50, 251):
    if c % 2 == 1:
        continue 
    totNumeros +=c
print(f'A soma total de todos os números pares na faixa de 50 até 250 é: {totNumeros}')