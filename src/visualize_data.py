import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/cleaned_food_prices.csv", parse_dates=["date"])

# Example: Rice price trend
rice = df[df["commodity"].str.contains("Rice", case=False)]

trend = rice.groupby("date")["price"].mean()

plt.figure(figsize=(10,5))
trend.plot()
plt.title("Rice Price Trend in Philippines")
plt.xlabel("Date")
plt.ylabel("Price")
plt.tight_layout()

plt.savefig("outputs/charts/rice_trend.png")
plt.show()