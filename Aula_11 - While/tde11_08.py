c = 1
totPos = 0
somaPos = 0
totNeg = 0
somaNeg = 0
while c <= 10:
   num = float(input(f'Digite o {c} número, pode ser positivo ou negativo: '))
   if num >= 0:
      totPos += 1
      somaPos += num
   else:
      totNeg +=1
      somaNeg += num
   c+=1
print(f'O total de números nulos ou positivos é {totPos}')
print(f'A soma de todos os números positimos é {somaPos}')
print(f'O total de números negativos é {totNeg}')
print(f'A soma de todos os números negativos é {somaNeg}')