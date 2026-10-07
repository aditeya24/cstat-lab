import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lois_continuous.csv", header=1, low_memory=False)

swale = df[df["SITE_NAME"] == "Swale at Catterick Bridge"]

mean_temperature = pd.to_numeric(
    swale["0476 (Cel)"], errors="coerce"
).mean()

median_oxygen = pd.to_numeric(
    swale["0474 (% satn)"], errors="coerce"
).median()

print("Mean Temperature:", mean_temperature, "°C")
print("Median Dissolved Oxygen:", median_oxygen, "% saturation")

temperature = pd.to_numeric(
    swale["0476 (Cel)"], errors="coerce"
).dropna()

plt.hist(temperature, bins=10, edgecolor="black")

plt.xlabel("Water Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Water Temperature at Swale at Catterick Bridge")
plt.show()