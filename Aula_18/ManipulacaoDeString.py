frase = 'Hello World'

print(frase[0]) # retornará 'H'

print(frase.upper()) # Renorna a variavel em maiuculas

print(frase.lower()) # Retorna a frase em minusculas

print(len(frase)) # Retorna o tamanho da string

print(frase.strip()) # Retira os espaçoes entre as palavras

print(frase.split()) # Transforma a frase em uma array, todo espaço vazio ele quebrará, no caso da frase, se tornaria ['Hello', 'World']. Se colocarmos um valor dentro dos (), ele deividirá e irá excluir a letra. Ex.: frase.split('l')  = ['He', 'o Wor', 'd' ].

print(frase.replace('Hello', 'Olá')) # Subistitui a palavra 'Hello' onde encontrar na variavel frase, quantas vezes aparecer.

print(frase[0:2]) #So mostrará uma parte da array. No caso da primeira até a terceira string. 'Hel'

for letra in frase: 
    print(letra)

nums = [1, 2, 3]
texto = ' '.join(nums) # Diz como concatenar as palavras na decorre do codigo. Podemos alterar o concatenador antes do .join(). Ex.: 1.join() 'x'.join() 9.join() '              '.join()
print(texto) # No caso desse print, e le nao imprimirá 123, e sim 1 2 3. Se trocarmos a concatenação por 'x', o resultado final será 1x2x3

