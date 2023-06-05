
salGrup = 0

masc = 0
salMasc = 0

fem = 0
salFem = 0

femSalInf1200 = 0

maiorSalSex = ''
maiorSal = 0
maiorSalID = 0

for c in range(1, 100**100):
    
    idade = input(f'\nDigite a idade da {c}° pessoa: ')
    while (idade == '') or (int(idade) > 120):
        print('\n[ERRO] POR FAVOR DIGITE UMA IDADE VÁLIDA')
        idade = input(f'Digite a idade da {c}° pessoa: ')

    if int(idade) < 0:
        break

    sexo = input(f'\nDigite o sexo da {c}° pessoa:(M/F) ')
    while (sexo == ''):
        if (str(sexo) == 'm' or str(sexo) == 'M') or (str(sexo) == 'F' or str(sexo) == 'f'):
            break
        print('\n[ERRO] POR FAVOR DIGITE UM SEXO VÁLIDO')
        sexo = input(f'\nDigite o sexo da {c}° pessoa:(M/F) ')

    sal = input(f'\nDigite o salário da {c}° pessoa: ')
    while (sal == ''):
        print('\n[ERRO] POR FAVOR DIGITE UM SALÁRIO VÁLIDO')
        sal = input(f'\nDigite o salário da {c}° pessoa: ')

    idade = int(idade)
    sexo = str(sexo)
    sal = float(sal)


    salGrup += sal

    if (sexo == 'm' or sexo == 'M'):
        masc += 1
        salMasc += sal
    elif (sexo == 'f' or sexo == 'F'):
        fem += 1
        salFem += sal

    if (sexo == 'f' or sexo == 'F'):
        femSalInf1200 += 1

    if sal > maiorSal:
        maiorSal = sal
        maiorSalID = idade
        if (sexo == 'm' or sexo == 'M'):
            maiorSalSex = 'Masculino'
        else:
            maiorSalSex = 'Feminino'

print(f'\nA média dos salários do grupo é R${salGrup/c}')
print(f'\nA média salarial dos homens é R${salMasc/masc}')
print(f'\nA média salarial das mulheres é R${salFem/fem}')
print(f'\nA quantidade de mulheres com salário até R$ 1200,00 é de {femSalInf1200} mulheres')
print(f'\nA  pessoa que possui o maior salário tem o sexo {maiorSalSex} e tem {maiorSalID} anos.')
