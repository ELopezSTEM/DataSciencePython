import pandas as pd

df = pd.read_csv(r"recursos\PEATONES_2020_mod.csv", encoding="ISO-8859-1", delimiter=";")

df2 = df[(df["FECHA"] >= "01/01/2020") & (df["FECHA"] <= "01/05/2020")]

print(df2)

df2 = df2[df2["DISTRITO"].str.contains("Centro")]

print(df2)

print(df2.count())

df_interp = df2.interpolate(method="linear", limit_direction="forward")

print(df_interp.count())