resp = ''
tot_v = 0
q_multas = 0 
s_multa = 0 
m_multa = 0
g_multa = 0 
gs_multa = 0
soma = 0
while resp != 'não':
    resp = str(input("Deseja continuar? Sim ou não.: "))
    if resp == 'sim':
        v_car = int(input("Digite a velocidade do carro(Km/h): "))
        tot_v += v_car
        q_multas +=1
        if v_car > 60 and v_car <= 67:
           print(f"Velocidade do carro: {v_car}Km/h. Dentro da margem de erro, multa não aplicada.")
           s_multa +=1
        elif v_car > 67 and v_car <= 60+(60*0.2):
            print(f"Velocidade do carro: {v_car}Km/h. Multa aplicada. R$130,16 - Multa média")
            m_multa +=1
            soma += 130.16
        elif v_car > 60+(60*0.2) and v_car <= 60+(60*0.5):
            print(f"Velocidade do carro: {v_car}Km/h. Multa aplicada. R$195,23 - Multa grave.")
            g_multa +=1
            soma += 195.23
        elif v_car > 60+(60*0.5):
            print(f"Velocidade do carro: {v_car}Km/h. Multa aplicada. R$195,23 - Multa grave.")
            g_multa +=1
            soma += 195.23
        else:
            print(f"Velocidade do carro: {v_car}Km/h. Dentro da velocidade permitida. Dirija com segurança.")
            s_multa +=1
        continue
    elif resp == "não" or resp == "nao":
        break
    else:
        print("Resposta inválida!!")
        continue

if q_multas >=1:
    print(f"Número de veículos contados: {q_multas}")
    print(f"Número de veículos sem multas: {s_multa}")
    print(f"Número de veículos com multa média: {m_multa}")
    print(f"Número de veículos com multa grave: {g_multa}")
    print(f"Número de veículos com multa gravíssima: {gs_multa}")
    print(f"A soma de todas as multas foi de R${soma}")
    print(f"A velocidade média na rodovia foi de {tot_v/q_multas}Km/h.")
else:
    print('Nenhum veiculo contado.')