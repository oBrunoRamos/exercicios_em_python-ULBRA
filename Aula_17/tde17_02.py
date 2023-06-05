
#Faça um programa para criar uma lista de compras de mercadorias. Ela deve possuir um "menu" com as opções de adicionar, alterar, remover, listar e sair.

'''
    Não consegui utilizar o type() do jeito que queria, 
    digitei error no VScode e ele me deu a opção de ValueError, 
    pesquisei e consegui fazer uma função que respondia ao que eu queria.
'''

compras = []
resp = 0
while True:
    print(f'\nFeirinha do seu Zé:\n\nMenu: (digite um número para continuar)\n\n[1] - Adicionar\n\n[2] - Alterar\n\n[3] - Remover\n\n[4] - Listar\n\n[5] - Sair\n\n')
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
        resp = int(input('Digite oque deseja fazer: '))
    
    if resp == 1:
        element = str(input('\nDigite o nome do produto: '))
        compras.append(element)
    elif resp == 2:
        if len(compras) == 0:
            print('\nVocê não possuí nada para alterar.')
        else:
            item = int(input('Digite o número do item que deseja alterar:(a partir de 0) '))
            rItem = str(input(f'Você deseja alterar: {compras[item]} ?(s/n)'))
            if rItem == 's':
                compras.pop(item)
                nItem = str(input('Digite o produto que deseja adicionar: '))
                compras.insert(item, nItem)

    elif resp == 3:
        if len(compras) == 0:
            print('\nVocê não possuí nada para remover.')
        else:
            item = int(input('Digite o número do item que deseja remover: (a partir de 0)'))
            rItem = str(input(f'Você deseja remover: {compras[item]} ? (digite "s" para continuar, se não deseja remover digite qualquer coisa.)  '))
            if rItem == 's' or rItem == 'S':
                compras.pop(item)

    elif resp == 4:
        if len(compras) == 0:
            print('\nVocê não possuí nada na sua lista de compras.')
        else:
            print(f'Sua lista de compras: {compras}')
    elif resp == 5:
        break

print('\nObrigado por comprar conosco\n')