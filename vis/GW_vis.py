# Maulahna Robinson
# Makendra Crosby
# CS620
# Note: 49% acceptance rate (moderate difficulty acceptance)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "data/George Washington Class of 2025.xlsx"
df = pd.read_excel(file_path)

sat_ranges = ["700-800", "600-699", "500-599", "400-499"]
sat_midpoints = [750, 650, 550, 450]
sat_reading = [56.0, 38.6, 5.5, 0.0]
sat_math = [49.6, 42.0, 7.8, 0.5]
sat_composite_ranges = ["1400-1600", "1200-1399", "1000-1199"]
sat_composite_midpoints = [1500, 1300, 1100]
sat_composite = [50.5, 44.7, 4.8]

act_ranges = ["30-36", "24-29", "18-23"]
act_midpoints = [33, 26.5, 20.5]
act_composite = [82.0, 17.0, 1.1]
act_english = [85.5, 12.8, 1.7]
act_math = [49.6, 45.1, 5.3]

def weighted_avg(midpoints, percentages):
    return sum(m * (p / 100) for m, p in zip(midpoints, percentages))

mean_sat_reading = weighted_avg(sat_midpoints, sat_reading)
mean_sat_math = weighted_avg(sat_midpoints, sat_math)
mean_sat_total = weighted_avg(sat_composite_midpoints, sat_composite)

mean_act_composite = weighted_avg(act_midpoints, act_composite)
mean_act_english = weighted_avg(act_midpoints, act_english)
mean_act_math = weighted_avg(act_midpoints, act_math)

sat_categories = ["SAT Reading", "SAT Math", "Total SAT"]
sat_values = [mean_sat_reading, mean_sat_math, mean_sat_total]

act_categories = ["ACT Composite", "ACT English", "ACT Math"]
act_values = [mean_act_composite, mean_act_english, mean_act_math]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.barplot(x=sat_categories, y=sat_values, palette="mako")
plt.title("GW University - Estimated Average SAT Scores", fontsize=14, fontweight='bold')
plt.ylabel("Score")
plt.ylim(0, 1600)
for i, v in enumerate(sat_values):
    plt.text(i, v + 25, f"{v:.2f}", ha='center', fontsize=12)

plt.subplot(1, 2, 2)
sns.barplot(x=act_categories, y=act_values, palette="rocket")
plt.title("GW University - Estimated Average ACT Scores", fontsize=14, fontweight='bold')
plt.ylabel("Score")
plt.ylim(0, 36)
for i, v in enumerate(act_values):
    plt.text(i, v + 0.5, f"{v:.2f}", ha='center', fontsize=12)

plt.tight_layout()
plt.show()

