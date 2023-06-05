apr = 0
rep = 0
for a in range(1, 11):
    somaNota = 0
    n = 1
    while n <= 3:
        nota = float(input(f'\n Digite a {n}° nota do {a}° aluno: '))
        if nota > 10:
            print('NOTA DIGITADA INCORRRETA [ERRO]. Digite novamente....')
            continue
        else:
            somaNota += nota
            if somaNota / 3 >= 7:
                apr += 1
            else:
                rep += 1
        n += 1
print(f'Total de alunos APROVADOS: {apr}')
print(f'Total de alunos REPROVADOS: {rep}')
print(f'Percentagem de alunos APROVADOS: {apr*10}%')