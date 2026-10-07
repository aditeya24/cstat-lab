import matplotlib.pyplot as plt

heights = [
    150, 155, 160, 162, 165,
    168, 170, 172, 175, 178,
    180, 165, 170, 158, 163
]

plt.hist(heights, bins=5, color="lightgreen", edgecolor="black")

plt.xlabel("Height (cm)")
plt.ylabel("Number of Students")
plt.title("Distribution of Classmates' Heights")

plt.show()