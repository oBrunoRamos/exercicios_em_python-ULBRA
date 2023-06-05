aluno = 1
digNota = 0
aprov = 0
while aluno <= 10:
   nota = 1
   while nota <= 3:
      totNota = 0
      digNota = float(input(f'Digite a {nota}° do {aluno}° aluno: '))
      if digNota > 10:
         print('Valor de nota digitado incorreto. [ERRO]')
         print('Tente novamente....')  
         continue
      else:
         totNota += digNota
      nota += 1
   if totNota >= 7:
      aprov +=1 
   aluno+=1
print(f'No total {aprov * 10}% dos alunos da turma foram aprovados.')

