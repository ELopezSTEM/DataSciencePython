import pandas as pd

df = pd.read_csv(r"recursos\PEATONES_2020.csv", encoding="ISO-8859-1", delimiter=";", index_col=2, nrows=10000)

print(df)