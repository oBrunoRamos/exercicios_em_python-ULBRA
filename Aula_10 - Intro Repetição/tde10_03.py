#. Faça um algoritmo que leia 10 valores inteiros e:
#• Encontre e mostre o maior valor 
#• Encontre e mostre o menor valor 
#• Calcule e mostre a média dos números lidos

n_maior = 0
n_menor = 100
c = 1
tot_n = 0
while c <= 10:
    c +=1
    n = float(input("Digite um número: "))
    
    tot_n +=n

    if n > n_maior:
        n_maior = n

    elif n < n_menor:
        n_menor = n
        

print(f"Maior número:{n_maior}. Menor número:{n_menor}.")
print(f"A média dos números é: {tot_n/10}")