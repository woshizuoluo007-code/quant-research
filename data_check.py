import pandas as pd

df = pd.read_csv("hs300.csv")

print(df.info())

print(df.describe())