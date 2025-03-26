# Maulahna Robinson
# Makendra Crosby
# CS620

import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/Ivy League Averages.xlsx"
df = pd.read_excel(file_path)

# print(df.columns) {this was for debugging}

# Clean the SAT and ACT columns (handling ranges like '1470-1560')
df['Average SAT score'] = df['Average SAT score'].astype(str).apply(lambda x: sum(map(int, x.split('-'))) / 2 if '-' in x else float(x))
df['Average ACT Score'] = df['Average ACT Score'].astype(str).apply(lambda x: sum(map(int, x.split('-'))) / 2 if '-' in x else float(x))

fig, axes = plt.subplots(1,3, figsize=(18,5))

# SAT Score Bar Chart
axes[0].bar(df['University'], df['Average SAT score'], color='blue')
axes[0].set_title('Average SAT scores')
axes[0].set_xlabel('Ivy League Universities')
axes[0].set_ylabel('SAT Score')
axes[0].tick_params(axis='x', rotation=45)

# ACT Score Bar Chart
axes[1].bar(df['University'], df['Average ACT Score'], color='green')
axes[1].set_title('Average ACT Scores')
axes[1].set_xlabel('Ivy League Universities')
axes[1].set_ylabel('ACT Score')
axes[1].tick_params(axis='x', rotation=45)

# GPA Bar Chart
axes[2].bar(df['University'], df['Average GPA'], color='purple')
axes[2].set_title('Average GPA Scores')
axes[2].set_xlabel('Ivy League Universities')
axes[2].set_ylabel('GPA')
axes[2].tick_params(axis='x', rotation=45)

# Adjust layout and display
plt.tight_layout()
plt.show()

