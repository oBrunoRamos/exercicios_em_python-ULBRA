'''
4- Faça um programa que leia o nome completo de um autor famoso e uma frase conhecida. Imprimir no final a mensagem no seguinte formato: "Descarte, René. Penso logo existo". Caso tenha mais que dois nomes considere apenas o primeiro e o último.

'''
def reverse(a):
    reverse = []
    name = a.split()
    reverse.append(name[1])
    reverse.append(name[0])
    reverse = ', '.join(reverse) 
    return reverse

autor = str(input('\nDigite o nome de um autor famoso: '))
frase = str(input('Digite agora sua frase: '))

while True:
    if autor == '' or frase == '':
        print('\nVocê não digitou o nome do autor ou a frase!')
        print('Digite novamente: ')
        autor = str(input('\nDigite o nome de um autor famoso: '))
        frase = str(input('Digite agora sua frase: '))
    else:
        break

if len(autor) > 2:
    autor = autor.split()
    for i in range(len(autor)-2, 0, -1):
        del autor[i]
    autor = ' '. join(autor)

print(f'{reverse(autor)} \n    {frase}')