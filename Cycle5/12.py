import matplotlib.pyplot as plt

continents = [
    "Asia", "Africa", "North America",
    "South America", "Antarctica", "Europe", "Australia"
]

areas = [44.58, 30.37, 24.71, 17.84, 14.20, 10.18, 8.53]

plt.bar(continents, areas, color="skyblue", edgecolor="black")
plt.xlabel("Continent")
plt.ylabel("Area (million km²)")
plt.title("Areas of Continents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()