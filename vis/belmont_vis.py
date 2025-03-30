# Maulahna Robinson
# Makendra Crosby
# CS620

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = "data/Belmont University Class of 2025.xlsx"
df = pd.read_excel(file_path) 

sat_ranges = ["700-800", "600-699", "500-599", "400-499", "300-399", "200-299"]
sat_midpoints = [750, 650, 550, 450, 350, 250]
sat_reading = [21.98, 50.12, 24.20, 3.70, 0.00, 0.00]
sat_math = [11.85, 43.46, 38.52, 6.17, 0.00, 0.00]
sat_composite = [12.10, 54.57, 29.38, 3.95, 0.00, 0.00]

act_ranges = ["30-36", "24-29", "18-23", "12-17", "6-11", "Below 6"]
act_midpoints = [33, 26.5, 20.5, 14.5, 8.5, 3]
act_composite = [31.56, 43.56, 20.79, 4.09, 0.00, 0.00]
act_english = [40.84, 33.04, 20.54, 5.33, 0.25, 0.00]
act_math = [14.11, 46.53, 27.60, 11.76, 0.00, 0.00]

gpa_ranges = ["4.0", "3.75-3.99", "3.50-3.74", "3.25-3.49", "3.00-3.24", "2.50-2.99", "2.0-2.49", "1.0-1.99", "<1.0"]
gpa_midpoints = [4.0, 3.875, 3.625, 3.375, 3.125, 2.75, 2.25, 1.5, 1.0]
gpa_percentages = [39.77, 21.17, 14.61, 11.05, 7.49, 5.53, 0.38, 0.00, 0.00]

def weighted_avg(midpoints, percentages):
    return sum(m * (p / 100) for m, p in zip(midpoints, percentages))

mean_sat_reading = weighted_avg(sat_midpoints, sat_reading)
mean_sat_math = weighted_avg(sat_midpoints, sat_math)
mean_sat_total = weighted_avg(sat_midpoints, sat_composite)

mean_act_composite = weighted_avg(act_midpoints, act_composite)
mean_act_english = weighted_avg(act_midpoints, act_english)
mean_act_math = weighted_avg(act_midpoints, act_math)

mean_gpa = weighted_avg(gpa_midpoints, gpa_percentages)

sat_categories = ["SAT Reading", "SAT Math", "Total SAT"]
sat_values = [mean_sat_reading, mean_sat_math, mean_sat_total]

act_categories = ["ACT Composite", "ACT English", "ACT Math"]
act_values = [mean_act_composite, mean_act_english, mean_act_math]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
sns.barplot(x=sat_categories, y=sat_values, palette="viridis")
plt.title("Belmont University - Estimated Average SAT Scores", fontsize=14, fontweight='bold')
plt.ylabel("Score")
plt.ylim(0, 1600)
for i, v in enumerate(sat_values):
    plt.text(i, v + 25, f"{v:.2f}", ha='center', fontsize=12)

plt.subplot(2, 2, 2)
sns.barplot(x=act_categories, y=act_values, palette="viridis")
plt.title("Belmont University - Estimated Average ACT Scores", fontsize=14, fontweight='bold')
plt.ylabel("Score")
plt.ylim(0, 36)
for i, v in enumerate(act_values):
    plt.text(i, v + 0.5, f"{v:.2f}", ha='center', fontsize=12)

plt.subplot(2, 2, 3)
sns.barplot(x=["Average GPA"], y=[mean_gpa], palette="viridis")
plt.title("Belmont University - Estimated Average GPA", fontsize=14, fontweight='bold')
plt.ylabel("GPA")
plt.ylim(0, 4.0)
plt.text(0, mean_gpa + 0.05, f"{mean_gpa:.2f}", ha='center', fontsize=12)

plt.tight_layout()
plt.show()