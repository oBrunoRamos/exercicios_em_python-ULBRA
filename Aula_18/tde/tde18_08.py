'''
8 - Faça um programa que leia 5 números inteiros e passe lista de números como argumento e retorne uma string contendo os números ordenados em ordem crescente, separados por vírgula.
'''
nums = []
num =  []
for i in range(5):
    nums.append(int(input('\nDigite um número: ')))
nums.sort()
for n in nums:
    num.append(str(n))
num = ', '.join(num)
print(num)