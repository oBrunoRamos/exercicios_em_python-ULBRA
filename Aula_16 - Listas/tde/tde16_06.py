# Preencher uma lista de 8 elementos inteiros. Mostrar a lista e informar quantos números são maiores que 30, e apresentar a somar apenas destes números;

numeros = []
for i in range(8):
    num = int(input('\nDigite um número novo: '))
    numeros.append(num)
numeros.sort()
copia = numeros.copy()
for i in copia:
    if i < 30:
        numeros.remove(i)

print(f'Números digitados: {copia}')
print(f'Números digitados maiores que 30: {numeros}')
print(f'Soma dos números maiores qu 30: {sum(numeros)}')