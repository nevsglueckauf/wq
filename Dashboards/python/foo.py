import pandas as pd

df = pd.read_csv("../../Data/Agg/brnd_per_day_sales_all.csv")
df["date"] = pd.to_datetime(df["date"])
print(df.describe())

nw = df.groupby("brand").resample('M', on='date').agg({'price': 'sum', 'price': 'mean'})
nw["price"] = round(nw["price"], 2)
# df_agg = df.groupby(["date, brand"])['price'].sum()
print(nw.tail(8))
nw.to_csv("../../Data/Agg/brnd_per_month_sales_all.csv")