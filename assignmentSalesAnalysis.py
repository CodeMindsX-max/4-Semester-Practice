import csv
import random
from datetime import date, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Product:
    def __init__(self, product_id, name, category, price, quantity_sold, sale_date):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity_sold = quantity_sold
        self.sale_date = sale_date

    def get_month(self):
        if isinstance(self.sale_date, str):
            return int(self.sale_date[5:7])
        return self.sale_date.month

    def get_revenue(self):
        return self.price * self.quantity_sold

    def __str__(self):
        return (
            f"Product(product_id={self.product_id}, name='{self.name}', "
            f"category='{self.category}', price={self.price}, "
            f"quantity_sold={self.quantity_sold}, sale_date='{self.sale_date}')"
        )


# ------------------------------
# DATA GENERATION
# ------------------------------
def generate_sample_data(num_records=100):
    categories = ("Electronics", "Clothing", "Home", "Books", "Sports")
    start_date = date.today() - timedelta(days=365)

    with open("salesData.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["product_id", "name", "category", "price", "quantity_sold", "sale_date"]
        )

        for product_id in range(1, num_records + 1):
            category = random.choice(categories)
            name = f"{category} Item {random.randint(1, 50)}"
            price = round(random.uniform(5.0, 500.0), 2)
            quantity_sold = random.randint(1, 25)
            sale_date = (
                start_date + timedelta(days=random.randint(0, 365))
            ).isoformat()

            writer.writerow(
                [product_id, name, category, price, quantity_sold, sale_date]
            )


# ------------------------------
# DATA PROCESSING
# ------------------------------
def products_to_dataframe():
    df = pd.read_csv("salesData.csv")
    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["revenue"] = df["price"] * df["quantity_sold"]
    df["month"] = df["sale_date"].dt.month
    return df


def sales_by_category(df):
    return df.groupby("category")["revenue"].sum()


def monthly_sales_trend(df):
    return df.groupby("month")["revenue"].sum().sort_index()


def price_vs_quantity(df):
    return df["price"], df["quantity_sold"]


def top_products(df, n=5):
    return df.sort_values(by="revenue", ascending=False).head(n)


# ------------------------------
# VISUALIZATIONS
# ------------------------------
def plot_category_performance(series):
    plt.figure()
    series.plot(kind="bar")
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Revenue")
    plt.show()


def plot_monthly_trend(series):
    plt.figure()
    series.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Revenue")
    plt.show()


def plot_price_quantity_scatter(price_series, quantity_series):
    plt.figure()
    plt.scatter(price_series, quantity_series)
    plt.title("Price vs Quantity Sold")
    plt.xlabel("Price")
    plt.ylabel("Quantity Sold")
    plt.show()


def plot_sales_histogram(df, bins=10):
    plt.figure()
    plt.hist(df["revenue"], bins=bins)
    plt.title("Revenue Distribution")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.show()


def plot_top_products_bar(df):
    plt.figure()
    plt.barh(df["name"], df["revenue"])
    plt.title("Top Products by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Product")
    plt.show()


# ------------------------------
# DASHBOARD
# ------------------------------
def sales_dashboard():
    print("Generating Sample Data...")
    generate_sample_data(200)

    print("Loading Data...")
    df = products_to_dataframe()

    print("\nSummary Statistics:")
    print(df.describe())

    category_sales = sales_by_category(df)
    monthly_sales = monthly_sales_trend(df)
    price_series, quantity_series = price_vs_quantity(df)
    top_df = top_products(df)

    plot_category_performance(category_sales)
    plot_monthly_trend(monthly_sales)
    plot_price_quantity_scatter(price_series, quantity_series)
    plot_sales_histogram(df)
    plot_top_products_bar(top_df)


# Run dashboard
if __name__ == "__main__":
    sales_dashboard()