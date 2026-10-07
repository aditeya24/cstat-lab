import pandas as pd

data = {
    "Name": ["Alen", "Abhinav", "Aditya", "Abhijith"],
    "Department": ["HR", "IT", "IT", "HR"],
    "Salary": [50000, 60000, 55000, 65000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Name",
    aggfunc="mean",
    fill_value=0
)

print("\nPivot Table:")
print(pivot)

crosstab = pd.crosstab(df["Department"], df["Name"])

print("\nCross Tabulation:")
print(crosstab)
