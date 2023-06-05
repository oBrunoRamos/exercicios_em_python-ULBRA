numeros = [0,7,4,12,434,20]

#Alterando elementos

print(numeros)
numeros[0] = 21
print(numeros)
numeros[4] = 3
print(numeros)

#Alterando o ultimo
numeros[-1] = 1

#Inserindo elementos
numeros.append(100) #inserindo na ultima posição
print(numeros)

numeros.insert(3, 450) #inserindo por posição(inserindo o número 450 na posição 3)
print(numeros)

#Excluindo elementos
numeros.pop() #exclui o ultimo item da lista e mostra o valor removido, caso queira um indice específico tem que colocar entre ().
print(numeros)

numeros.remove(12) #remove o valor especificado. caso tenha mais de um valor igual, exclui o primeiro. caso não tenha dá erro no código.
print(numeros)

