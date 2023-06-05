#Faça um programa que leia uma lista de 5 elementos inteiros e mostre a soma dos elementos lidos.

numeros = []

for i in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)

print(f'A soma desses números é: {sum(numeros)}')