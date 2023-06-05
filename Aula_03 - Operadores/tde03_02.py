produto = input("Digite o produto: ")
venda = float(input("Digite o valor que você vai vender esse produto: "))
custo = float(input("Digite seu valor de custo sobre esse produto: "))

lucro = float(venda - custo)

print('Voce terá um lucro total de R$' + str(lucro) + ' sobre o produto "', produto ,'".')