import pandas as pd
import numpy as np
import os

# File paths
INPUT_FILE = r"C:\Users\Avinash Nalla\Desktop\Apex\Datasets\Superstore.csv"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "superstore_cleaned.csv")

# --- Step 1: Load the Dataset ---
print("=" * 60)
print("TASK 1 - DATA IMMERSION & WRANGLING")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, encoding='latin1')
initial_rows = len(df)
initial_cols = len(df.columns)

print(f"\nDataset Loaded Successfully")
print(f"  Total Rows   : {initial_rows}")
print(f"  Total Columns: {initial_cols}")
print(f"\nColumn Names:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2d}. {col}")

# --- Step 2: Check Missing Values ---
print("\n")
print("MISSING VALUES CHECK")
print("=" * 60)
missing = df.isnull().sum()
total_missing = missing.sum()
if total_missing == 0:
    print("  No missing values found in any column.")
else:
    print(f"  Total missing values: {total_missing}")
    for col in missing[missing > 0].index:
        print(f"  - {col}: {missing[col]} missing values")

# --- Step 3: Check and Remove Duplicates ---
print("\n")
print("DUPLICATE ROWS CHECK")
print("=" * 60)
duplicates_count = df.duplicated().sum()
print(f"  Duplicate rows found: {duplicates_count}")
if duplicates_count > 0:
    df = df.drop_duplicates()
    print(f"  Removed {duplicates_count} duplicate rows.")
    print(f"  Rows after removal: {len(df)}")
else:
    print("  No duplicate rows found.")

# --- Step 4: Convert Date Columns to Datetime ---
print("\n")
print("DATE CONVERSION")
print("=" * 60)
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', dayfirst=False)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed', dayfirst=False)
print(f"  'Order Date' converted to datetime: {df['Order Date'].dtype}")
print(f"  'Ship Date' converted to datetime : {df['Ship Date'].dtype}")
print(f"  Date range: {df['Order Date'].min().strftime('%Y-%m-%d')} to {df['Order Date'].max().strftime('%Y-%m-%d')}")

# --- Step 5: Create New Columns (Feature Engineering) ---
print("\n")
print("FEATURE ENGINEERING - NEW COLUMNS")
print("=" * 60)

# Days_to_Ship: how many days it took from order to shipment
df['Days_to_Ship'] = (df['Ship Date'] - df['Order Date']).dt.days
print(f"  'Days_to_Ship' created (avg: {df['Days_to_Ship'].mean():.1f} days)")

# Profit_Margin_%: what percentage of sales turned into profit
df['Profit_Margin_%'] = np.where(
    df['Sales'] != 0,
    (df['Profit'] / df['Sales']) * 100,
    0
)
df['Profit_Margin_%'] = df['Profit_Margin_%'].round(2)
print(f"  'Profit_Margin_%' created (avg: {df['Profit_Margin_%'].mean():.2f}%)")

# Order_Year: year from Order Date
df['Order_Year'] = df['Order Date'].dt.year
print(f"  'Order_Year' created (range: {df['Order_Year'].min()}-{df['Order_Year'].max()})")

# Order_Month: month number from Order Date
df['Order_Month'] = df['Order Date'].dt.month
print(f"  'Order_Month' created (1-12)")

# Order_Month_Name: month name from Order Date
df['Order_Month_Name'] = df['Order Date'].dt.strftime('%B')
print(f"  'Order_Month_Name' created (e.g., {df['Order_Month_Name'].iloc[0]})")

# Is_Loss: flag for orders that lost money
df['Is_Loss'] = df['Profit'] < 0
loss_count = df['Is_Loss'].sum()
print(f"  'Is_Loss' created ({loss_count} loss-making orders, {loss_count/len(df)*100:.1f}%)")

# --- Step 6: Outlier Detection in Sales (IQR Method) ---
print("\n")
print("OUTLIER DETECTION - SALES COLUMN (IQR METHOD)")
print("=" * 60)
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['Sales'] < lower_bound) | (df['Sales'] > upper_bound)]
print(f"  Q1 (25th percentile) : ${Q1:,.2f}")
print(f"  Q3 (75th percentile) : ${Q3:,.2f}")
print(f"  IQR                  : ${IQR:,.2f}")
print(f"  Lower Bound          : ${lower_bound:,.2f}")
print(f"  Upper Bound          : ${upper_bound:,.2f}")
print(f"  Outliers detected    : {len(outliers)} rows ({len(outliers)/len(df)*100:.1f}%)")
print(f"  Note: Outliers kept in the data since they are valid high-value sales")

# --- Step 7: Standardize Text Columns ---
print("\n")
print("TEXT STANDARDIZATION")
print("=" * 60)
text_cols = ['Segment', 'Region', 'Category', 'Ship Mode']
for col in text_cols:
    df[col] = df[col].str.strip().str.title()
    unique_vals = df[col].unique()
    print(f"  '{col}' standardized -> {list(unique_vals)}")

# --- Step 8: Save the Cleaned Dataset ---
print("\n")
print("SAVING CLEANED DATASET")
print("=" * 60)
df.to_csv(OUTPUT_FILE, index=False)
print(f"  Saved to: {OUTPUT_FILE}")

# --- Step 9: Final Summary ---
print("\n")
print("FINAL SUMMARY OF ALL CHANGES")
print("=" * 60)
print(f"  Original rows          : {initial_rows}")
print(f"  Original columns       : {initial_cols}")
print(f"  Duplicates removed     : {duplicates_count}")
print(f"  Final rows             : {len(df)}")
print(f"  Final columns          : {len(df.columns)}")
print(f"  New columns added      : {len(df.columns) - initial_cols}")
print(f"  New columns list       : Days_to_Ship, Profit_Margin_%, Order_Year,")
print(f"                           Order_Month, Order_Month_Name, Is_Loss")
print(f"  Date columns converted : Order Date, Ship Date")
print(f"  Text columns cleaned   : {', '.join(text_cols)}")
print(f"  Outliers in Sales      : {len(outliers)} (kept as valid data)")
print(f"  Missing values         : {total_missing}")
print(f"  Output file            : superstore_cleaned.csv")

