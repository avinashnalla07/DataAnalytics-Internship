-Data Analytics Internship Portfolio

A 60-day virtual internship project in Data Analytics.

---

## Intern Details

| Field | Details |
|-------|---------|
| Name | Avinash Nalla |
| Intern ID | APSPL2632585 |
| Organization | ApexPlanet Software Pvt. Ltd. |
| Duration | 21 April 2026 – 19 June 2026 |
| Domain | Data Analytics |

---

## What This Project Is About

This portfolio covers everything I did during my 60-day internship at ApexPlanet Software Pvt. Ltd. I worked with the **Superstore Sales Dataset** (9,994 orders, 27 columns, spanning 2014-2017) and went through the full data analytics process — from cleaning the raw data all the way to statistical testing and presenting findings.

---

## Task Summary

| # | Task Name | What I Did | Key Files |
|---|-----------|-----------|-----------|
| 1 | Data Wrangling | Cleaned the dataset, fixed dates, added new columns, checked for outliers | `task1_cleaning.py`, `data_dictionary.xlsx`, `superstore_cleaned.csv` |
| 2 | EDA & Business Intelligence | Built 6 charts, wrote SQL queries, found key patterns in the data | `task2_eda.py`, `task2_sql_queries.sql`, `sql_results.txt`, `task2_dashboard_mockup.pptx` |
| 3 | Deep-Dive Analysis | Segmented customers by value, defined KPIs, tracked trends over years | `task3_segmentation.py`, `kpi_definitions.md`, `task3_dashboard_presentation.pptx` |
| 4 | Statistical Validation | Ran T-test and ANOVA to back up findings with real statistics | `task4_hypothesis_testing.py`, `task4_presentation.pptx` |
| 5 | Portfolio | Put everything together into a presentable format | `README.md`, `internship_summary.md` |

---

## Folder Structure

```
AvinashNalla-DataAnalyst-Internship-Portfolio/
├── Task1-Data-Wrangling/
│   ├── task1_cleaning.py
│   ├── create_data_dictionary.py
│   ├── data_dictionary.xlsx
│   └── superstore_cleaned.csv
├── Task2-EDA/
│   ├── task2_eda.py
│   ├── task2_sql_queries.sql
│   ├── sql_results.txt
│   ├── task2_dashboard_mockup.pptx
│   ├── create_task2_pptx.py
│   ├── chart1_sales_by_category.png
│   ├── chart2_monthly_sales.png
│   ├── chart3_profit_by_region.png
│   ├── chart4_discount_vs_profit.png
│   ├── chart5_subcategory_sales.png
│   └── chart6_correlation_heatmap.png
├── Task3-Dashboard/
│   ├── task3_segmentation.py
│   ├── kpi_definitions.md
│   ├── task3_dashboard_presentation.pptx
│   ├── create_task3_pptx.py
│   ├── task3_customer_segments.png
│   └── task3_yearly_segment_sales.png
├── Task4-Storytelling/
│   ├── task4_hypothesis_testing.py
│   ├── task4_presentation.pptx
│   └── create_task4_pptx.py
└── Task5-Portfolio/
    ├── README.md
    └── internship_summary.md
```

## Tools & Technologies

| Category | Tools |
|----------|-------|
| Programming | Python 3.x |
| Data Work | Pandas, NumPy |
| Charts | Matplotlib, Seaborn |
| Statistics | SciPy (T-test, ANOVA) |
| Database | SQL |
| Presentations | PowerPoint, python-pptx |
| Spreadsheets | Excel, openpyxl |
| Dashboarding | Looker Studio |
| Version Control | GitHub |

---

## What I Learned

1. **Data cleaning takes time but it's worth it.** Before I could analyze anything, I had to clean up the data — fix dates, handle missing values, remove duplicates. This step took longer than I expected but made everything else much easier.

2. **Charts tell the story better than numbers.** A bar chart showing that Technology leads sales is way more impactful than just saying "Technology = $836K." I learned to pick the right chart for each type of data.

3. **Statistics matter.** It's easy to look at data and assume something is true. But the T-test and ANOVA showed me that some assumptions hold up (discounts hurt profit) while others don't (regions don't actually differ in per-order sales). Without proper tests, I would have drawn wrong conclusions.

4. **Connecting data to business decisions is the real skill.** Anyone can make a chart. The hard part is figuring out what the data actually means for the business and what should be done about it.

5. **End-to-end experience is valuable.** Going from raw data all the way to a final presentation gave me a sense of what a real analytics project looks like from start to finish.

---

## Key Findings

- Discounts are destroying profit — proved statistically with T-test (p < 0.05). Discounted orders lose $6.66 on average vs $66.90 profit for full-price ones.
- Technology is the best category — brings in $836K with the lowest discount rate (13%).
- West region makes 2.7x more profit than Central — but individual order values are similar, so the gap is about discounts and volume.
- 10 states are losing money — Texas is the worst at -$25,729.
- About 15% of customers bring in most of the revenue — classic 80/20 pattern.

---

## Contact

- **Name**: Avinash Nalla
- **Intern ID**: APSPL2632585
- **Organization**: ApexPlanet Software Pvt. Ltd.

---
