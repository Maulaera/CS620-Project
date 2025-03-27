# Maulahna Robinson
# Makendra Crosby
# CS620
# Note: 72.8% acceptance rate (easy acceptance)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = "data/Adelphi University Class of 2024.xlsx"
df = pd.read_excel(file_path) 

mean_sat_reading = df.loc[df.iloc[:, 0] == "Mean SAT Evidence-based Reading and Writing"].iloc[0, 1]
mean_sat_math = df.loc[df.iloc[:, 0] == "Mean SAT Math"].iloc[0, 1]
mean_total_sat = df.loc[df.iloc[:, 0] == "Mean total SAT"].iloc[0, 1]
mean_gpa = df.loc[df.iloc[:, 0] == "Mean high school GPA"].iloc[0, 1]

mean_sat_reading = float(mean_sat_reading)
mean_sat_math = float(mean_sat_math)
mean_total_sat = float(mean_total_sat)
mean_gpa = float(mean_gpa)

sat_categories = ["SAT Reading", "SAT Math", "Total SAT"]
sat_values = [mean_sat_reading, mean_sat_math, mean_total_sat]


fig, axes = plt.subplots(1, 2, figsize=(12, 5))

#SAT Scores
sns.barplot(x=sat_categories, y=sat_values, palette="viridis", ax=axes[0])
# axes[0].set_xlabel("")
axes[0].set_ylabel("Score")
axes[0].set_title("Average SAT Scores")
axes[0].set_ylim(0, 1600)  
# Add values on bars
for i, v in enumerate(sat_values):
    axes[0].text(i, v + 30, str(v), ha='center', fontsize=12)  # Adjust text placement

# GPA
axes[1].bar(["Admitted Freshmen"], [mean_gpa], color="teal")
# axes[1].set_xlabel("Admitted Freshmen")
axes[1].set_ylabel("GPA")
axes[1].set_title("Average High School GPA")
axes[1].set_ylim(0, 4.0)  
axes[1].text(0, mean_gpa + 0.1, str(mean_gpa), ha='center', fontsize=12)  # Adjust text placement

fig.suptitle("Adelphi University Class of 2024 - SAT & GPA Statistics", fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()
