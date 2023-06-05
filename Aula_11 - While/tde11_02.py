c = 100
totImpar = 0

while c <= 500:
   if c % 2 == 1:
      totImpar += c
   c+=1
   
print(f'A soma de todos os números entre 100 e 500 é {totImpar}')
   