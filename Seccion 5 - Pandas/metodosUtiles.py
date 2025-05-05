import pandas as pd

df = pd.read_csv(r"recursos\PEATONES_2020_mod.csv", encoding="ISO-8859-1", delimiter=";")

print("Valores erroneos de la columna ""PEATONES"":\n", df.count())
print()

print("Media de la variable ""PEATONES"":\n", df["PEATONES"].mean())
print()

print("El rango de las fechas es desde: ", df["FECHA"].min(), " hasta ", df["FECHA"].max())
print()

df["PEATONES_AXUM"] = df["PEATONES"].cumsum()
