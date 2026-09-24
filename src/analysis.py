from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIGURES_DIR = ROOT / "figures"
SQL_FILE = ROOT / "sql" / "analysis.sql"


def load_data():
    payments = pd.read_csv(DATA_DIR / "payment_cards_2022_2025.csv")
    retail = pd.read_csv(DATA_DIR / "retail_turnover_2024_2026.csv")

    required_payment_columns = {
        "year",
        "domestic_card_value_bln_azn",
        "cashless_card_value_bln_azn",
        "cashless_share_pct",
        "ecommerce_value_bln_azn",
        "ecommerce_count_mln",
        "pos_value_bln_azn",
        "pos_count_mln",
        "payment_cards_mln",
    }
    missing = required_payment_columns - set(payments.columns)
    if missing:
        raise ValueError(f"Missing payment columns: {sorted(missing)}")

    return payments, retail


def calculate_metrics(payments, retail):
    start = payments.loc[payments["year"] == 2022].iloc[0]
    end = payments.loc[payments["year"] == 2025].iloc[0]

    metrics = {
        "cashless_value_growth_pct": (
            end["cashless_card_value_bln_azn"]
            / start["cashless_card_value_bln_azn"]
            - 1
        )
        * 100,
        "cashless_share_change_pp": (
            end["cashless_share_pct"] - start["cashless_share_pct"]
        ),
        "ecommerce_value_growth_pct": (
            end["ecommerce_value_bln_azn"]
            / start["ecommerce_value_bln_azn"]
            - 1
        )
        * 100,
        "pos_count_growth_pct": (
            end["pos_count_mln"] / start["pos_count_mln"] - 1
        )
        * 100,
        "pos_value_growth_pct": (
            end["pos_value_bln_azn"] / start["pos_value_bln_azn"] - 1
        )
        * 100,
    }

    payments = payments.copy()
    payments["pos_avg_ticket_azn"] = (
        payments["pos_value_bln_azn"] * 1000 / payments["pos_count_mln"]
    )
    payments["ecommerce_share_of_cashless_pct"] = (
        payments["ecommerce_value_bln_azn"]
        / payments["cashless_card_value_bln_azn"]
        * 100
    )

    annual_retail = retail[retail["period_type"] == "annual"].copy()
    return metrics, payments, annual_retail


def run_sql(payments, retail):
    with sqlite3.connect(":memory:") as conn:
        payments.to_sql("payment_cards", conn, index=False)
        retail.to_sql("retail_turnover", conn, index=False)

        queries = SQL_FILE.read_text(encoding="utf-8").split(";")
        results = []
        for query in queries:
            query = query.strip()
            if not query:
                continue
            results.append(pd.read_sql_query(query, conn))
    return results


def make_charts(payments, annual_retail):
    FIGURES_DIR.mkdir(exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.plot(payments["year"], payments["cashless_share_pct"], marker="o")
    plt.title("Cashless share of domestic card turnover")
    plt.xlabel("Year")
    plt.ylabel("Cashless share (%)")
    plt.xticks(payments["year"])
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "cashless_share.png", dpi=180)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.plot(payments["year"], payments["pos_avg_ticket_azn"], marker="o")
    plt.title("Implied average cashless POS transaction")
    plt.xlabel("Year")
    plt.ylabel("AZN per transaction")
    plt.xticks(payments["year"])
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "pos_average_ticket.png", dpi=180)
    plt.close()

    chart = annual_retail.set_index("period")[
        ["food_bev_tobacco_bln_azn", "nonfood_bln_azn"]
    ]
    chart.plot(kind="bar", figsize=(8, 5))
    plt.title("Azerbaijan retail turnover by broad category")
    plt.xlabel("Year")
    plt.ylabel("AZN billion")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "retail_mix.png", dpi=180)
    plt.close()


def main():
    payments, retail = load_data()
    metrics, payments_enriched, annual_retail = calculate_metrics(payments, retail)

    print("Key metrics")
    print("-----------")
    for name, value in metrics.items():
        print(f"{name}: {value:.1f}")

    print("\nImplied POS average ticket")
    print(
        payments_enriched[
            ["year", "pos_avg_ticket_azn", "ecommerce_share_of_cashless_pct"]
        ].round(2).to_string(index=False)
    )

    print("\nSQL outputs")
    print("-----------")
    for i, result in enumerate(run_sql(payments, retail), start=1):
        print(f"\nQuery {i}")
        print(result.to_string(index=False))

    make_charts(payments_enriched, annual_retail)
    print(f"\nCharts written to: {FIGURES_DIR}")


if __name__ == "__main__":
    main()
