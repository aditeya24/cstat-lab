import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/home/mec/cu5-cstat/Cycle2/BankChurners.csv", na_values="Unknown")

cols_to_drop = [
    "CLIENTNUM",
    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"
]
df.drop(columns=cols_to_drop, errors='ignore', inplace=True)

print(df.describe(include='all').T)

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

attrition_counts = df['Attrition_Flag'].value_counts()
axes[0, 0].pie(
    attrition_counts, 
    labels=attrition_counts.index, 
    autopct='%1.1f%%', 
    colors=['#2b5c8f', '#d95f02']
)
axes[0, 0].set_title('Attrition Ratio', fontsize=14, fontweight='bold')

sns.countplot(data=df, x='Marital_Status', hue='Marital_Status', palette='Blues_r', ax=axes[0, 1], legend=False)
axes[0, 1].set_title('Marital Status Distribution', fontsize=14, fontweight='bold')

sns.boxplot(data=df, x='Attrition_Flag', y='Total_Relationship_Count', hue='Attrition_Flag', palette='Set2', ax=axes[1, 0], legend=False)
axes[1, 0].set_title('Product Count by Attrition Status', fontsize=14, fontweight='bold')

corr = df.select_dtypes(include=[np.number]).corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

sns.heatmap(
    corr, 
    mask=mask, 
    cmap='coolwarm', 
    cbar=True, 
    square=True, 
    ax=axes[1, 1],
    cbar_kws={"shrink": 0.8}
)
axes[1, 1].set_title('Correlation Matrix', fontsize=14, fontweight='bold')

axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=45, ha='right', fontsize=9)
axes[1, 1].set_yticklabels(axes[1, 1].get_yticklabels(), rotation=0, fontsize=9)

plt.tight_layout()
plt.show()
