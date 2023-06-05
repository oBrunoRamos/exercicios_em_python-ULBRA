'''
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
'''
for n in range(1,30):
    soma = 0
    for d in range(1, n + 1):
        if n % d == 0:
            soma += 1
    if soma == 2:
        print(n)