-- E-Commerce Analytics Key Queries

-- Monthly Revenue Trend
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(order_value) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM orders
GROUP BY 1 ORDER BY 1;

-- Top 10 Products by Revenue
SELECT
    p.product_name,
    p.category,
    SUM(oi.quantity * oi.unit_price) AS revenue,
    SUM(oi.quantity) AS units_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY 1, 2 ORDER BY 3 DESC LIMIT 10;

-- Customer Cohort Retention
SELECT
    cohort_month,
    months_since_first_purchase,
    COUNT(DISTINCT customer_id) AS customers
FROM (
    SELECT
        customer_id,
        DATE_TRUNC('month', order_date) AS order_month,
        DATE_TRUNC('month', MIN(order_date) OVER (PARTITION BY customer_id)) AS cohort_month,
        EXTRACT(YEAR FROM AGE(DATE_TRUNC('month', order_date),
                              DATE_TRUNC('month', MIN(order_date) OVER (PARTITION BY customer_id)))) * 12 +
        EXTRACT(MONTH FROM AGE(DATE_TRUNC('month', order_date),
                               DATE_TRUNC('month', MIN(order_date) OVER (PARTITION BY customer_id)))) AS months_since_first_purchase
    FROM orders
) cohort_data
GROUP BY 1, 2 ORDER BY 1, 2;