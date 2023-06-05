ptsEquip1 = 0
ptsEquip2 = 0
equip1 = str(input('\nDigite o nome da 1º equipe: '))
equip2 = str(input('\nDigite o nome da 2º equipe: '))
algoEquip1 = int(input(f'\nDigite quantos algoritimos a equipe {equip1} entregou: '))
algoEquip2 = int(input(f'\nDigite quantos algoritimos a equipe {equip2} entregou: '))
erros2= int(input(f'\nEquipe {equip1}, quantos erros foram achados nos códigos da equipe adiversária? '))
if erros2 > algoEquip2:
    print('\nDados digitados são incorretos [ERRO]!!!!\n')
else:
    erros1= int(input(f'\nEquipe {equip2}, quantos erros foram achados nos códigos da equipe adiversária? '))
    if erros1 > algoEquip1:
        print('\nDados digitados são incorretos [ERRO]!!!!\n')
    else:
        corr1 = int(input(f'\nEquipe {equip1}, quantos erros vocês corrigiram da equipe adversária? '))
        if corr1 > erros1:
            print('\nDados digitados são incorretos [ERRO]!!!!\n')
        else:
            corr2 = int(input(f'\nEquipe {equip2}, quantos erros vocês corrigiram da equipe adversária? '))
            if corr2 > erros2:
                print('\nDados digitados são incorretos [ERRO]!!!!\n')
            else:
                #pontuação de total de algoritimos
                for c in range(0,algoEquip1,1):
                    ptsEquip1 += 10
                for c in range(0,algoEquip2,1):
                    ptsEquip2 += 10
                #porntuação erros
                for c in range(0,erros1,1):
                    ptsEquip1 -= 5
                for c in range(0,erros2,1):
                    ptsEquip2 -= 5
                #pontução corressões
                for c in range(0, corr1, 1):
                    ptsEquip1 += 5
                for c in range(0, corr2, 1):
                    ptsEquip2 += 5
                #potuação atraso de entrega
                hora1 = int(input(f'\nDigite a hora de entrega da {equip1}: (SOMENTE A HORA, SEM OS MINUTOS, POR FAVOR!!!)'))
                if hora1 > 12:
                    print('Dados digitados são incorretos [ERRO]!!!!')
                else:
                    min1 = int(input(f'Agora digite os minutos: '))
                    if min1 > 59:
                        print('Dados digitados são incorretos [ERRO]!!!!')
                    else:
                        hora2 = int(input(f'\nDigite a hora de entrega da {equip2}: (SOMENTE A HORA, SEM OS MINUTOS, POR FAVOR!!!)'))
                        if hora2 > 12:
                            print('Dados digitados são incorretos [ERRO]!!!!')
                        else:
                            min2 = int(input(f'Agora digite os minutos: '))
                            if min2 > 60:
                                print('Dados digitados são incorretos [ERRO]!!!!')
                            else:
                                ptsPerdido1 = 0
                                if hora1 >= 9:
                                    ptsPerdido1 = min1 * 10
                                    ptsEquip1 -= ptsPerdido1
                                ptsPerdido2 = 0
                                if hora2 >= 9:
                                    ptsPerdido2 = min2 * 10
                                    ptsEquip2 -= ptsPerdido2
                                print(f'\nEquipe: {equip1} \n Algoritimos Resolvidos: {algoEquip1} Pontos: {algoEquip1*10} \n Erros Encontrados: {erros1}. Pontos: {erros1*(-5)} \n Erros Corrigidos: {corr1} Pontos: {corr1*5} \n Hora Entregue: 0{hora1}:{min1} Desconto:{ptsPerdido1} \n Pontuação total: {ptsEquip1} ')
                                print(f'\nEquipe: {equip2} \n Algoritimos Resolvidos: {algoEquip2} Pontos: {algoEquip2*10} \n Erros Encontrados: {erros2}. Pontos: {erros2*(-5)} \n Erros Corrigidos: {corr2} Pontos: {corr2*5} \n Hora Entregue: 0{hora2}:{min2} Desconto:{ptsPerdido2} \n Pontuação total: {ptsEquip2} ')
                                if ptsEquip1 > ptsEquip2:
                                    print(f'\nA equipe {equip1} ganhou!!!\n')
                                elif ptsEquip1 == ptsEquip2:
                                    print(f'\nHouve um empate entre {equip1} e {equip2}\n')
                                else:
                                    print(f'\nA equipe {equip2} ganhou!!!\n')