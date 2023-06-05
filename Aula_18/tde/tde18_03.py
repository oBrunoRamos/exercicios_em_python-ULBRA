'''
3- Escreva um programa que solicite ao usuário que digite uma frase e, em seguida, substitua todas as ocorrências de uma determinada letra por outra letra especificada pelo usuário. Informe no final a frase modificada.

'''                                                                                

frase = str(input('\nDigite uma Frase: '))
subs = str(input('Agora digite uma letra para ser substituída: '))
colc = str(input('Essa letra vai ser subistituida por qual? '))


print(frase.replace(subs, colc))

