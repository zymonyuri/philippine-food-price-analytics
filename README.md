# Philippine Food Price Analytics

An interactive Python data analytics project for exploring food price patterns in the Philippines across commodities, regions, markets, and time.

## Project Overview

This project uses a cleaned food price dataset to support:

- exploratory data analysis in Jupyter notebooks
- interactive dashboard analysis in Streamlit
- regional and commodity-level price comparisons
- trend, volatility, and distribution analysis

The dashboard is designed to help answer questions such as:

- Which commodities have the highest average prices?
- Which regions tend to have higher food prices?
- How do prices change over time?
- Which commodities are the most volatile?

## Dataset

The project uses the cleaned dataset at:

```text
data/processed/cleaned_food_prices.csv
```

Key fields used in the analysis include:

- `date`
- `admin1`
- `market`
- `commodity`
- `price`

## Features

### Notebook Analysis

The notebook workflow supports:

- top 10 most expensive commodities
- top 10 regions by average price
- average food price over time
- rice price trend analysis
- top 10 most volatile commodities

### Streamlit Dashboard

The dashboard includes:

- sidebar filters for commodity, region, market, and date range
- summary metrics for rows, commodities, markets, and regions
- trend charts for daily and monthly average price
- comparison charts for commodities and regions
- volatility and price distribution analysis
- filtered data preview table
- CSV download of filtered records

## Tech Stack

- Python
- pandas
- matplotlib
- Streamlit

## Installation

Create and activate your virtual environment, then install the required packages:

```bash
pip install pandas matplotlib streamlit
```

## Run the Dashboard

From the project root, run:

```bash
streamlit run app.py
```



## How to Use

1. Open the Streamlit dashboard.
2. Use the sidebar filters to narrow the dataset.
3. Review the overview metrics and insights.
4. Explore trends, comparisons, volatility, and distribution charts.
5. Inspect or download the filtered data.

## Analysis Areas

- price trends over time
- commodity-level price differences
- regional price differences
- market-level filtering
- price variability and volatility

## Future Improvements

- add more commodity-specific drilldowns
- include inflation-adjusted comparisons
- add map-based regional exploration
- expand notebook analysis with additional business questions

## Author

This project was built as a data analytics project focused on practical dashboarding, visual analysis, and storytelling with food price data.
