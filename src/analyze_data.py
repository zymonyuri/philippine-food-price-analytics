import pandas as pd

df = pd.read_csv("data/processed/cleaned_food_prices.csv", parse_dates=["date"])

print("Rows:", len(df))
print("Columns:", df.columns.tolist())

print("\nTop commodities:")
print(df["commodity"].value_counts().head())

print("\nAverage price per commodity:")
print(df.groupby("commodity")["price"].mean().sort_values(ascending=False).head())

print("\nDate range:")
print(df["date"].min(), "to", df["date"].max())