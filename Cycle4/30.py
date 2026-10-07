import pandas as pd

df = pd.read_csv("crime_dataset_india.csv")

columns_to_analyze = ['Victim Age', 'Police Deployed']

for col in columns_to_analyze:
    print(f"--- Statistics for {col} ---")
    print(f"Mean: {df[col].mean()}")
    print(f"Median: {df[col].median()}")
    print(f"Variance: {df[col].var()}")
