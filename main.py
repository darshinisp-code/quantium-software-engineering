import pandas as pd

df = pd.read_csv("daily_sales_data_0.csv")

df = df[df["product"] == "pink morsel"]

df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)

df["sales"] = df["price"] * df["quantity"]

final_df = df[["sales", "date", "region"]]

final_df.to_csv("output.csv", index=False)

print("Output file created successfully!")