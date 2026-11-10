import string

def eh_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    string.punctuation
    for letra in texto:
        if letra in string.punctuation:
            texto = texto.replace(letra, "")

    inverso = texto[::-1]


    return inverso == texto



print(eh_palindromo("Ame, a ema"))
print(eh_palindromo("Anotaram a data da maratona"))
print(eh_palindromo("Python"))