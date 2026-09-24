# Sources and data definitions

All inputs in this repository come from official public sources.

## Central Bank of the Republic of Azerbaijan

### 2022 — Digital Payments Report 2022
https://uploads.cbar.az/assets/Digital%20Payments%20Report_2022.pdf

Used for:
- total domestic payment-card transaction value;
- domestic cashless card-payment value and share;
- domestic e-commerce transaction count and value;
- cashless POS transaction count and value.

### 2023 — Digital Payments Report 2023
https://uploads.cbar.az/assets/PS%20annual%20report%20ENG.pdf

Used for:
- payment cards in circulation;
- total domestic card-payment value;
- cashless card-payment value and share;
- domestic e-commerce transaction count and value;
- cashless POS activity.

### 2024 — Digital Payments Report 2024
https://uploads.cbar.az/assets/Digital%20payments%20report_2024__march_2025_KR_MI%20%28002%29.pdf

Used for:
- 2022–2024 historical comparison;
- payment cards in circulation;
- total domestic card-payment value;
- domestic cashless card-payment value and share;
- e-commerce count and value;
- cashless POS count and value.

### 2025 — Digital Payments Review 2025
https://uploads.cbar.az/assets/Digital%20payments%20review_2025_KR_MI_final.pdf

Used for:
- payment cards in circulation;
- total domestic payment-card value;
- domestic cashless payment-card value and share;
- e-commerce transaction value and reported transaction count;
- cashless POS count and value.

The 2025 report states that e-commerce transaction count reached **1.5 billion**. Because this figure is rounded in the source, it should not be used for high-precision average-ticket calculations.

### Current payment-system statistics
https://www.cbar.az/page-45/payment-?language=en

This page provides the Central Bank's regularly updated payment-system workbooks.

## State Statistical Committee of the Republic of Azerbaijan

### Retail trade turnover — 2024
https://www.stat.gov.az/special_version/news/index.php?id=6163

Used for:
- total retail turnover;
- food, beverages and tobacco turnover;
- non-food turnover;
- official real year-over-year growth rates;
- average monthly per-capita retail purchases.

### Retail trade turnover — 2025
https://stat.gov.az/news/index.php?id=6587&lang=en

Used for the same annual retail indicators for 2025.

### Retail trade turnover — January-August 2026
https://stat.gov.az/news/index.php?id=6923&lang=en

Used for:
- year-to-date 2026 retail turnover;
- food, beverages and tobacco turnover;
- non-food turnover;
- real year-over-year growth;
- average monthly per-capita purchases.

## Important interpretation notes

1. **Nominal values vs real growth**  
   Turnover values are reported in current AZN. The State Statistical Committee's growth rates are explicitly reported in real terms. A percentage change calculated directly from nominal turnover is therefore not the same as official real growth.

2. **Annual vs year-to-date periods**  
   The 2026 retail row covers January-August only and must not be compared directly with full-year 2024 or 2025 totals.

3. **Market-level, not customer-level data**  
   These data describe aggregate payment and retail activity. They cannot identify customer retention, individual basket size, household behaviour or retailer market share.

4. **Average POS ticket**  
   The project calculates an implied average transaction value as total cashless POS value divided by POS transaction count. This is a market-level ratio, not an observed individual basket value.
