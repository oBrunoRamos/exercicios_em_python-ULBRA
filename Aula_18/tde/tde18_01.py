'''
1- Escreva um programa que solicite ao usuário que digite um texto e conte o número de caracteres no texto e exiba o resultado na tela. Os espaços em branco não devem ser contados.
'''


frase = str(input('\nDigite uma frase: '))
cont = 0
for letra in frase:
    if letra == ' ':
        continue
    else:
        cont+=1

print(f'\nNo total {cont} letras foram digitadas.')