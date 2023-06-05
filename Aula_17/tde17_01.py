
#Preencher uma lista de 10 elementos, ao fim da leitura o programa deve passar os números pares para um segundo vetor, e os ímpares para um terceiro vetor. Imprimir os dois novos vetores no final.

numeros = []
par = []
impar = []

for i in range(10):
    num = int(input('\nDigite um novo número: '))
    numeros.append(num)

numeros.sort()
print(numeros)

for n in numeros:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)

print(f'Numeros pares digitados: {par}')
print(f'Numeros inpares digitados {impar}')
