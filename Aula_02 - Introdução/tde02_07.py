peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

print("Seu IMC: " + str(imc))

if imc < 17 :
    print("Você está muito abaixo do peso.")
elif (imc >= 17) and (imc < 18.5):
    print("Você está abaixo do peso.")
elif (imc >= 18.5) and (imc < 25):
    print("Você está no seu peso ideal.")
elif (imc >= 25) and (imc < 30):
    print("Você está com sobre peso.")
elif (imc >= 30) and (imc < 35):
    print("Você está obeso.")
elif (imc >= 35) and (imc < 40):
    print("Você está com obesidade severa.")
elif (imc >= 40):
    print("Você tem obesidade morbida.")