tot_id = 0

tot_alt = 0
tot_pessoas = 0

pess_peso = 0

c1 = 0
while c1 <= 25:
    c1 +=1
    print(f"DIGITE OS DADOS: {c1}")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    if idade > 50:
        tot_id +=1

    if idade <=20  and  idade >=10:
        tot_alt +=altura
        tot_pessoas +=1

    if peso < 40:
        pess_peso +=1
    
    


print(f"Pessoas com mais de 50: {tot_id}")
print(f"Média das alturas de pessoas entre 10 e 20 anos: {tot_alt/tot_pessoas}")
print(f"Percentagem de pessoas inferior a 40Kg: {(25*100)/pess_peso}")