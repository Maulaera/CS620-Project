# Maulahna Robinson
# Makendra McCrosby
# CS620

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "data/Adelphi University Class of 2024.xlsx"
df = pd.read_excel(file_path)

# print(df.columns) (THIS WAS TO MAKE SURE THE DATA WAS BEING READ CORRECTLY)


x = df['Ethnicity']
y = df['New First-Year Students']

# print(f"Length of ethnin: {len(x)}") (THIS WAS FOR DEBUGGING AND TESTING)
# print(f"Length of percen: {len(y)}") (THIS WAS FOR DEBUGGING AND TESTING)

y = y.astype(str).str.rstrip('%')
y = pd.to_numeric(y, errors='coerce')

plt.bar(x,y) # Bar Chart

plt.xlabel('Student Ethnicities')
plt.ylabel('Percentage')
plt.title('Adelphi Admissions by Ethnicity')

plt.show()
