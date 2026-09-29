import pandas as pd 

dicionario = {"nome": ["joão", "maria", "pedro", "alex", "juliana", "marcos"], 
              "idade": [12, 10, 11, 9, 13, 10], "nota": [7.0, 5.6, 9.0, 6.2, 5.7, 10]}


df = pd.DataFrame(dicionario)

df.to_csv("alunos.csv", index=False, sep=";")