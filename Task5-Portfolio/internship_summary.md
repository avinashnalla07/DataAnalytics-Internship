# Internship Summary - Data Analytics at ApexPlanet Software Pvt. Ltd.

**Intern:** Avinash Nalla  
**Intern ID:** APSPL2632585  
**Organization:** ApexPlanet Software Pvt. Ltd.  
**Duration:** 21 April 2026 – 19 June 2026  
**Domain:** Data Analytics  

---

## Executive Summary

This document covers everything I worked on during my 60-day Data Analytics internship at ApexPlanet Software Pvt. Ltd. The main project was analyzing the **Superstore Sales Dataset** — a retail dataset with 9,994 transactions over 4 years (2014-2017), covering 793 customers, 3 product categories, and 4 regions across the United States.

The work was split into 5 tasks that built on each other: data cleaning, exploratory analysis, customer segmentation, hypothesis testing, and finally putting it all together into this portfolio.

The biggest takeaway? Discounts are quietly destroying the company's profit. I proved this statistically — discounted orders lose $6.66 on average while full-price orders make $66.90. That's a $73.56 gap per order. On top of that, 10 states are actually losing money, with Texas alone at -$25,729 in losses.

---

## What I Found in Each Task

### Task 1: Data Cleaning & Wrangling

- Started with 21 columns and 9,994 rows. No missing values or duplicates, which was nice.
- Converted Order Date and Ship Date from text to proper datetime format so I could do time-based analysis.
- Created 6 new columns: `Days_to_Ship`, `Profit_Margin_%`, `Order_Year`, `Order_Month`, `Order_Month_Name`, and `Is_Loss`. This brought the total to 27 columns.
- Checked for outliers in Sales using the IQR method. Found some really high-value orders, but they're legit transactions so I kept them.
- Cleaned up text columns (Segment, Region, Category, Ship Mode) to make sure formatting was consistent.
- Built a data dictionary in Excel documenting every column — what it is, what type it is, and why it matters.

### Task 2: EDA & Business Intelligence

- **Technology** is the top category at $836,154 in sales (36.4% of total). Furniture is second at $741,999, and Office Supplies is third at $719,047.
- **Monthly sales** have a clear pattern — Q4 is always the biggest quarter. Peak month was November 2017 at $118,447. Slowest was February 2014 at $4,519.
- **Profit by region** shows a big gap: West ($108,418) is way ahead, followed by East ($91,522), South ($46,749), and Central ($39,706).
- **Discounts and profit** have a clear negative relationship — the more you discount, the more money you lose.
- **10 states** are operating at a loss. Texas is the worst at -$25,729, then Ohio (-$16,971) and Pennsylvania (-$15,559).
- Wrote 7 SQL queries to answer key business questions and verified the numbers match the Python analysis.
- Created 6 charts: category bar chart, monthly trend line, regional profit bar, discount-profit scatter, sub-category horizontal bar, and correlation heatmap.

### Task 3: Customer Segmentation & Dashboarding

- Defined 5 KPIs: Total Revenue ($2,297,201), Profit Margin (12.47%), Average Order Value ($458.61), Customer Retention Rate (~79.3%), and Loss Order Rate (~18.4%).
- Segmented customers into three groups:
  - **High Value** (Sales > $5,000): 117 customers (14.8%) — these are the key accounts
  - **Mid Value** ($1,000 to $5,000): 509 customers (64.2%) — the bulk of the customer base
  - **Low Value** (< $1,000): 167 customers (21.1%) — these need attention
- Looked at how each segment grew over the years. All three segments went up from 2014 to 2017. Customer base grew 10.5% while revenue per customer jumped 37%.

### Task 4: Hypothesis Testing & Statistical Validation

- **Test 1 (T-test): Do discounts hurt profit?**
  - Answer: Yes, they definitely do. REJECT the null hypothesis (T = 15.74, p is basically 0).
  - Discounted orders lose $6.66 on average. Non-discounted orders make $66.90. That's a $73.56 gap.

