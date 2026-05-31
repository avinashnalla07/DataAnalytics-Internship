import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# --- Setup ---
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Task1-Data-Wrangling', 'superstore_cleaned.csv')
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Color scheme
NAVY = '#0A1628'
TEAL = '#0D9488'
COLORS = ['#0D9488', '#14B8A6', '#2DD4BF', '#5EEAD4', '#99F6E4', '#CCFBF1']
CHART_COLORS = ['#0D9488', '#F59E0B', '#EF4444', '#8B5CF6']

# Chart styling - dark theme to match the presentations
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
print("TASK 2 - EXPLORATORY DATA ANALYSIS & BUSINESS INTELLIGENCE")
print("=" * 60)

df = pd.read_csv(DATA_FILE)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
print(f"\nDataset loaded: {df.shape[0]} rows x {df.shape[1]} columns")

# --- Descriptive Statistics ---
print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)
stats_cols = ['Sales', 'Profit', 'Quantity', 'Discount']
desc_stats = df[stats_cols].describe()
print(desc_stats.to_string())

# --- Chart 1: Sales by Category (Bar Chart) ---
print("\nCreating Chart 1: Sales by Category...")
fig, ax = plt.subplots(figsize=(10, 6))
cat_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
bars = ax.bar(cat_sales.index, cat_sales.values, color=CHART_COLORS[:3],
              width=0.6, edgecolor='none', zorder=3)
for bar, val in zip(bars, cat_sales.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5000,
            f'${val:,.0f}', ha='center', va='bottom', fontsize=13,
            fontweight='bold', color='white')
ax.set_title('Total Sales by Category', fontsize=18, fontweight='bold', pad=20, color='white')
ax.set_ylabel('Total Sales ($)', fontsize=13)
ax.set_xlabel('')
ax.grid(axis='y', alpha=0.2)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'chart1_sales_by_category.png'), dpi=150, bbox_inches='tight')
plt.close()

# --- Chart 2: Monthly Sales Trend (Line Chart) ---
print("Creating Chart 2: Monthly Sales Trend...")
fig, ax = plt.subplots(figsize=(14, 6))
df['YearMonth'] = df['Order Date'].dt.to_period('M')
monthly = df.groupby('YearMonth')['Sales'].sum().reset_index()
monthly['YearMonth'] = monthly['YearMonth'].astype(str)
ax.plot(range(len(monthly)), monthly['Sales'].values, color=TEAL, linewidth=2.5, zorder=3)
ax.fill_between(range(len(monthly)), monthly['Sales'].values, alpha=0.15, color=TEAL)

# Mark the peak and lowest points
peak_idx = monthly['Sales'].idxmax()
low_idx = monthly['Sales'].idxmin()
ax.scatter([peak_idx], [monthly['Sales'].iloc[peak_idx]], color='#F59E0B', s=100, zorder=5)
ax.annotate(f"Peak: ${monthly['Sales'].iloc[peak_idx]:,.0f}\n{monthly['YearMonth'].iloc[peak_idx]}",
            xy=(peak_idx, monthly['Sales'].iloc[peak_idx]),
            xytext=(peak_idx-5, monthly['Sales'].iloc[peak_idx]+10000),
            fontsize=9, color='#F59E0B', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#F59E0B'))
ax.scatter([low_idx], [monthly['Sales'].iloc[low_idx]], color='#EF4444', s=100, zorder=5)
ax.set_title('Monthly Sales Trend (2014-2017)', fontsize=18, fontweight='bold', pad=20)
tick_positions = range(0, len(monthly), 6)
tick_labels = [monthly['YearMonth'].iloc[i] for i in tick_positions]
ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels, rotation=45, ha='right')
ax.set_ylabel('Total Sales ($)', fontsize=13)
ax.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'chart2_monthly_sales.png'), dpi=150, bbox_inches='tight')
plt.close()

# --- Chart 3: Profit by Region (Bar Chart) ---
print("Creating Chart 3: Profit by Region...")
fig, ax = plt.subplots(figsize=(10, 6))
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
bars = ax.bar(region_profit.index, region_profit.values, color=CHART_COLORS[:4],
              width=0.6, edgecolor='none', zorder=3)
for bar, val in zip(bars, region_profit.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2000,
            f'${val:,.0f}', ha='center', va='bottom', fontsize=13,
            fontweight='bold', color='white')
ax.set_title('Total Profit by Region', fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('Total Profit ($)', fontsize=13)
ax.grid(axis='y', alpha=0.2)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'chart3_profit_by_region.png'), dpi=150, bbox_inches='tight')
plt.close()

# --- Chart 4: Discount vs Profit (Scatter Plot) ---
print("Creating Chart 4: Discount vs Profit...")
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(df['Discount'], df['Profit'], c=df['Profit'],
                     cmap='RdYlGn', alpha=0.5, s=15, edgecolors='none')
