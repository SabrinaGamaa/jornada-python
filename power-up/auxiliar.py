import pandas as pd

dado = pd.read_csv('power-up/produtos.csv')

pri = dado.head(5)
print(pri.isna())

for linha in pri.itertuples():
    print(linha.codigo)
    if pd.isna(linha.obs) == False:
        print(linha.obs)
