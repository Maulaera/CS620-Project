import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "data/Adelphi University Class of 2024 (1).xlsx"
df = pd.read_excel(file_path)

print(df.columns)


x = df['Ethnicity']
y = df['New First-Year Students']

print(f"Length of ethnin: {len(x)}")
print(f"Length of percen: {len(y)}")

#y = y.astype(str).str.rstrip('%')
#y = pd.to_numeric(y, errors='coerce')

#plt.bar(x,y) # Bar Chart

#plt.xlabel('Student Ethnicities')
#plt.ylabel('Percentage')
#plt.title('Adelphi Admissions by Ethnicity')

#plt.show()
