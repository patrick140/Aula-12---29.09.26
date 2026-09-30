#CRIE UM DATAFRAME QUE TERA 3 COLUNAS e 3 linhas: NOME, CARGO E SALARIO
import pandas as pd

dicionario = {"NOME": ["joão", "regina", "pedro"], "CARGO": 
              ["analista de dados", "analista de dados", "analista de dados"], 
              "SALARIO": [1000000.00, 1000000.00, 1000000.00]}

df = pd.DataFrame(dicionario)

print(df["NOME"])

df.to_csv("pandas exercicio 1.csv", index=False, sep=";")

