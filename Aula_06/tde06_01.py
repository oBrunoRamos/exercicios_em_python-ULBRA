
tot_dia = int(input("Digite a quantidade de diárias serão necessárias: "))

if tot_dia < 15:
    print(f"O total vai ser a taxa de serviço diário de 50 reais mais a taxa diária de 1,50 dando o total de {tot_dia*1.5}, dando um total de {tot_dia*1.5 + tot_dia*50}")
elif tot_dia == 15:
    print(f"O total vai ser a taxa de serviço diário de 50 reais mais a taxa diária de 1,00 dando o total de {tot_dia*1.0}, dando um total de {tot_dia*1 + tot_dia*50}")
else:
    print(f"O total vai ser a taxa de serviço diário de 50 reais mais a taxa diária de 0,50 dando o total de {tot_dia*0.5}, dando um total de {tot_dia*0.5 + tot_dia*50}")
