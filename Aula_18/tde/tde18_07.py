'''
7- Faça um programa que leia dois números do usuário e exiba o seguinte menu de opções: 
            (1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir, 5 - Sair)
e apresente o resultado escolhido na tela. Crie uma função para cada operação, lembre-se que não se divide número por 0.
'''
def som(a, b):
    soma = a + b
    return f'\n\nA soma ente {a} e {b} é {soma}'
def sub(a, b):
    sub = a - b
    return f'\n\nA subtração ente {a} e {b} é {sub}'
def mult(a, b):
    mlt = a * b
    return f'\n\nA multiplicação ente {a} e {b} é {mlt}'
def div(a, b):
    div = a / b
    return f'\n\nA divisão ente {a} e {b} é {div}'

n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite um número: '))

while True:

    print(f'\n\nEscolha: (digite um número para continuar)\n\n[1] - Somar\n\n[2] - Subtrair\n\n[3] - Multiplicar\n\n[4] - Dividir\n\n[5] - Sair\n\n')
    resp = input('Digite oque deseja fazer: ')

    while True:
        try:
            resp = int(resp)
            break
        except ValueError:
            print('\n[ERRO] Ação inválida')
            resp = input('Digite oque deseja fazer: ') 

    if resp > 5 or resp < 1:
        print('\n[ERRO] Ação inválida')
        
    if resp == 1:
        print(som(n1, n2))
    elif resp == 2:
        print(sub(n1, n2))
    elif resp == 3:
        print(mult(n1, n2))
    elif resp == 4:
        print(div(n1, n2))
    elif resp == 5:
        break

print('Abcabou!')