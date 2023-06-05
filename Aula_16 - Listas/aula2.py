

planetas = ['terra', 'Jupiter', 'Marte', 'Vênus', 'Saturno', 'Netuno']

for p in planetas:
    print(p)
    if p == 'Vênus':
        print('Você descobriu um planeta')

#Preenchendo uma lista

nomes = []
for i in range(3):
    nome = input('Digite o nome: ')
    nomes.append(nome)

for n in nomes:
    if n == 'ana':
        print('você encontrou a ana')
print(nomes)