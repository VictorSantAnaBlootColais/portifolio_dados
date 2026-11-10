frase = "Eu amo sabrina carpenter , ela é uma diva, sabrina Carpenter é tudo para mim"
frase = frase.lower()
palavras = frase.split()
contador = {}
maior = 0
mais_aparece = ""

for i in palavras:
    if i in contador:
        contador[i] += 1
    else:
        contador[i] = 1

for palavra, quantidade in contador.items():
    if quantidade > maior:
        maior = quantidade
        mais_aparece = palavra

print(maior)
print(mais_aparece)


