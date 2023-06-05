
#Faça um programa que leia uma lista de 10 elementos inteiros ou até os usuários digitar 99, ao fim o programa deve mostrar a média dos elementos lidos, a soma dos elementos lidos, e quantos foram os elementos lidos.

numeros = []
for i in range(10):
    num = int(input('Digite um número novo: '))
    if(num == 99):
        break
    
    numeros.append(num)
media = sum(numeros) / len(numeros)

print(f'A média de elemntos lidos é de {media}')
print(f'A soma dos elementos lidos é de {sum(numeros)}')
print(f'A quântidade de números lidos é de {len(numeros)}')