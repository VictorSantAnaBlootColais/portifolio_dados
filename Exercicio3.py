def fatorial(a):
    total = 1
    for e in range(a, 1, -1):
        total = total * e

    return total


numero = int(input("Digite um número para fatorar: "))
fatorial(numero)
print(fatorial(numero))