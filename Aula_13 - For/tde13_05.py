nul = 0
pos = 0
neg = 0
for c in range(1, 11):
    num = float(input('\nDigite um número positivo, nulo ou negativo: '))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    elif num == 0:
        nul += 1
print(f'\nTotal de números positivos: {pos}')
print(f'\nTotal de números negativos: {neg}')
print(f'\nTotal de números nulos: {nul}\n')