import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")

print(df.head())
print(df.columns)


month = df["month_number"].to_numpy()
profit = df["total_profit"].to_numpy()

facecream = df["facecream"].to_numpy()
facewash = df["facewash"].to_numpy()
toothpaste = df["toothpaste"].to_numpy()
bathingsoap = df["bathingsoap"].to_numpy()
shampoo = df["shampoo"].to_numpy()
moisturizer = df["moisturizer"].to_numpy()
total_units = df["total_units"].to_numpy()



plt.figure(figsize=(8, 5))

plt.plot(month, profit, marker="o")

plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit per Month")

plt.show()



plt.figure(figsize=(8, 5))

plt.plot(
    month,
    profit,
    color="red",
    linestyle="--",
    marker="o",
    linewidth=2,
    markersize=6
)

plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Styled Total Profit Line Plot")
plt.grid(True)

plt.show()



plt.figure(figsize=(10, 6))

plt.plot(month, facecream, marker="o", label="Face Cream")
plt.plot(month, facewash, marker="s", label="Face Wash")
plt.plot(month, toothpaste, marker="^", label="Toothpaste")
plt.plot(month, bathingsoap, marker="D", label="Bathing Soap")

plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.title("Monthly Product Sales")

plt.legend()
plt.grid(True)

plt.show()



plt.figure(figsize=(8, 5))

plt.scatter(
    total_units,
    profit,
    color="purple"
)

plt.xlabel("Total Units Sold")
plt.ylabel("Total Profit")
plt.title("Total Units vs Total Profit")

plt.show()



products = [
    "Face Cream",
    "Face Wash",
    "Toothpaste",
    "Bathing Soap",
    "Shampoo",
    "Moisturizer"
]

sales = [
    facecream.sum(),
    facewash.sum(),
    toothpaste.sum(),
    bathingsoap.sum(),
    shampoo.sum(),
    moisturizer.sum()
]

plt.figure(figsize=(10, 6))

plt.bar(
    products,
    sales,
    color="skyblue",
    edgecolor="black"
)

plt.xlabel("Product")
plt.ylabel("Total Units Sold")
plt.title("Total Sales by Product")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()



plt.figure(figsize=(10, 6))

plt.bar(
    products,
    sales,
    color="orange",
    edgecolor="black"
)

plt.xlabel("Product")
plt.ylabel("Total Units Sold")
plt.title("Total Sales by Product")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("company_sales_bar_chart.png", dpi=300)

plt.show()



plt.figure(figsize=(8, 5))

plt.hist(
    profit,
    bins=6,
    color="lightgreen",
    edgecolor="black"
)

plt.xlabel("Total Profit")
plt.ylabel("Frequency")
plt.title("Distribution of Total Profit")

plt.show()



plt.figure(figsize=(8, 8))

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Product")

plt.show()



fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].plot(month, profit, marker="o")

axes[0, 0].set_title("Total Profit")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Profit")


axes[0, 1].bar(
    products,
    sales,
    color="skyblue"
)

axes[0, 1].set_title("Product Sales")
axes[0, 1].set_xlabel("Product")
axes[0, 1].set_ylabel("Units Sold")

axes[0, 1].tick_params(axis="x", rotation=45)


axes[1, 0].scatter(
    total_units,
    profit,
    color="purple"
)

axes[1, 0].set_title("Units vs Profit")
axes[1, 0].set_xlabel("Total Units")
axes[1, 0].set_ylabel("Total Profit")


axes[1, 1].hist(
    profit,
    bins=6,
    color="lightgreen",
    edgecolor="black"
)

axes[1, 1].set_title("Profit Distribution")
axes[1, 1].set_xlabel("Total Profit")
axes[1, 1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 6))

plt.stackplot(
    month,
    facecream,
    facewash,
    toothpaste,
    bathingsoap,
    shampoo,
    moisturizer,
    labels=[
        "Face Cream",
        "Face Wash",
        "Toothpaste",
        "Bathing Soap",
        "Shampoo",
        "Moisturizer"
    ]
)

plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.title("Stacked Product Sales")

plt.legend(loc="upper left")

plt.show()