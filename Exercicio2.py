notas = {
    "Ana": 8,
    "Pedro": 6,
    "Lucas": 10,
    "Julia": 9,
    "Marcos": 5
}
aprovados = []

for aluno, nota in notas.items():
    if nota >= 7:
        aprovados.append(aluno)

for e in aprovados:
    print(e, "está aprovado")
