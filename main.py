import pandas as pd
import glob

# Read all CSV files from data folder
files = glob.glob("data/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsel rows
    df = df[df["product"] == "pink morsel"]

    # Create Sales column
    df["sales"] = df["price"] * df["quantity"]

    # Keep only required columns
    df = df[["sales", "date", "region"]]

    all_data.append(df)

# Combine all files
final_df = pd.concat(all_data)

# Save output file
final_df.to_csv("output.csv", index=False)

print("Output file created successfully!")