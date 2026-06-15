import pandas as pd

df = pd.read_csv("hs300.csv")

print(df.tail())

print("\n")

df2025 = df[df["date"] >= "2025-01-01"]

print(df2025.head())

print("\n")

print("2025 first close:", df2025.iloc[0]["close"])

print("latest close:", df2025.iloc[-1]["close"])