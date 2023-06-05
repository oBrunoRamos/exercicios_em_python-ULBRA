nome = input("Digite o nome do funcionário: ")
tempo = float(input("Digite o tempo de horas trabalhadas: "))
sal_hora = float(input("Digite o salário por hora do funcionáio: "))

salario = tempo * sal_hora

print("O funcionário " + nome + " trabalhando " + str(tempo) + "h por dia tendo um salário de " + str(sal_hora) + ", ela terá um salário total de " + str(salario) + " reais por mês.")