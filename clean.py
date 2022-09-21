import csv
import pandas as pd

df = pd.read_csv("final_stars.csv")

print(df)
print(df.columns)

del df["Unnamed: 0"]
del df["Unnamed: 6"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Luminosity"]

final_data = df.dropna()
print(final_data)


print(list(df))

print(df)

df.to_csv('new.csv')