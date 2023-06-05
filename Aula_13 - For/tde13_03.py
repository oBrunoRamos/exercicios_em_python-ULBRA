notaTot = 0
for c in range(1, 11):
    nota = float(input(f'\nDigite a nota do {c}° aluno: '))
    notaTot += nota
print(f'Com essas notas, a média da turma foi: {notaTot/ 10}')