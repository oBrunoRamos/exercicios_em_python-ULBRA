not1 = float(input("Digite a primeira nota: "))
not2 = float(input("Digite a segunda nota: "))
not3 = float(input("Digite a terceira nota: "))

if not1 > 10 or not1 < 0:
    print ("[ERRO] nota inválida")
elif not2 > 10 or not2 < 0:
    print ("[ERRO] nota inválida")
elif not3 > 10 or not3 < 0:
    print ("[ERRO] nota inválida")
else:
    m = (not1 * 0.2) + (not2 * 0.3) + (not3 * 0.5)
    
    if m < 6: 
        print("Sinto muito, você reprovou.")
    elif m >= 6:
        print("Parabéns você foi aprovado.")
