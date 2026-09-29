import pandas as pd #importar pandas com apelido pd

#criar um dicionario (os dados)
dicionario = {"nome": ["joão", "maria", "pedro"], "idade": [12, 10, 11], "nota": [7.0, 5.6, 9.0]}

#importar o dicionario (dados) para um dataframe
df = pd.DataFrame(dicionario)

#mostrar o dataframe no terminal
print(df)