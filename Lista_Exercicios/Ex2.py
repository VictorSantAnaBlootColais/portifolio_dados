def contador_vogais(frase):
    frase = frase.lower()
    contador = {}

    for letras in frase:
        if letras in "aeiou":
            if letras in contador:
                contador[letras] += 1
            else:
                contador[letras] = 1

    return contador

print(contador_vogais("abacaxi"))


