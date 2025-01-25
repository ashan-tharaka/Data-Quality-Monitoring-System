import pandas as pd

df=pd.read_csv('sales_data.csv')

print(df.head())

missing_values=df.isnull().sum()

print("Missing Values per Column:")
print(missing_values)

duplicates=df[df.duplicated()]

print("Duplicate Entries:")
print(duplicates)

# Validate quantity_sold
invalid_quantity = df[df["quantity_sold"] < 0]

# Validate total_revenue
invalid_revenue = df[df["total_revenue"] <= 0]

print("Invalid Quantities Sold:")
print(invalid_quantity)

print("Invalid Total Revenue:")
print(invalid_revenue)

from datetime import datetime

# Define date range
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Convert sale_date to datetime and validate
df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")
invalid_dates = df[(df["sale_date"] < start_date) | (df["sale_date"] > end_date)]

print("Invalid Dates:")
print(invalid_dates)


# Summary report
report = {
    "Metric": [
        "Total Records",
        "Missing Values",
        "Duplicate Entries",
        "Invalid Quantities Sold",
        "Invalid Total Revenue",
        "Invalid Dates"
    ],
    "Value": [
        len(df),
        missing_values.to_dict(),
        len(duplicates),
        len(invalid_quantity),
        len(invalid_revenue),
        len(invalid_dates)
    ]
}

report_df = pd.DataFrame(report)

# Display the report DataFrame
print("\nData Quality Report as DataFrame:")
print(report_df)


import matplotlib.pyplot as plt

# Visualize missing values
missing_values.plot(kind="bar", title="Missing Values per Column")
plt.show()