ax.axhline(y=0, color='#EF4444', linestyle='--', alpha=0.7, linewidth=1)
cbar = plt.colorbar(scatter, ax=ax, pad=0.02)
cbar.set_label('Profit ($)', color='white')
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')
ax.set_title('Discount vs Profit Relationship', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Discount', fontsize=13)
ax.set_ylabel('Profit ($)', fontsize=13)
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'chart4_discount_vs_profit.png'), dpi=150, bbox_inches='tight')
plt.close()

# --- Chart 5: Top 10 Sub-Categories (Horizontal Bar) ---
print("Creating Chart 5: Top 10 Sub-Categories...")
fig, ax = plt.subplots(figsize=(12, 7))
subcat_sales = df.groupby('Sub-Category')['Sales'].sum().nlargest(10).sort_values()
bars = ax.barh(subcat_sales.index, subcat_sales.values,
               color=[TEAL if i >= 7 else '#14B8A6' if i >= 4 else '#2DD4BF' for i in range(len(subcat_sales))],
               height=0.65, edgecolor='none', zorder=3)
for bar, val in zip(bars, subcat_sales.values):
    ax.text(bar.get_width() + 2000, bar.get_y() + bar.get_height()/2,
            f'${val:,.0f}', ha='left', va='center', fontsize=11,
            fontweight='bold', color='white')
ax.set_title('Top 10 Sub-Categories by Sales', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Total Sales ($)', fontsize=13)
ax.grid(axis='x', alpha=0.2)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'chart5_subcategory_sales.png'), dpi=150, bbox_inches='tight')
plt.close()

# --- Chart 6: Correlation Heatmap ---
print("Creating Chart 6: Correlation Heatmap...")
fig, ax = plt.subplots(figsize=(10, 8))
numeric_cols = ['Sales', 'Quantity', 'Discount', 'Profit', 'Days_to_Ship', 'Profit_Margin_%']
corr = df[numeric_cols].corr()
mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='YlGnBu',
            center=0, square=True, linewidths=1, linecolor='#0A1628',
            cbar_kws={'shrink': 0.8, 'label': 'Correlation'},
            ax=ax, annot_kws={'size': 12, 'fontweight': 'bold'})
ax.set_title('Correlation Heatmap', fontsize=18, fontweight='bold', pad=20)
ax.tick_params(axis='x', rotation=45)
ax.tick_params(axis='y', rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'chart6_correlation_heatmap.png'), dpi=150, bbox_inches='tight')
plt.close()

# --- 5 Key Business Insights ---
print("\n" + "=" * 60)
print("5 KEY BUSINESS INSIGHTS")
print("=" * 60)

# Insight 1: Technology is the top revenue category
tech_sales = df[df['Category'] == 'Technology']['Sales'].sum()
total_sales = df['Sales'].sum()
print(f"\n1. TECHNOLOGY IS THE TOP REVENUE CATEGORY")
print(f"   Technology brings in ${tech_sales:,.0f} which is {tech_sales/total_sales*100:.1f}% of total sales.")
print(f"   It earns the most while having the lowest discount rate.")

# Insight 2: A lot of orders are losing money
loss_pct = (df['Is_Loss'].sum() / len(df)) * 100
avg_loss = df[df['Is_Loss'] == True]['Profit'].mean()
print(f"\n2. TOO MANY ORDERS ARE LOSING MONEY")
print(f"   {df['Is_Loss'].sum()} orders ({loss_pct:.1f}%) end up as losses.")
print(f"   The average loss per bad order is ${avg_loss:,.2f}.")

# Insight 3: Discounts are hurting profits badly
disc_profit = df[df['Discount'] > 0]['Profit'].mean()
no_disc_profit = df[df['Discount'] == 0]['Profit'].mean()
print(f"\n3. DISCOUNTS ARE EATING INTO PROFITS")
print(f"   Average profit with discount: ${disc_profit:,.2f}")
print(f"   Average profit without discount: ${no_disc_profit:,.2f}")
print(f"   That's a ${no_disc_profit - disc_profit:,.2f} difference per order.")

# Insight 4: West region is way ahead in profitability
west_profit = df[df['Region'] == 'West']['Profit'].sum()
central_profit = df[df['Region'] == 'Central']['Profit'].sum()
print(f"\n4. WEST REGION LEADS IN PROFIT BY A BIG MARGIN")
print(f"   West region profit: ${west_profit:,.0f}")
print(f"   Central region profit: ${central_profit:,.0f}")
print(f"   West makes ${west_profit - central_profit:,.0f} more than Central.")

# Insight 5: Sales are growing year over year
yearly_sales = df.groupby('Order_Year')['Sales'].sum()
growth = ((yearly_sales.iloc[-1] - yearly_sales.iloc[0]) / yearly_sales.iloc[0]) * 100
print(f"\n5. SALES HAVE BEEN GROWING EVERY YEAR")
print(f"   2014: ${yearly_sales.iloc[0]:,.0f}")
print(f"   2017: ${yearly_sales.iloc[-1]:,.0f}")
print(f"   That's {growth:.1f}% growth over 4 years.")

print("\n" + "=" * 60)
print("TASK 2 - EDA COMPLETE! All 6 charts saved.")
print("=" * 60)

# Clean up temp column
df.drop(columns=['YearMonth'], inplace=True, errors='ignore')
