n1 = float(input("Digite 1° a nota do aluno: "))
n2 = float(input("Digite 2° a nota do aluno: "))
n3 = float(input("Digite 3° a nota do aluno: "))

ma = (n1 + n2 + n3)/3

if ma >= 9:
    print(f'Média: {ma}')
    print('Conceito: A. Aluno[APROVADO]')
elif ma >= 7.5 and ma < 9:
    print(f'Média: {ma}')
    print('Conceito: B. Aluno[APROVADO]')
elif ma >= 6 and ma < 7.5:
    print(f'Média: {ma}')
    print('Conceito: C. Aluno[APROVADO]')
elif ma >= 4 and ma < 6:
    print(f'Média: {ma}')
    print('Conceito: D. Aluno[REPROVADO]')
else:
    print(f'Média: {ma}')
    print('Conceito: E. Aluno[REPROVADO]')