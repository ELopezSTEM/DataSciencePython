import pandas as pd

df = pd.read_csv(r"recursos\PEATONES_2020_mod.csv", encoding="ISO-8859-1", delimiter=";")

num_registros_originales = df.shape[0]

print("Número de registros originales:\n", num_registros_originales, "\n")

df.drop_duplicates(inplace=True)

num_registros_sin_duplicados = df.shape[0]

print("Número de registros sin duplicados:\n", num_registros_sin_duplicados, "\n")

df.dropna(inplace=True)

num_registros_sin_nulos = df.shape[0]

print("Número de registros sin nulos:\n", num_registros_sin_nulos, "\n")

print("Porcentaje de los datos erroneos:\n", (100 - (num_registros_sin_nulos * 100) / num_registros_originales), "%")

