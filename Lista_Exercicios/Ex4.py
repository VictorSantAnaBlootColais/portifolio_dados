def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    for i in lista:
        if i < menor:
            menor = i
    
    return maior, menor

print(maior_menor([7, 3, 4, 5, 6]))
