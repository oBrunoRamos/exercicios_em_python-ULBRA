print("DIGITE SOMENTE NÚMEROS!!!")

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0): 
    if mes % 2 == 1 and dia <= 31 and dia >= 1:
        print("Data válida.")
    elif mes % 2 == 0 and mes != 2 and dia <= 30 and dia >= 1:
        print("Data válida ")
    elif mes == 2 and dia <= 29 and dia >= 1:
        print("Data válida")
    else:
        print("Data inválida")   
else: 
    if mes % 2 == 1 and dia <= 31 and dia >= 1:
        print("Data válida.")
    elif mes % 2 == 0 and mes != 2 and dia <= 30 and dia >= 1:
        print("Data válida ")
    elif mes == 2 and dia <= 28 and dia >= 1:
        print("Data válida")
    else:
        print("Data inválida")





