import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Task1-Data-Wrangling', 'superstore_cleaned.csv')
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

NAVY = '#0A1628'
TEAL = '#0D9488'
AMBER = '#F59E0B'
RED = '#EF4444'

plt.rcParams.update({
    'figure.facecolor': NAVY,
    'axes.facecolor': '#0F1D32',
    'axes.edgecolor': '#1E3A5F',
    'axes.labelcolor': 'white',
    'text.color': 'white',
    'xtick.color': '#94A3B8',
    'ytick.color': '#94A3B8',
    'grid.color': '#1E3A5F',
    'grid.alpha': 0.3,
    'font.family': 'sans-serif',
    'font.size': 11,
})

# --- Load the Data ---
print("=" * 60)
print("TASK 3 - CUSTOMER SEGMENTATION ANALYSIS")
print("=" * 60)

df = pd.read_csv(DATA_FILE)
df['Order Date'] = pd.to_datetime(df['Order Date'])
print(f"\nDataset loaded: {df.shape[0]} rows x {df.shape[1]} columns")

# --- Group by Customer ---
print("\n" + "=" * 60)
print("CUSTOMER AGGREGATION")
print("=" * 60)

customer_agg = df.groupby('Customer ID').agg(
    Customer_Name=('Customer Name', 'first'),
    Total_Orders=('Order ID', 'nunique'),
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Avg_Order_Value=('Sales', 'mean')
).reset_index()

# Recalculate average order value properly (total sales / number of orders)
customer_agg['Avg_Order_Value'] = (customer_agg['Total_Sales'] / customer_agg['Total_Orders']).round(2)
customer_agg['Total_Sales'] = customer_agg['Total_Sales'].round(2)
customer_agg['Total_Profit'] = customer_agg['Total_Profit'].round(2)

print(f"  Total unique customers: {len(customer_agg)}")
print(f"  Average orders per customer: {customer_agg['Total_Orders'].mean():.1f}")
print(f"  Average total sales per customer: ${customer_agg['Total_Sales'].mean():,.2f}")

# --- Segment Customers by Value ---
print("\n" + "=" * 60)
print("CUSTOMER SEGMENTATION")
print("=" * 60)

def segment_customer(total_sales):
    if total_sales > 5000:
        return 'High Value'
    elif total_sales >= 1000:
        return 'Mid Value'
    else:
        return 'Low Value'

customer_agg['Segment_Value'] = customer_agg['Total_Sales'].apply(segment_customer)

segment_counts = customer_agg['Segment_Value'].value_counts()
print("\n  Customer Value Segments:")
for seg in ['High Value', 'Mid Value', 'Low Value']:
    count = segment_counts.get(seg, 0)
    pct = count / len(customer_agg) * 100
    avg_sales = customer_agg[customer_agg['Segment_Value'] == seg]['Total_Sales'].mean()
    print(f"  - {seg:12s}: {count:4d} customers ({pct:5.1f}%) | Avg Sales: ${avg_sales:,.2f}")

# --- Chart 1: Customer Segment Bar Chart ---
print("\nCreating Chart: Customer Segment Counts...")
fig, ax = plt.subplots(figsize=(10, 6))
colors = [TEAL, AMBER, RED]
segment_order = ['High Value', 'Mid Value', 'Low Value']
counts = [segment_counts.get(s, 0) for s in segment_order]

bars = ax.bar(segment_order, counts, color=colors, width=0.6, edgecolor='none', zorder=3)
for bar, val in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
            f'{val}', ha='center', va='bottom', fontsize=16,
            fontweight='bold', color='white')
    pct = val / len(customer_agg) * 100
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
            f'{pct:.1f}%', ha='center', va='center', fontsize=13,
            color='white', alpha=0.8)

ax.set_title('Customer Segmentation by Value', fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('Number of Customers', fontsize=13)
ax.grid(axis='y', alpha=0.2)
ax.set_axisbelow(True)

# Legend at bottom
legend_text = "High Value: Sales > $5,000  |  Mid Value: $1,000-$5,000  |  Low Value: < $1,000"
ax.text(0.5, -0.12, legend_text, transform=ax.transAxes, ha='center',
        fontsize=10, color='#94A3B8')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'task3_customer_segments.png'), dpi=150, bbox_inches='tight')
plt.close()

# --- Chart 2: Yearly Sales by Segment (Line Chart) ---
print("Creating Chart: Yearly Sales by Segment...")
df['Order_Year'] = pd.to_datetime(df['Order Date']).dt.year

# Add segment info to main dataframe
customer_segments = customer_agg[['Customer ID', 'Segment_Value']]
df_with_seg = df.merge(customer_segments, on='Customer ID', how='left')

yearly_seg_sales = df_with_seg.groupby(['Order_Year', 'Segment_Value'])['Sales'].sum().reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
seg_colors = {'High Value': TEAL, 'Mid Value': AMBER, 'Low Value': RED}

for seg in segment_order:
    seg_data = yearly_seg_sales[yearly_seg_sales['Segment_Value'] == seg]
    ax.plot(seg_data['Order_Year'], seg_data['Sales'], marker='o', linewidth=2.5,
            markersize=8, color=seg_colors[seg], label=seg, zorder=3)
    # Show the dollar values on each point
    for _, row in seg_data.iterrows():
        ax.annotate(f"${row['Sales']:,.0f}",
                    xy=(row['Order_Year'], row['Sales']),
                    xytext=(0, 12), textcoords='offset points',
                    ha='center', fontsize=9, color=seg_colors[seg], fontweight='bold')

ax.set_title('Yearly Sales Trend by Customer Segment', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Total Sales ($)', fontsize=13)
ax.set_xticks([2014, 2015, 2016, 2017])
ax.legend(loc='upper left', framealpha=0.1, edgecolor='none', fontsize=12)
ax.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'task3_yearly_segment_sales.png'), dpi=150, bbox_inches='tight')
plt.close()

# --- Final Summary ---
print("\n" + "=" * 60)
print("FINAL SUMMARY - CUSTOMER SEGMENTATION")
print("=" * 60)
for seg in ['High Value', 'Mid Value', 'Low Value']:
    count = segment_counts.get(seg, 0)
    total_sales = customer_agg[customer_agg['Segment_Value'] == seg]['Total_Sales'].sum()
    total_profit = customer_agg[customer_agg['Segment_Value'] == seg]['Total_Profit'].sum()
    print(f"\n  {seg}:")
    print(f"    Customers   : {count}")
    print(f"    Total Sales : ${total_sales:,.2f}")
    print(f"    Total Profit: ${total_profit:,.2f}")
    print(f"    Avg AOV     : ${customer_agg[customer_agg['Segment_Value'] == seg]['Avg_Order_Value'].mean():,.2f}")

print("\n" + "=" * 60)

# Show Top 10 High Value Customers
print("\nTOP 10 HIGH VALUE CUSTOMERS:")
print("-" * 60)
top10 = customer_agg[customer_agg['Segment_Value'] == 'High Value'].nlargest(10, 'Total_Sales')
for i, (_, row) in enumerate(top10.iterrows(), 1):
    print(f"  {i:2d}. {row['Customer_Name']:<30s} | Sales: ${row['Total_Sales']:>10,.2f} | "
          f"Profit: ${row['Total_Profit']:>9,.2f} | Orders: {row['Total_Orders']}")

print("\n" + "=" * 60)
print("TASK 3 - CUSTOMER SEGMENTATION COMPLETE!")
print("=" * 60)