- **Test 2 (ANOVA): Is there a sales difference between regions?**
  - Answer: Surprisingly, no. FAIL TO REJECT the null hypothesis (F = 0.80, p = 0.49).
  - Even though total profit varies hugely between regions, the average sales per order is roughly the same everywhere. The profit gap comes from discount patterns and order frequency, not from the size of individual orders.

- This was actually a really interesting finding because it changes the strategy. Instead of trying to sell bigger orders in weak regions, the focus should be on controlling discounts and getting more orders.

### Task 5: Portfolio & Documentation

- Created this summary document and the GitHub README.
- Organized everything into proper folders so it's easy to navigate.
- Made sure all files are named consistently and all the numbers check out.

---

## Skills I Used

| Skill | How I Used It |
|-------|--------------|
| **Data Cleaning** | Handled dates, types, outliers, and text standardization with Pandas |
| **EDA** | Descriptive stats, distributions, correlations, trend spotting |
| **Visualization** | Bar charts, line charts, scatter plots, heatmaps with Matplotlib & Seaborn |
| **SQL** | Wrote queries for aggregation, grouping, filtering, and having clauses |
| **Statistics** | T-test for comparing two groups, ANOVA for comparing four groups |
| **Customer Segmentation** | Value-based grouping and cohort tracking |
| **KPI Design** | Defined metrics with formulas and business context |
| **Presenting Data** | Built PowerPoint decks with consistent dark theme |
| **Documentation** | Data dictionary, README, and this summary |

---

## Business Recommendations

Based on everything I analyzed, here's what I'd recommend:

### 1. Fix the Discount Problem (Most Important)

The T-test proved it — discounts are costing the business real money. Every discounted order loses about $6.66 instead of making $66.90. Here's what to do:
- Set a hard cap at 20% discount
- Any discount above 15% needs manager approval
- Track discount-to-profit ratio weekly
- Try product bundles instead of flat discounts

### 2. Deal with the Loss-Making States

10 states are bleeding money. Texas alone is losing $25,729. Steps to take:
- Audit what's going on in Texas, Ohio, and Pennsylvania specifically
- Compare the product mix in these states vs profitable ones
- Consider pulling back on discounts in states that are chronically losing money
- Check if shipping costs are eating into margins

### 3. Protect the High Value Customers

117 customers (just 14.8%) are driving a huge chunk of the revenue. Losing even a few of these would be painful.
- Assign dedicated account managers to the top 50
- Set up alerts if any high-value customer's purchase frequency drops
- Give them perks like priority shipping — but avoid blanket discounts

### 4. Grow the Low Value Segment

167 customers are spending under $1,000 total. There's room to move them up.
- Recommend related products based on what they've bought before
- Create starter bundles to increase order size
- Send targeted follow-up emails after purchases

### 5. Build a Real-Time Dashboard

Right now, all this analysis was done after the fact. A live dashboard would let the team:
- See loss order rates by region and category daily
- Monitor discount levels weekly
- Track customer movement between segments monthly
- Catch problems early before they become expensive

---

## Conclusion

This internship taught me that data analysis isn't just about making charts and running numbers. The real value comes from connecting what the data says to what the business should actually do about it.

The biggest finding was about discounts — they're statistically proven to destroy profit, and that's not something you'd catch just by looking at a spreadsheet. You need proper hypothesis testing to separate real patterns from noise.

The ANOVA result was equally eye-opening. I expected regions to have different sales patterns, but they don't — the profit gap is about discount behavior, not about how much people buy per order. That completely changes what the fix should look like.

If the business acts on the discount recommendation alone, it could realistically recover over $100,000 in annual profits. That's a meaningful impact from a data analysis project.

---

*Completed during the Data Analytics Virtual Internship at ApexPlanet Software Pvt. Ltd.*  
*Intern: Avinash Nalla | ID: APSPL2632585*
