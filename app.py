

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


DATA_PATH = "data/processed/cleaned_food_prices.csv"

PRIMARY_COLOR = "#1F6F5F"
SECONDARY_COLOR = "#2FA084"
ACCENT_COLOR = "#6FCF97"
BACKGROUND_COLOR = "#EEEEEE"
CARD_COLOR = "#FFFFFF"
TEXT_COLOR = "#2E2E2E"
MUTED_TEXT_COLOR = "#5E6663"
BORDER_COLOR = "#D8DFDC"
GRID_COLOR = "#D6E4DF"

CHART_FIGSIZE_WIDE = (10, 4.8)
CHART_FIGSIZE_TALL = (10, 5.2)


st.set_page_config(
    page_title="Philippine Food Price Analytics",
    layout="wide",
)


st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
        }}

        [data-testid="stHeader"] {{
            background: rgba(238, 238, 238, 0.94);
        }}

        [data-testid="stSidebar"] {{
            background-color: #F7F7F7;
            border-right: 1px solid {BORDER_COLOR};
        }}

        [data-baseweb="tag"] {{
            background-color: {PRIMARY_COLOR} !important;
            border-color: {PRIMARY_COLOR} !important;
        }}

        [data-baseweb="tag"] span {{
            color: #FFFFFF !important;
        }}

        [data-baseweb="select"] > div {{
            border-color: {BORDER_COLOR} !important;
            box-shadow: none !important;
        }}

        [data-baseweb="select"] > div:focus-within {{
            border-color: {SECONDARY_COLOR} !important;
            box-shadow: 0 0 0 1px {SECONDARY_COLOR} !important;
        }}

        .stMultiSelect [data-baseweb="select"] > div:hover,
        .stDateInput input:hover,
        .stDateInput div[data-baseweb="input"]:hover {{
            border-color: {SECONDARY_COLOR} !important;
        }}

        .stToggle > label > div[data-testid="stWidgetLabel"] {{
            color: {TEXT_COLOR} !important;
        }}

        .stToggle [data-baseweb="switch"] {{
            background-color: {SECONDARY_COLOR} !important;
        }}

        .stToggle [data-baseweb="switch"] > div {{
            background-color: {SECONDARY_COLOR} !important;
            border-color: {SECONDARY_COLOR} !important;
        }}

        .stToggle [data-baseweb="switch"] input:not(:checked) + div {{
            background-color: #BFC9C5 !important;
        }}

        .stToggle input:checked + div,
        .stToggle input:checked + div > div,
        .stToggle [role="switch"][aria-checked="true"],
        .stToggle [role="switch"][aria-checked="true"] > div {{
            background-color: {SECONDARY_COLOR} !important;
            border-color: {SECONDARY_COLOR} !important;
        }}

        .block-container {{
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }}

        .title-wrap {{
            padding: 0.3rem 0 0.8rem 0;
        }}

        .title-kicker {{
            color: #1F6F5F !important;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.55rem;
            opacity: 1 !important;
        }}


        .title-main {{
            color: {PRIMARY_COLOR};
            font-size: 2.8rem;
            font-weight: 800;
            line-height: 1.05;
            margin-bottom: 0.7rem;
        }}

        .title-sub {{
            color: {MUTED_TEXT_COLOR};
            font-size: 1rem;
            line-height: 1.7;
            max-width: 900px;
            margin-bottom: 0.9rem;
        }}

        .meta-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
        }}

        .meta-pill {{
            background: {CARD_COLOR};
            border: 1px solid {BORDER_COLOR};
            border-radius: 999px;
            padding: 0.42rem 0.78rem;
            color: {TEXT_COLOR};
            font-size: 0.9rem;
        }}

        .section-title {{
            color: {PRIMARY_COLOR};
            font-size: 1.26rem;
            font-weight: 700;
            margin-bottom: 0.18rem;
        }}

        .section-text {{
            color: {MUTED_TEXT_COLOR};
            font-size: 0.96rem;
            margin-bottom: 0.9rem;
        }}

        .metric-card {{
            background: {CARD_COLOR};
            border: 1px solid {BORDER_COLOR};
            border-top: 4px solid {PRIMARY_COLOR};
            border-radius: 18px;
            padding: 1rem 1rem 0.95rem 1rem;
            box-shadow: 0 4px 14px rgba(31, 111, 95, 0.06);
            min-height: 118px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}

        .metric-label {{
            color: {MUTED_TEXT_COLOR};
            font-size: 0.88rem;
            font-weight: 600;
            margin-bottom: 0.35rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .metric-value {{
            color: {PRIMARY_COLOR};
            font-size: 1.9rem;
            font-weight: 800;
            line-height: 1.1;
        }}

        .chart-block {{
            margin-bottom: 0.8rem;
        }}

        .chart-title {{
            color: {PRIMARY_COLOR};
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }}

        .chart-text {{
            color: {MUTED_TEXT_COLOR};
            font-size: 0.9rem;
            margin-bottom: 0.45rem;
        }}

        .insight-card {{
            background: {CARD_COLOR};
            border: 1px solid {BORDER_COLOR};
            border-left: 4px solid {SECONDARY_COLOR};
            border-radius: 18px;
            padding: 1rem 1rem 0.95rem 1rem;
            box-shadow: 0 4px 14px rgba(31, 111, 95, 0.05);
            min-height: 148px;
        }}

        .insight-title {{
            color: {PRIMARY_COLOR};
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 0.45rem;
        }}

        .insight-text {{
            color: {MUTED_TEXT_COLOR};
            font-size: 0.95rem;
            line-height: 1.65;
        }}

        .table-card {{
            background: {CARD_COLOR};
            border: 1px solid {BORDER_COLOR};
            border-radius: 18px;
            padding: 0.95rem;
            box-shadow: 0 4px 14px rgba(31, 111, 95, 0.05);
        }}

        .sidebar-section {{
            margin-top: 0.3rem;
            margin-bottom: 0.25rem;
            color: {PRIMARY_COLOR};
            font-size: 0.92rem;
            font-weight: 700;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


plt.style.use("default")


def style_axis(ax):
    ax.set_facecolor(BACKGROUND_COLOR)
    ax.grid(True, linestyle="--", linewidth=0.8, alpha=0.8, color=GRID_COLOR)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(BORDER_COLOR)
    ax.spines["bottom"].set_color(BORDER_COLOR)
    ax.tick_params(colors=TEXT_COLOR, labelsize=9.5)
    ax.xaxis.label.set_color(TEXT_COLOR)
    ax.yaxis.label.set_color(TEXT_COLOR)


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "price"]).copy()
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    return df


@st.cache_data
def convert_df_to_csv(dataframe):
    return dataframe.to_csv(index=False).encode("utf-8")


def render_metric_card(label, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_insight_card(title, text):
    st.markdown(
        f"""
        <div class="insight-card">
            <div class="insight-title">{title}</div>
            <div class="insight-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def format_php(value):
    return f"{value:,.2f} PHP"


df = load_data()

if "filter_reset_counter" not in st.session_state:
    st.session_state.filter_reset_counter = 0


commodity_options = sorted(df["commodity"].dropna().unique())
region_options = sorted(df["admin1"].dropna().unique())
market_options = sorted(df["market"].dropna().unique())

min_date = df["date"].min().date()
max_date = df["date"].max().date()


st.markdown(
    f"""
    <div class="title-wrap">
        <div class="title-kicker">Analytics Dashboard</div>
        <div class="title-main">Philippine Food Price Analytics</div>
        <div class="title-sub">
            This dashboard provides an interactive view of food price patterns across commodities, regions, markets, and time, helping highlight price levels, geographic differences, and overall variability in the dataset.
        </div>
       
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")


st.sidebar.title("Filters")
st.sidebar.caption("Refine the dashboard view with targeted selections.")

if st.sidebar.button("Clear Filters", use_container_width=True):
    st.session_state.filter_reset_counter += 1

filter_key_suffix = str(st.session_state.filter_reset_counter)

st.sidebar.markdown('<div class="sidebar-section">Commodity</div>', unsafe_allow_html=True)
selected_commodities = st.sidebar.multiselect(
    "Commodity",
    options=commodity_options,
    default=[],
    placeholder="Select one or more commodities",
    key=f"commodity_filter_{filter_key_suffix}",
    help="Filter the dashboard to one or more commodities.",
    label_visibility="collapsed",
)

st.sidebar.markdown('<div class="sidebar-section">Region</div>', unsafe_allow_html=True)
selected_regions = st.sidebar.multiselect(
    "Region",
    options=region_options,
    default=[],
    placeholder="Select one or more regions",
    key=f"region_filter_{filter_key_suffix}",
    help="Filter by region using the admin1 field.",
    label_visibility="collapsed",
)

st.sidebar.markdown('<div class="sidebar-section">Market</div>', unsafe_allow_html=True)
selected_markets = st.sidebar.multiselect(
    "Market",
    options=market_options,
    default=[],
    placeholder="Select one or more markets",
    key=f"market_filter_{filter_key_suffix}",
    help="Filter the data to specific markets.",
    label_visibility="collapsed",
)

st.sidebar.markdown('<div class="sidebar-section">Date Range</div>', unsafe_allow_html=True)
selected_date_range = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
    key=f"date_filter_{filter_key_suffix}",
    label_visibility="collapsed",
)

if len(selected_date_range) != 2:
    st.warning("Please select a valid start and end date.")
    st.stop()

start_date, end_date = selected_date_range

filtered_df = df.copy()

if selected_commodities:
    filtered_df = filtered_df[filtered_df["commodity"].isin(selected_commodities)]

if selected_regions:
    filtered_df = filtered_df[filtered_df["admin1"].isin(selected_regions)]

if selected_markets:
    filtered_df = filtered_df[filtered_df["market"].isin(selected_markets)]

filtered_df = filtered_df[
    (filtered_df["date"] >= pd.to_datetime(start_date))
    & (filtered_df["date"] <= pd.to_datetime(end_date))
]

if filtered_df.empty:
    st.warning("No data matches the selected filters.")
    st.stop()


show_raw_data = st.toggle("Show Data Table", value=True)


st.markdown('<div class="section-title">Overview</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-text">A concise summary of the filtered dataset currently displayed on the dashboard.</div>',
    unsafe_allow_html=True,
)

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    render_metric_card("Total Rows", f"{len(filtered_df):,}")

with metric_col2:
    render_metric_card("Commodities", filtered_df["commodity"].nunique())

with metric_col3:
    render_metric_card("Markets", filtered_df["market"].nunique())

with metric_col4:
    render_metric_card("Regions", filtered_df["admin1"].nunique())


if len(selected_commodities) == 1:
    selected_commodity_name = selected_commodities[0]
    commodity_detail_df = filtered_df[filtered_df["commodity"] == selected_commodity_name].copy()
    commodity_avg_price = commodity_detail_df["price"].mean()
    commodity_market_count = commodity_detail_df["market"].nunique()
    commodity_region_count = commodity_detail_df["admin1"].nunique()

    st.markdown("---")
    st.markdown('<div class="section-title">Commodity Detail</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="section-text">Focused view for <strong>{selected_commodity_name}</strong> across the selected date range.</div>',
        unsafe_allow_html=True,
    )

    detail_col1, detail_col2, detail_col3 = st.columns(3)
    with detail_col1:
        render_metric_card("Average Price", f"{commodity_avg_price:,.2f} PHP")
    with detail_col2:
        render_metric_card("Markets Covered", commodity_market_count)
    with detail_col3:
        render_metric_card("Regions Covered", commodity_region_count)


st.divider()

top_commodity_row = (
    filtered_df.groupby("commodity", as_index=False)["price"]
    .mean()
    .sort_values("price", ascending=False)
    .head(1)
)
top_region_row = (
    filtered_df.groupby("admin1", as_index=False)["price"]
    .mean()
    .sort_values("price", ascending=False)
    .head(1)
)
overall_avg_price = filtered_df["price"].mean()
overall_price_std = filtered_df["price"].std()
top_market_row = (
    filtered_df.groupby("market", as_index=False)["price"]
    .mean()
    .sort_values("price", ascending=False)
    .head(1)
)

st.markdown('<div class="section-title">Insights</div>', unsafe_allow_html=True)

insight_col1, insight_col2, insight_col3 = st.columns(3)

with insight_col1:
    if not top_commodity_row.empty:
        render_insight_card(
            "Commodity Insight",
            f"{top_commodity_row.iloc[0]['commodity']} stands out as the highest average-priced "
            f"commodity at {format_php(top_commodity_row.iloc[0]['price'])}, which may point to "
            f"premium positioning, tighter supply, or consistently higher production and transport costs."
        )

with insight_col2:
    if not top_region_row.empty:
        render_insight_card(
            "Regional Insight",
            f"{top_region_row.iloc[0]['admin1']} records the highest average prices at "
            f"{format_php(top_region_row.iloc[0]['price'])}, suggesting stronger regional cost "
            f"pressures or distribution dynamics compared with other areas in the filtered view."
        )

with insight_col3:
    if not top_market_row.empty:
        variability_text = "relatively stable" if overall_price_std < overall_avg_price * 0.35 else "fairly dispersed"
        render_insight_card(
            "Market Insight",
            f"Prices in the current selection average {format_php(overall_avg_price)} with a standard "
            f"deviation of {overall_price_std:,.2f}, indicating a {variability_text} pricing environment. "
            f"{top_market_row.iloc[0]['market']} currently sits at the top end of the market price range."
        )


st.divider()

st.markdown('<div class="section-title">Trends</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-text">Review how average prices evolve over time across the filtered dataset.</div>',
    unsafe_allow_html=True,
)

trend_col1, trend_col2 = st.columns(2)

with trend_col1:
    daily_avg = (
        filtered_df.groupby("date", as_index=False)["price"]
        .mean()
        .sort_values("date")
    )

    st.markdown('<div class="chart-block">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Average Price Over Time</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="chart-text">Daily average price movement within the current filtered view.</div>',
        unsafe_allow_html=True,
    )
    fig, ax = plt.subplots(figsize=CHART_FIGSIZE_WIDE)
    ax.plot(
        daily_avg["date"],
        daily_avg["price"],
        color=PRIMARY_COLOR,
        linewidth=2.4,
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Average Price (PHP)")
    style_axis(ax)
    fig.autofmt_xdate(rotation=30)
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    st.markdown("</div>", unsafe_allow_html=True)

with trend_col2:
    monthly_avg = (
        filtered_df.groupby("month", as_index=False)["price"]
        .mean()
        .sort_values("month")
    )

    st.markdown('<div class="chart-block">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Monthly Average Price</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="chart-text">Smoothed monthly pricing pattern for easier comparison over time.</div>',
        unsafe_allow_html=True,
    )
    fig, ax = plt.subplots(figsize=CHART_FIGSIZE_WIDE)
    ax.plot(
        monthly_avg["month"],
        monthly_avg["price"],
        color=SECONDARY_COLOR,
        linewidth=2.4,
        marker="o",
        markersize=3.8,
    )
    ax.fill_between(
        monthly_avg["month"],
        monthly_avg["price"],
        color=ACCENT_COLOR,
        alpha=0.15,
    )
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Price (PHP)")
    style_axis(ax)
    fig.autofmt_xdate(rotation=30)
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("---")

st.markdown('<div class="section-title">Regional and Commodity Comparisons</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-text">Compare average prices across commodities and regions to identify the highest-cost segments.</div>',
    unsafe_allow_html=True,
)

comparison_col1, comparison_col2 = st.columns(2)

with comparison_col1:
    top_expensive = (
        filtered_df.groupby("commodity", as_index=False)["price"]
        .mean()
        .sort_values("price", ascending=False)
        .head(10)
        .sort_values("price")
    )

    st.markdown('<div class="chart-block">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Top 10 Most Expensive Commodities</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="chart-text">Average price ranking of the highest-cost commodities in the current selection.</div>',
        unsafe_allow_html=True,
    )
    fig, ax = plt.subplots(figsize=CHART_FIGSIZE_TALL)
    ax.barh(top_expensive["commodity"], top_expensive["price"], color=PRIMARY_COLOR)
    ax.set_xlabel("Average Price (PHP)")
    ax.set_ylabel("Commodity")
    style_axis(ax)
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    st.markdown("</div>", unsafe_allow_html=True)

with comparison_col2:
    top_regions = (
        filtered_df.groupby("admin1", as_index=False)["price"]
        .mean()
        .sort_values("price", ascending=False)
        .head(10)
        .sort_values("price")
    )

    st.markdown('<div class="chart-block">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Top 10 Regions by Average Price</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="chart-text">Regional average price comparison based on the filtered dataset.</div>',
        unsafe_allow_html=True,
    )
    fig, ax = plt.subplots(figsize=CHART_FIGSIZE_TALL)
    ax.barh(top_regions["admin1"], top_regions["price"], color=SECONDARY_COLOR)
    ax.set_xlabel("Average Price (PHP)")
    ax.set_ylabel("Region")
    style_axis(ax)
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("---")

st.markdown('<div class="section-title">Distribution and Volatility</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-text">Assess price variability across commodities and the broader distribution of prices in the filtered data.</div>',
    unsafe_allow_html=True,
)

distribution_col1, distribution_col2 = st.columns(2)

with distribution_col1:
    volatility = (
        filtered_df.groupby("commodity", as_index=False)["price"]
        .std()
        .rename(columns={"price": "price_std"})
        .dropna()
        .sort_values("price_std", ascending=False)
        .head(10)
        .sort_values("price_std")
    )

    st.markdown('<div class="chart-block">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Top 10 Most Volatile Commodities</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="chart-text">Commodity price variability measured using the standard deviation of prices.</div>',
        unsafe_allow_html=True,
    )
    fig, ax = plt.subplots(figsize=CHART_FIGSIZE_TALL)
    ax.barh(volatility["commodity"], volatility["price_std"], color=PRIMARY_COLOR)
    ax.set_xlabel("Price Standard Deviation")
    ax.set_ylabel("Commodity")
    style_axis(ax)
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    st.markdown("</div>", unsafe_allow_html=True)

with distribution_col2:
    st.markdown('<div class="chart-block">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Price Distribution Histogram</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="chart-text">Distribution of price observations across all records in the current filtered view.</div>',
        unsafe_allow_html=True,
    )
    fig, ax = plt.subplots(figsize=CHART_FIGSIZE_TALL)
    ax.hist(
        filtered_df["price"],
        bins=30,
        color=PRIMARY_COLOR,
        edgecolor="#FFFFFF",
        alpha=0.92,
    )
    ax.set_xlabel("Price (PHP)")
    ax.set_ylabel("Frequency")
    style_axis(ax)
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("---")

st.markdown('<div class="section-title">Data Preview</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-text">Inspect, export, or hide the filtered records that support the summary metrics and charts shown above.</div>',
    unsafe_allow_html=True,
)

download_col, info_col = st.columns([1, 3])
with download_col:
    st.download_button(
        label="Download Filtered CSV",
        data=convert_df_to_csv(filtered_df.sort_values("date")),
        file_name="filtered_food_prices.csv",
        mime="text/csv",
        use_container_width=True,
    )
with info_col:
    st.caption("Export the current filtered dataset for reporting, validation, or additional analysis.")

if show_raw_data:
    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.dataframe(filtered_df.sort_values("date"), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("The data preview is currently hidden. Use the toggle above to display the filtered records.")
