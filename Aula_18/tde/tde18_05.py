'''
5- Faça um programa que leia uma lista de 5 elementos inteiros, ao fim o programa deve mostrar a média dos elementos lidos e a soma dos elementos lidos. Deve criar uma função soma e uma função média que receba a lista como argumento e retorne o valor.

'''
def media(a):
    media = a/5
    return media

def soma(a, b, c, d, e):
    soma = a+b+c+d+e
    return soma



n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
n5 = int(input('Digite um número: '))

print(f'A soma desses números é {soma(n1, n2, n3, n4,n5)}')
print(f'E a média é {media(soma(n1, n2, n3, n4,n5))}')