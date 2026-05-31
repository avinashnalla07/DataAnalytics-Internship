-- Task 2 - SQL Business Queries for Superstore Sales Analysis

-- Q1: Which products bring in the most sales?
SELECT 
    "Product Name",
    ROUND(SUM(Sales), 0) AS Total_Sales
FROM superstore
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 5;

-- Q2: How do sales change month by month?
SELECT 
    strftime('%Y-%m', "Order Date") AS Month,
    ROUND(SUM(Sales), 0) AS Total_Sales
FROM superstore
GROUP BY Month
ORDER BY Month;

-- Q3: Which region makes the most profit?
SELECT 
    Region,
    ROUND(SUM(Profit), 0) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Profit DESC;

-- Q4: How many customers are in each segment?
SELECT 
    Segment,
    COUNT(DISTINCT "Customer ID") AS Customer_Count
FROM superstore
GROUP BY Segment
ORDER BY Customer_Count DESC;

-- Q5: What's the average discount for each category?
SELECT 
    Category,
    ROUND(AVG(Discount) * 100, 0) || '%' AS Avg_Discount
FROM superstore
GROUP BY Category
ORDER BY AVG(Discount) DESC;

-- Q6: Which states are actually losing money?
SELECT 
    State,
    ROUND(SUM(Profit), 0) AS Total_Profit
FROM superstore
GROUP BY State
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC;

-- Q7: How do customers prefer to ship their orders?
SELECT 
    "Ship Mode",
    COUNT(*) AS Order_Count
FROM superstore
GROUP BY "Ship Mode"
ORDER BY Order_Count DESC;
