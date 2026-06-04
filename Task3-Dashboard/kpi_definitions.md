# KPI Definitions - Deep-Dive Analysis & Interactive Dashboarding

## Intern: Avinash Nalla | ID: APSPL2632585
## Organization: ApexPlanet Software Pvt. Ltd.

---

## KPI 1: Total Revenue

- **Formula:** `SUM(Sales)`
- **What it means:** The total money coming in from all sales transactions.
- **Why it matters:** This is the most basic measure of how the business is doing. If revenue is going up, the business is growing. If it's flat or dropping, something needs to change. We use this as the starting point for almost every other analysis.
- **Current Value:** $2,297,201 (across 9,994 orders from 2014-2017)

---

## KPI 2: Profit Margin %

- **Formula:** `(SUM(Profit) / SUM(Sales)) * 100`
- **What it means:** Out of every dollar in sales, how many cents actually become profit.
- **Why it matters:** Revenue is great, but if most of it goes to costs and discounts, the business isn't really making money. A profit margin of 12% means only $0.12 out of every $1 is actual profit. If this number drops, it usually means discounts are too high or costs are going up.
- **Current Value:** 12.47% ($286,397 profit on $2,297,201 revenue)

---

## KPI 3: Average Order Value (AOV)

- **Formula:** `SUM(Sales) / COUNT(DISTINCT Order ID)`
- **What it means:** How much revenue each order brings in on average.
- **Why it matters:** Higher AOV means customers are buying more per order, which is more efficient for the business. You can boost AOV through product bundling, cross-selling, or minimum order thresholds. Tracking this by customer segment helps find where the biggest opportunities are.
- **Current Value:** $458.61 (5,009 unique orders)

---

## KPI 4: Customer Retention Rate

- **Formula:** `(Returning Customers / Total Customers) * 100`
- **What it means:** What percentage of customers come back and buy again.
- **Why it matters:** Getting a new customer costs way more than keeping an existing one (some studies say 5-25x more). A retention rate around 79% means most customers do come back, which is a good sign. But the 21% who don't return represent lost potential revenue that could be recovered with better follow-up.
- **Current Value:** ~79.3% (roughly 629 out of 793 customers are repeat buyers)

---

## KPI 5: Loss Order Rate

- **Formula:** `(Orders where Profit < 0 / Total Orders) * 100`
- **What it means:** What percentage of orders actually lose money for the business.
- **Why it matters:** Almost 1 in 5 orders is a loss. That's a lot. These are orders where the discount or cost was so high that the business actually lost money on the sale. Finding out which products, regions, and discount levels cause the most losses helps fix the problem at its root.
- **Current Value:** ~18.4% (about 1,838 out of 9,994 orders lose money)

---

*All values calculated from the Superstore Sales dataset (2014-2017, 9,994 transactions).*
