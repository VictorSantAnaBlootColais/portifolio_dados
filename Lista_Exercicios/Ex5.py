
def sao_anagramas(palavra1, palavra2):
  # Remove espaços e converte para minúsculas
  p1 = palavra1.replace(" ", "").lower()
  p2 = palavra2.replace(" ", "").lower()

  return sorted(p1) == sorted(p2)

print(sao_anagramas("roma", "amor"))