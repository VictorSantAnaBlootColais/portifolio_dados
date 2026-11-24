import pandas as pd

tabela = pd.read_csv("Projeto_vendas/Dados/vendas.csv", sep=",")
print(tabela)

print(len(tabela))