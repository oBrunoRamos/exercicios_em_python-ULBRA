comput = float(input("Digite o valor de fábrica do computador: "))
impost = float((comput * 30) / 100)
revend = float((comput * 10) / 100)

tot_valor = comput + impost + revend

print("Você vai pagar um total de R$" + str(tot_valor) + " já incluso os impostos (R$" + str(impost) + ") e o lucro de venda da fábrica(R$" + str(revend) + ")")