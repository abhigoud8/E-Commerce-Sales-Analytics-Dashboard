# E-Commerce Sales Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.9-blue) ![SQL](https://img.shields.io/badge/SQL-PostgreSQL-blue) ![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28-brightgreen)

## Overview
A full end-to-end e-commerce analytics solution that combines SQL data engineering, Python analysis, and interactive dashboards to uncover sales trends, customer segments, and product performance insights.

## Features
- Sales trend analysis (daily, monthly, yearly)
- Customer segmentation using RFM (Recency, Frequency, Monetary) analysis
- Product performance and category insights
- Cohort analysis for customer retention
- Geo-based sales heatmap
- Interactive Power BI + Streamlit dashboards

## Tech Stack
- **Data Engineering** — SQL (PostgreSQL), pandas
- **Analysis** — Python, numpy, scipy
- **Visualization** — Power BI, Plotly, Streamlit
- **Database** — SQLite / PostgreSQL

## Project Structure
```
E-Commerce-Sales-Analytics-Dashboard/
├── sql/
│   ├── schema.sql         # Database schema
│   └── queries.sql        # Key analytical queries
├── src/
│   ├── rfm_analysis.py    # Customer segmentation
│   ├── sales_trends.py    # Sales trend analysis
│   └── dashboard.py       # Streamlit dashboard
├── notebooks/             # EDA notebooks
├── requirements.txt
└── README.md
```

## Key Insights
- Identified top 20% customers generating 80% revenue (Pareto principle)
- Peak sales detected in Q4 — driving 35% of annual revenue
- 3 major customer segments: Champions, At-Risk, Lost
- Product return rate reduced insight: electronics 12%, apparel 28%

## How to Run
```bash
pip install -r requirements.txt
streamlit run src/dashboard.py
```