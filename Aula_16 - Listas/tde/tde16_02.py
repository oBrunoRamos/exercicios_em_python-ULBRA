#Faça um programa que leia uma lista de número não determinado de nomes, ao ser digitado "fim" deve mostrar na tela todos os nomes lidos.

nomes = []
nome = ''
while nome != 'fim':
    nome = str(input('Digite um nome novo: '))
    nomes.append(nome)

nomes.remove('fim')
for n in nomes:
    print(n)