# Azerbaijan Retail & Digital Payments Analytics

A compact business analytics project using official public data to examine how consumer spending and payment behaviour are changing in Azerbaijan.

The analysis combines payment-card statistics from the **Central Bank of the Republic of Azerbaijan** with retail-turnover data from the **State Statistical Committee of the Republic of Azerbaijan**.

## Business question

**How is consumer spending in Azerbaijan changing, and what does the shift toward digital payments imply for retailers?**

Rather than building a predictive model, this project focuses on a practical analytics workflow:

1. structure public data into analysis-ready tables;
2. calculate interpretable business metrics;
3. use SQL and Python to test trends;
4. translate the results into implications for a retail business.

## Key findings

### 1. Cashless card payments have moved from minority to majority behaviour

The value of domestic cashless card payments increased from **AZN 24.4B in 2022 to AZN 99.1B in 2025**, an increase of about **306%**. Over the same period, the cashless share of domestic card turnover rose from **43.2% to 67.6%**.

For a retailer, this means digital payment acceptance is no longer a secondary channel. It is part of the core customer experience.

### 2. Domestic e-commerce has expanded even faster

Domestic e-commerce payment value increased from **AZN 18.5B in 2022 to AZN 86.4B in 2025**, approximately **366% growth**.

E-commerce represented about **76% of domestic cashless card value in 2022** and about **87% in 2025**. The comparison is useful as a channel indicator, although the public data describes payment flows rather than retailer-level online sales.

### 3. Cards are increasingly used for smaller everyday purchases

Cashless POS transaction count increased from **199.1M in 2022 to 760.5M in 2025** (+282%), while POS transaction value increased from **AZN 5.8B to AZN 12.7B** (+118%).

The implied average POS transaction fell from roughly **AZN 29.2 to AZN 16.7**. That does not prove a change in any individual customer's behaviour, but at market level it is consistent with cards being used more frequently for lower-value, everyday purchases.

This is particularly relevant to grocery and convenience retail, where transaction frequency is high and basket values are relatively small.

### 4. Food remains a large, comparatively stable part of Azerbaijani retail spending

Total retail turnover increased from **AZN 62.2B in 2024 to AZN 67.6B in 2025**. The official real-growth rate was **3.8%**, while food, beverages and tobacco grew **1.2% in real terms** and non-food goods grew **6.8%**.

In January-August 2026, overall retail turnover was **AZN 44.3B** and real growth was **3.9% year over year**. Food products grew **1.5%**, beverages and tobacco **1.4%**, and non-food goods **6.9%** in real terms.

Food-related categories still accounted for roughly **55% of retail spending**, making the segment large even when its real growth is slower than non-food.

## What this could mean for a retailer

The data points to a market where:

- digital payment acceptance is increasingly essential;
- e-commerce has become a major payment channel;
- frequent, lower-value card transactions are becoming more common;
- grocery-related spending represents a large and relatively stable share of total retail demand.

The data does **not** show retailer market shares, household-level baskets, customer retention or delivery demand, so those questions would require transaction-level or company-level data.

## Repository structure

```text
.
├── data/
│   ├── payment_cards_2022_2025.csv
│   └── retail_turnover_2024_2026.csv
├── sql/
│   └── analysis.sql
├── src/
│   └── analysis.py
├── SOURCES.md
└── requirements.txt
```

## Analysis workflow

The Python script:

- loads and validates the two public-data tables;
- calculates growth rates and channel shares;
- creates an in-memory SQLite database;
- runs SQL queries for the main business metrics;
- generates charts in a local `figures/` directory.

Run:

```bash
pip install -r requirements.txt
python src/analysis.py
```

## Tools

**Python · Pandas · SQL (SQLite) · Matplotlib**

## Data notes

The Central Bank reports payment statistics in both transaction counts and values. The 2025 e-commerce transaction count is reported as **1.5 billion** in the annual review and is therefore rounded in this dataset. Values are kept in the units used by the official source where possible.

Retail values are nominal AZN turnover. Official year-over-year growth rates are reported in **real terms**, so nominal changes calculated from turnover values should not be confused with inflation-adjusted growth.

See [SOURCES.md](SOURCES.md) for the exact source documents and field definitions.
