'''
2- Escreva um programa que solicite ao usuário que digite uma palavra e verifique se ela é um palíndromo. Um palíndromo é uma palavra que pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda. O programa deve exibir "É um palíndromo" ou "Não é um palíndromo".

'''

palavra = input('\nDigite uma palavra: ')
 
plvRev = []

for letra in reversed(palavra):
    plvRev.append(letra)
    
plvRev = ''.join(plvRev)

if palavra == plvRev:
    print('Essa palavra é um palíndromo')
else:
    print('Essa palavra não é um palíndromo')