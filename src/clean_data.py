import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/wfp_food_prices_phl.csv")
OUTPUT_PATH = Path("data/processed/cleaned_food_prices.csv")

def main():
    df = pd.read_csv(RAW_PATH)

    # Remove weird first row if needed
    if str(df.iloc[0]["date"]).startswith("#"):
        df = df.iloc[1:].copy()

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Convert types
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Drop missing important values
    df = df.dropna(subset=["date", "commodity", "market", "price"])

    # Sort
    df = df.sort_values("date")

    # Save
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("Cleaned data saved:", OUTPUT_PATH)

if __name__ == "__main__":
    main()