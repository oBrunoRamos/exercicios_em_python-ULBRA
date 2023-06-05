aluno = int(input("Digite o código do aluno: "))
nota1 = float(input("Digite a nota do aluno da prova com nota maxima de 4: "))
nota2 = float(input("Digite a nota do aluno da prova com nota maxima de 3: "))
nota3 = float(input("Digite a nota do aluno da outra prova com nota maxima de 3: "))

print(f"Código do aluno: {aluno}")
print(f"Nota 01: {nota1}")
print(f"Nota 02: {nota2}")
print(f"Nota 03: {nota3}")

if nota1 == 4:
    nota1 = 10
elif nota1 == 3:
    nota1 = 8.5
elif nota1 == 2:
    nota1 = 5
elif nota1 == 1:
    nota1 = 2.5
elif nota1 == 0:
    nota1 = 0
else:
    nota1 = '[ERRO] Valor inválido!'

if nota2 == 3:
    nota2 = 10
elif nota2 == 2:
    nota2 = 6.66
elif nota2 == 1:
    nota2 = 3.33
elif nota2 == 0:
    nota2 = 0
else:
    nota2 = '[ERRO] Valor inválido!'

if nota3 == 3:
    nota3 = 10
elif nota3 == 2:
    nota3 = 6.66
elif nota3 == 1:
    nota3 = 3.33
elif nota3== 0:
    nota3 = 0
else:
    nota3 = '[ERRO] Valor inválido!'

media = (nota1 + nota2 + nota3)/ 3

print(f"Média: {media}")
if media >= 7:
    print("Aluno [APROVADO]")
else:
    print("Aluno [REPROVADO]")