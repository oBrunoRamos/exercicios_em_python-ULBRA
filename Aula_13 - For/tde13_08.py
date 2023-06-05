pos = 0
neg = 0
somaPos =0
somaNeg = 0
for c in range(1, 11):
    num = float(input('\n Digite número qualquer: '))
    if num >= 0:
        pos +=1 
        somaPos += num
    else:
        neg += 1 
        somaNeg += num
print(f'\n Quantidade de números positivos digitados: {pos}')
print(f'A soma entre eles: {somaPos}\n')
print(f'Quantidade de números negativos digitados: {neg}')
print(f'A soma entre eles: {somaNeg}')