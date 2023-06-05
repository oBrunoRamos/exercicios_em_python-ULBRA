'''
6- Faça um programa que leia uma frase e apresente o número de vogais presentes na frase. O número de vogais devem vir do retorno da função.
'''
def vogal(a):
    cont = 0
    for letra in a:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            cont = cont + 1

    if cont <= 0:
        return 'Sua frase não possuí vogais'
    else:
        return f'Sua frase possui {cont} vogais.'

frase = str(input('\nDigite uma frase: '))
print(vogal(frase))