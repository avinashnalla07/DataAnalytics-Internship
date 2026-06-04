import pandas as pd
import numpy as np
from scipy import stats
import os
import warnings
warnings.filterwarnings('ignore')

# --- Setup ---
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Task1-Data-Wrangling', 'superstore_cleaned.csv')

# --- Load the Data ---
print("=" * 60)
print("TASK 4 - DATA STORYTELLING & STATISTICAL VALIDATION")
print("=" * 60)

df = pd.read_csv(DATA_FILE)
print(f"\nDataset loaded: {df.shape[0]} rows x {df.shape[1]} columns")

# =================================================================
# HYPOTHESIS TEST 1: Do Discounts Lead to Lower Profit?
# =================================================================
print("\n" + "=" * 60)
print("HYPOTHESIS TEST 1: DO DISCOUNTS LEAD TO LOWER PROFIT?")
print("=" * 60)

print("\nTest Setup:")
print("  Method         : Independent Samples T-test")
print("  Significance   : alpha = 0.05")
print("  Null Hypothesis: There's no real difference in profit between")
print("                   discounted and non-discounted orders.")
print("  Alternative    : Discounted orders have significantly lower profit.")

# Split the data into two groups
discounted = df[df['Discount'] > 0]['Profit']
non_discounted = df[df['Discount'] == 0]['Profit']

print(f"\nSample Sizes:")
print(f"  Discounted orders     : {len(discounted):,}")
print(f"  Non-discounted orders : {len(non_discounted):,}")

# Calculate the averages
avg_profit_disc = discounted.mean()
avg_profit_no_disc = non_discounted.mean()
std_disc = discounted.std()
std_no_disc = non_discounted.std()

print(f"\nDescriptive Statistics:")
print(f"  Avg Profit WITH discount    : ${avg_profit_disc:,.2f}")
print(f"  Avg Profit WITHOUT discount : ${avg_profit_no_disc:,.2f}")
print(f"  Std Dev WITH discount       : ${std_disc:,.2f}")
print(f"  Std Dev WITHOUT discount    : ${std_no_disc:,.2f}")
print(f"  Profit Difference           : ${avg_profit_no_disc - avg_profit_disc:,.2f}")

# Run the T-test
t_statistic, p_value = stats.ttest_ind(non_discounted, discounted, equal_var=False)

print(f"\nT-test Results:")
print(f"  T-statistic : {t_statistic:.4f}")
print(f"  P-value     : {p_value:.6f}")
print(f"  P-value     : {p_value:.2e} (scientific notation)")

print(f"\nDecision (alpha = 0.05):")
if p_value < 0.05:
    print(f"  REJECT the Null Hypothesis (p = {p_value:.6f} < 0.05)")
    print(f"\nBusiness Conclusion:")
    print(f"  Yes, discounts DO significantly hurt profits. The numbers show it")
    print(f"  clearly - discounted orders average ${avg_profit_disc:,.2f} in profit")
    print(f"  while non-discounted orders average ${avg_profit_no_disc:,.2f}.")
    print(f"  That's a ${avg_profit_no_disc - avg_profit_disc:,.2f} gap per order.")
    print(f"\nWhat to do about it:")
    print(f"  - Cap discounts at 20% max")
    print(f"  - Need manager approval for anything above 15%")
    print(f"  - Try bundling products instead of straight discounts")
else:
    print(f"  FAIL TO REJECT the Null Hypothesis (p = {p_value:.6f} >= 0.05)")
    print(f"  No significant difference found.")

# =================================================================
# HYPOTHESIS TEST 2: Does Region Affect Sales Performance?
# =================================================================
print("\n\n" + "=" * 60)
print("HYPOTHESIS TEST 2: DOES REGION AFFECT SALES PERFORMANCE?")
print("=" * 60)

print("\nTest Setup:")
print("  Method         : One-Way ANOVA (Analysis of Variance)")
print("  Significance   : alpha = 0.05")
print("  Null Hypothesis: Average sales per order is the same across")
print("                   all four regions (East, West, Central, South).")
print("  Alternative    : At least one region has different average sales.")

# Split data by region
regions = df['Region'].unique()
region_groups = [df[df['Region'] == r]['Sales'] for r in sorted(regions)]
region_names = sorted(regions)

print(f"\nSample Sizes by Region:")
for name, group in zip(region_names, region_groups):
    print(f"  {name:10s}: {len(group):,} orders | Avg Sales: ${group.mean():,.2f} | Total: ${group.sum():,.0f}")

# Run the ANOVA test
f_statistic, p_value_anova = stats.f_oneway(*region_groups)

print(f"\nANOVA Results:")
print(f"  F-statistic : {f_statistic:.4f}")
print(f"  P-value     : {p_value_anova:.6f}")
print(f"  P-value     : {p_value_anova:.2e} (scientific notation)")

print(f"\nDecision (alpha = 0.05):")
if p_value_anova < 0.05:
    print(f"  REJECT the Null Hypothesis (p = {p_value_anova:.6f} < 0.05)")
    print(f"\nBusiness Conclusion:")
    print(f"  Region does significantly affect sales performance.")
    print(f"  Some regions are doing noticeably better than others.")
else:
    print(f"  FAIL TO REJECT the Null Hypothesis (p = {p_value_anova:.6f} >= 0.05)")
    print(f"\nBusiness Conclusion:")
    print(f"  Interestingly, individual order sales are NOT significantly different")
    print(f"  across regions. Even though West makes way more total profit than")
    print(f"  Central, the average sale per order is about the same everywhere.")
    print(f"  This means the profit gap comes from discount patterns and order")
    print(f"  volume, not from how much each order is worth.")
    print(f"\nWhat this means for the business:")
    print(f"  Don't try to increase individual order sizes in weak regions.")
    print(f"  Instead, focus on controlling discounts and getting more orders.")

# --- Final Summary ---
print("\n\n" + "=" * 60)
print("SUMMARY OF STATISTICAL TESTS")
print("=" * 60)
print(f"\n  Test 1: Discount Impact on Profit (T-test)")
print(f"  Result: {'REJECT H0' if p_value < 0.05 else 'FAIL TO REJECT H0'}")
print(f"  T-stat: {t_statistic:.4f} | P-value: {p_value:.6f}")
print(f"  Finding: Discounts cut average profit by ${avg_profit_no_disc - avg_profit_disc:,.2f} per order")
print(f"\n  Test 2: Regional Sales Differences (ANOVA)")
print(f"  Result: {'REJECT H0' if p_value_anova < 0.05 else 'FAIL TO REJECT H0'}")
print(f"  F-stat: {f_statistic:.4f} | P-value: {p_value_anova:.6f}")
print(f"  Finding: Per-order sales are similar across regions; the profit gap is about discounts and volume")

print("\n" + "=" * 60)
print("TASK 4 - HYPOTHESIS TESTING COMPLETE!")
print("=" * 60)
