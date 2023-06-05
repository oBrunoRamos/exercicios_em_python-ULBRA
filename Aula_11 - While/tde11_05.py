c = 1
nul = 0
pos = 0
neg = 0
while c <= 10:
   num = float(input('Digite um número qualque, segativo ou positivo: '))
   if num == 0:
      nul += 1
   elif num < 0:
      neg += 1
   elif num > 0:
      pos += 1
   c+=1
print(f'Total de números positivos: {pos}')
print(f'Total de números nulos: {nul}')
print(f'Total de números negativos: {neg}')