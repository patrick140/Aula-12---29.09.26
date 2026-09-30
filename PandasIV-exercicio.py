#CRIE UM DATAFRAME COM OS DADOS DO ARQUIVO FUNCIONARIOS.CSV E FILTRE:
#TODOS OS FUNCIONARIOS ATIVOS NO DEPARTAMENTO DE VENDAS
#TODOS OS FUNCIONARIOS ATIVOS COM LUCRO MAIOR QUE 5000
#TODOS OS FUNCIONARIOS INATIVOS
#CADA FILTRO TERA QUE SER SALVO EM UMA VARIAVEL
#EXPORTAR CADA FILTRO PARA UM ARQUIVO CSV

import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Downloads\funcionarios.csv")

df_func_ativos_dep_vendas = df[(df["ativo"] == True) & (df["departamento"] == "Vendas")]

print(df_func_ativos_dep_vendas)

df_func_ativos_lucro_maior_5000 = df[(df["ativo"] == True) & (df["lucro"] > 5000)]

print(df_func_ativos_lucro_maior_5000)

df_func_inativos = df[df["ativo"] == False]

print(df_func_inativos)

df_func_ativos_dep_vendas.to_csv("df_func_ativos_dep_vendas.csv", index=False, sep=";")

df_func_ativos_lucro_maior_5000.to_csv("df_func_ativos_lucro_maior_5000.csv", index=False, sep=";")

df_func_inativos.to_csv("df_func_inativos.csv", index=False, sep=";")