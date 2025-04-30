import pandas as pd
import os

def parse_range(value):
    """Converts a range string like '1470-1560' to its midpoint."""
    if isinstance(value, str) and '-' in value:
        parts = value.split('-')
        return (int(parts[0]) + int(parts[1])) / 2
    try:
        return float(value)
    except:
        return None

def load_ivy_data(filepath):
    df = pd.read_excel(filepath)
    df.columns = df.columns.str.strip()
    df = df.rename(columns={
        "Average SAT score": "SAT",
        "Average ACT Score": "ACT",
        "Average GPA": "GPA"
    })
    df["SAT"] = df["SAT"].apply(parse_range)
    df["ACT"] = df["ACT"].apply(parse_range)
    df["GPA"] = df["GPA"].apply(parse_range)
    df = df.dropna(subset=["SAT", "ACT", "GPA"], how="all")
    return df

def evaluate(score, average):
    if score is None:
        return "N/A"
    if score >= average + 50:
        return "Likely"
    elif score >= average - 50:
        return "Competitive"
    else:
        return "Reach"

def main():
    # Get user input
    sat_input = input("Enter your SAT score (or leave blank): ").strip()
    act_input = input("Enter your ACT score (or leave blank): ").strip()
    gpa_input = input("Enter your GPA (or leave blank): ").strip()

    sat = int(sat_input) if sat_input else None
    act = int(act_input) if act_input else None
    gpa = float(gpa_input) if gpa_input else None

    # Load Ivy League data
    ivy_file = os.path.join("data", "Ivy League Averages.xlsx")
    df = load_ivy_data(ivy_file)

    print("\n===== Ivy League Admission Predictions =====")
    for _, row in df.iterrows():
        print(f"\n{row['University']}")
        print(f"   SAT: {evaluate(sat, row['SAT'])}")
        print(f"   ACT: {evaluate(act, row['ACT'])}")
        print(f"   GPA: {evaluate(gpa, row['GPA'])}")

if __name__ == "__main__":
    main()
