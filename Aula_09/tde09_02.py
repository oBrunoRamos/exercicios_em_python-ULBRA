idade = int(input("Digite sua idade: "))
sex = str(input("Digite seu sexo:(fem/masc) "))
her_fam = int(input("Digite quantos parentes seus tem cardiopatia: "))
perc_g = float(input("Digite seu percentual de gordura (não ponha '%'): "))
tabag = int(input("Digite quantos cigarros você fuma por dia: "))
exerc = float(input("Digite quantos minutos de exercícios você faz por semana: "))
colest = int(input("Digite a sua taxa de colesterol: "))
pres_sis = int(input("Digite sua pressão arterial sistólica: "))
pres_dia = int(input("Digite sua pressão arterial diastólica: "))

#Idade
if idade >= 10 and idade <= 20:
    id_pts = 1
elif idade >= 21 and idade <= 30:
    id_pts = 2
elif idade >= 31 and idade <= 40:
    id_pts = 3
elif idade >= 41 and idade <= 50:
    id_pts = 4
elif idade >= 51 and idade <= 60:
    id_pts = 5
else:
    id_pts = 8

#Herança
if her_fam == 0:
    her_pts = 1
elif her_fam == 1:
    her_pts = 2
elif her_fam == 3:
    her_pts = 3
elif her_fam >= 4:
    her_pts = 7

#Precentual de gordura
if sex == 'fem':
    if perc_g == 12:
        perc_pts = 0
    elif perc_g >= 12 and perc_g < 16:
        perc_pts = 1
    elif perc_g >= 16 and perc_g < 20:
        perc_pts = 2
    elif perc_g >= 20 and perc_g < 22:
        perc_pts = 3
    elif perc_g >= 22 and perc_g < 30:
        perc_pts = 5
    else:
        perc_pts = 7
else:
    if perc_g == 16:
        perc_pts = 0
    elif perc_g >= 16 and perc_g < 20:
       perc_pts = 1
    elif perc_g >= 20 and perc_g < 25:
        perc_pts = 2
    elif perc_g >= 25 and perc_g < 33:
        perc_pts = 3
    elif perc_g >= 33 and perc_g < 40:
        perc_pts = 5
    else:
        perc_pts = 7

#Tabagismo
if tabag == 0:
    tab_pts = 0
elif tabag <= 10:
    tab_pts = 2
elif tabag <= 20:
    tab_pts = 4
elif tabag <= 30:
    tab_pts = 6
elif tabag <= 40:
    tab_pts = 10
else:
    tab_pts = 8

#Exercícios
if exerc >= 0:
    exe_pts = 8
elif exerc >= 31:
    exe_pts = 6
elif exerc >= 60:
    exe_pts = 3
elif exerc >= 80:
    exe_pts = 2
elif exerc >= 120:
    exe_pts = 1
elif exerc >= 240:
    exe_pts = 0


#Colesterol
if colest <= 180:
    col_pts = 1
elif colest <= 205:
    col_pts = 2
elif colest <= 230:
    col_pts = 3
elif colest <= 255:
    col_pts = 4
elif colest <= 280:
    col_pts = 5
else:
    col_pts = 7

#Pressão sitólica
if pres_sis <= 120:
    sis_pts = 1
elif pres_sis <= 139:
    sis_pts = 2
elif pres_sis <= 159:
    sis_pts = 3
elif pres_sis <= 179:
    sis_pts = 4
elif pres_sis <= 199:
    sis_pts = 6
else:
    sis_pts = 8

#Pressão diastólica
if pres_dia <= 70:
    dia_pts = 1
elif pres_dia <= 76:
    dia_pts = 2
elif pres_dia <= 82:
    dia_pts = 3
elif pres_dia <= 93:
    dia_pts = 4
elif pres_dia <= 105:
    dia_pts = 6
else:
    dia_pts = 8

print("SEUS PONTOS")
print(f"Idade: {idade} - {id_pts} pts")
print(f"Herança familiar: {her_fam} - {her_pts} pts")
print(f"Percentual de gordura: {perc_g} - {perc_pts} pts")
print(f"Tabagismo: {tabag} - {tab_pts} pts")
print(f"Exercícios semanais: {exerc} minutos - {exe_pts} pts")
print(f"Colesterol: {colest} - {col_pts} pts")
print(f"Pressão sitólica: {pres_sis} - {sis_pts} pts")
print(f"Pressão diastólica: {pres_dia} - {dia_pts} pts")

tot_pts = id_pts+her_pts+col_pts+dia_pts+exe_pts+sis_pts+tab_pts+perc_pts

print(f"Seu total de pontos foi: {tot_pts} pts")
print("Confira seus potos na tabela")

print("De 05 a 11 pontos - Risco bem baixo da média")
print("De 12 a 17 pontos - Risco abaixo da média")
print("De 18 a 24 pontos - Risco médio habitual")
print("De 25 a 31 pontos - Risco moderado")
print("De 32 a 40 pontos - Risco perigoso")
print("De 41 a 63 pontos - Perigo urgrnte - Procure deu médico")