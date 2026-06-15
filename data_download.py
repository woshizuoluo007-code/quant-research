import akshare as ak

df = ak.stock_zh_index_daily(symbol="sh000300")

print(df.head())

print(df.tail())

df.to_csv("hs300.csv", index=False)

print("保存成功")