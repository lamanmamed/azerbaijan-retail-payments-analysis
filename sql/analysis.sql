-- Azerbaijan Retail & Digital Payments Analytics
-- SQLite-compatible queries used to answer the main business questions.

-- 1. How quickly did cashless card payments grow from 2022 to 2025?
WITH endpoints AS (
    SELECT
        MAX(CASE WHEN year = 2022 THEN cashless_card_value_bln_azn END) AS value_2022,
        MAX(CASE WHEN year = 2025 THEN cashless_card_value_bln_azn END) AS value_2025,
        MAX(CASE WHEN year = 2022 THEN cashless_share_pct END) AS share_2022,
        MAX(CASE WHEN year = 2025 THEN cashless_share_pct END) AS share_2025
    FROM payment_cards
)
SELECT
    value_2022,
    value_2025,
    ROUND((value_2025 / value_2022 - 1) * 100, 1) AS value_growth_pct,
    ROUND(share_2025 - share_2022, 1) AS share_change_percentage_points
FROM endpoints;


-- 2. How important is e-commerce within domestic cashless card payments?
SELECT
    year,
    ecommerce_value_bln_azn,
    cashless_card_value_bln_azn,
    ROUND(ecommerce_value_bln_azn / cashless_card_value_bln_azn * 100, 1)
        AS ecommerce_share_of_cashless_value_pct
FROM payment_cards
ORDER BY year;


-- 3. Are POS payments becoming smaller and more frequent?
SELECT
    year,
    pos_count_mln,
    pos_value_bln_azn,
    ROUND(pos_value_bln_azn * 1000.0 / pos_count_mln, 2) AS implied_average_pos_ticket_azn
FROM payment_cards
ORDER BY year;


-- 4. How has the retail mix changed?
SELECT
    period,
    period_type,
    total_retail_bln_azn,
    ROUND(food_bev_tobacco_bln_azn / total_retail_bln_azn * 100, 1)
        AS food_bev_tobacco_share_pct,
    real_growth_total_pct,
    real_growth_food_bev_tobacco_pct,
    real_growth_nonfood_pct
FROM retail_turnover
ORDER BY
    CASE period
        WHEN '2024' THEN 1
        WHEN '2025' THEN 2
        ELSE 3
    END;
