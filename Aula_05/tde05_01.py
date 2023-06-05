peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

print("Seu IMC: " + str(imc))

if imc < 18.5:
    print("Você está muito abaixo do peso.")
elif (imc >= 18.5) and (imc <= 24.9):
    print("Você com peso normal.")
elif (imc >= 25) and (imc <= 29.9):
    print("Você está com sobre peso.")
elif (imc >= 30) and (imc <= 34.9):
    print("Você está com obesidade grau 1.")
elif (imc >= 35):
    print("Você está com obesidade grau 2.")