horas = float(input("Digite quantas horas você dorme por noite? "))
tempo = float(input("Digite a quantos dias você está dormindo assim: "))

print("Segundo estudo, a cada hora de sono perdida você perde 1 hora e 30 min de vida. Para uma vida mais sáudavel você precisa dormir cerca de 8 horas de sono.")

if horas < 8: 
    tperdido = ((8 - horas) * 1.5) * tempo
    print(f"Segundo os dados que você deu, dormindo por {horas} durante {tempo} dias, você perdeu {tperdido} horas de vida.")

if tempo >=90:
    if horas < 4 and tempo >= 90:
        print('Segundo estudos com esse tempo de sono, você corre risco de problemas cardíacos e aumento de riscos de acidentes.')
    elif horas < 6 and tempo >= 180:
        print("Segundo estudos com esse tempo de sono, você tem uma diminuição na capacidade de concentação e de memória.")
    elif horas < 8 and tempo >= 365: 
        print("Segundo estudos com esse tempo de sono, você tem menor risco de problemas de saúde e maior disposiçaõ física e mental.")
    elif horas < 8 and tempo >= 365: 
        print("Segundo estudos com esse tempo de sono, voce tem um aumento do risco de doenças crônicas, como obesidade e diabetes.")
    else:
        print("Você precisa melhorar a qualidade de seu sono, procure dormir entre 6 e 8 horas por dia.")

else:
    print("Você está nessa rotina a menos de 90 dias, tente sempre manter seu nono entre 6 e 8 horas.")
