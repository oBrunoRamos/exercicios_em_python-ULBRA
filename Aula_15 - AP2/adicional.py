soma = 0
for n in range(2,30):
    primo = 0
    for d in range(2, n):
        if n % d == 0:
            primo += 1
    if primo == 0:
        soma += n
print(f'{soma} - soma de todos os números primos entre 2 e 30')


maiorPrim = 0
for n in range(100,150):
    primo = 0
    for d in range(2, n):
        if n % d == 0:
            primo += 1
    if primo == 0:
        if n >= maiorPrim:
            maiorPrim = n
print(f'{maiorPrim} - Maior número primo entre 100 e 150')

menorPrim = 230
for n in range(200,230):
    primo = 0
    for d in range(2, n):
        if n % d == 0:
            primo += 1
    if primo == 0:
        if n <= menorPrim:
            menorPrim = n
print(f'{menorPrim} - Menor numero primo entre 200 e 230')

print(f'{menorPrim * maiorPrim} - multiplicação do menor numero primo entre 200 e 230, com o maior numero primo entre 100 e 150')