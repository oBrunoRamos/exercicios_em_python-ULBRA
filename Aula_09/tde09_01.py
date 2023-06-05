cig = int(input('Digite quatos cigarros você fuma diariamente: '))
mes = int(input('Digite a quantos meses você fuma: '))

print('Segundo estudos a cada cigaro fumado vove perde em média 15 minutos de vida.')
tot = cig * 15
tot_cig = tot * 30
tot_vida = tot_cig * mes
tot_mes = mes * 30

dias = tot_vida / 1440

print(f'{tot_mes}Segundo os dados inseridos você perdeu já {tot_vida} minutos de vida. Em dias é igual a {dias} dias.')

if tot_mes <= 90:
    print('As consequencias atuais são seus dentes amarelos')
elif tot_mes <= 365:
    print('Suas consequencias de fumar atualmente é a perda do paladar e a respiração comprometida.')
elif tot_mes > 365: 
    print('seu pulmão já está comprometido')