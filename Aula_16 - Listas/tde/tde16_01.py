
#Faça um programa que leia uma lista de 5 elementos inteiros e mostre-os na tela.

numeros = []

for i in range(5):
    num = int(input('\nDigite um novo número: '))
    numeros.append(num)
numeros.sort()
for n in numeros:
    print(n)