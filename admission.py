import pandas as pd
import os

# Define the directory and files
data_folder = "data"
file_names = [
    "Adelphi University Class of 2024.xlsx",
    "Belmont University Class of 2025.xlsx",
    "George Washington Class of 2025.xlsx",
    "Ivy League Averages.xlsx"
]

# Function to standardize SAT/ACT score ranges
def score_match(user_score, school_score):
    try:
        if pd.isna(school_score):
            return "N/A"
        if "-" in str(school_score):
            low, high = map(int, str(school_score).split("-"))
            if user_score >= high:
                return "Likely"
            elif user_score >= low:
                return "Competitive"
            else:
                return "Reach"
        else:
            school_score = float(school_score)
            if user_score >= school_score + 50:
                return "Likely"
            elif user_score >= school_score - 50:
                return "Competitive"
            else:
                return "Reach"
    except:
        return "N/A"

# Get user input
user_sat = input("Enter your SAT score (or leave blank): ")
user_act = input("Enter your ACT score (or leave blank): ")
user_gpa = input("Enter your GPA (or leave blank): ")

# Convert inputs
user_sat = int(user_sat) if user_sat.strip().isdigit() else None
user_act = int(user_act) if user_act.strip().isdigit() else None
try:
    user_gpa = float(user_gpa) if user_gpa.strip() != "" else None
except:
    user_gpa = None

if not any([user_sat, user_act, user_gpa]):
    print("Please enter at least one valid score.")
    exit()

print("\n===== Admission Predictions =====")

# Process each file
for file in file_names:
    filepath = os.path.join(data_folder, file)
    
    try:
        df = pd.read_excel(filepath)
    except Exception as e:
        print(f"\nCould not read {file}: {e}")
        continue

    # Look for the row that contains 'University' or has a recognizable structure
    if "University" in df.columns:
        use_df = df
    else:
        # Try to auto-detect score row
        df.columns = df.columns.str.strip()
        try:
            use_df = df[df['University'].notnull()]
        except:
            print(f"Skipping file due to unexpected structure: {file}")
            continue

    # Loop through universities
    for index, row in use_df.iterrows():
        school = row.get("University", "Unknown School")
        school_sat = row.get("Average SAT score")
        school_act = row.get("Average ACT Score")
        school_gpa = row.get("Average GPA")

        results = []
        if user_sat:
            results.append(f"SAT: {score_match(user_sat, school_sat)}")
        if user_act:
            results.append(f"ACT: {score_match(user_act, school_act)}")
        if user_gpa:
            results.append(f"GPA: {score_match(user_gpa, school_gpa)}")

        print(f"\n{school}")
        for r in results:
            print("  ", r)
