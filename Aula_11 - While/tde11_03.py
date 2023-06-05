c = 1
totNota = 0
while c <= 10:
   totNota += float(input(f'Digite a nota do {c}° aluno: '))
   c += 1

media = totNota / 10

print(f'A média geral d turma foi {media}')