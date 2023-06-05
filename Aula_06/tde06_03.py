grp1 = 'indústrias do grupo 1'
grp2 = 'indústrias do grupo 2'
grp3 = 'indústrias do grupo 3'
ind_pol = float(input('Digite o índice de poluição atual: '))

if ind_pol >= 0.05 and ind_pol <= 0.25:
    print("Indíce de poluição aceitável.")
elif ind_pol > 0.26 and ind_pol <= 0.30:
    print(f"Indíce de poluição acima do aceitável as {grp1} serão intimadas a suspender as atividades.")
elif ind_pol > 0.31 and ind_pol <= 0.4:
    print(f"Indíce de poluição acima do aceitável as {grp1} e {grp2} serão intimadas a suspender as atividades.")
elif ind_pol > 0.4: 
    print("Todas as empresas devem parar suas atividades de imediato!!")
