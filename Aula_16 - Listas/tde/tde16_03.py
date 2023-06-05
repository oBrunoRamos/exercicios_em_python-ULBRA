#Faça um programa que leia uma lista de 5 elementos e mostre-os na tela na ordem inversa que foi digitada.

numeros = []

for i in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)

numeros.reverse()
print(numeros)