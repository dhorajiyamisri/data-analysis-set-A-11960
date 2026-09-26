# 🚚 Delivery Delay Analysis

### 📊 Data Analysis Set A | End-to-End Delivery Performance Analytics

> An end-to-end data analytics project focused on analyzing delivery delays,
> identifying operational patterns, and generating actionable business insights
> using Excel, SQL, Python, and Power BI.

---

## 👤 Student Information

| Detail | Information |
|---|---|
| **Student Name** | **Misari Dhorajiya** |
| **Student ID** | **11960** |
| **Exam Set** | **Set A** |
| **Project Type** | Data Analysis Practical Examination |
| **Domain** | Data Analytics & Logistics |

---

## 🛠️ Technology Stack

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Analysis-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge&logo=matplotlib&logoColor=white)

---

## 📌 Project Overview

This project presents a complete delivery delay analysis workflow
using multiple data analysis tools.

The same dataset is analyzed independently through **Excel, SQL,
Python, and Power BI** to ensure consistent calculations and
cross-tool validation.

The analysis focuses on:

- 🚚 Delivery performance
- ⏱️ Delivery delays
- 🛣️ Route-level performance
- 🏢 Hub-level performance
- 📦 Service-type performance
- 📅 Monthly delay trends

---

## 🎯 Business Objective

The primary objective of this project is to analyze delivery performance
and identify the major factors contributing to delivery delays.

The analysis aims to transform raw delivery records into meaningful
business insights that can support operational decision-making.

---

## ❓ Business Questions

1. Which **service types and routes** contribute the most to total delivery delay?
2. How does delivery delay vary across **hubs and months**?

---

## 📊 Key Metrics

| Metric | Value |
|---|---:|
| 🚚 Total Deliveries | **12** |
| ⏱️ Total Delay Days | **34** |
| ⚠️ Delay Incidence Rate | **75.00%** |
| 🧹 Raw Records | **13** |
| ✅ Clean Records | **12** |

---

## 📁 Dataset

The project uses two CSV files:

### `deliveries.csv`

Contains the delivery-level operational records, including:

- Record ID
- Month
- Route ID
- Hub
- Promised Days
- Actual Days

### `routes.csv`

Contains route-level lookup information:

- Route ID
- Route Name
- Service Type

---

## 📖 Data Dictionary

### Deliveries Dataset

| Column | Description |
|---|---|
| `record_id` | Unique delivery record identifier |
| `month` | Delivery month |
| `route_id` | Route identifier used to connect with route information |
| `hub` | Delivery hub |
| `promised_days` | Expected delivery duration |
| `actual_days` | Actual delivery duration |

### Routes Dataset

| Column | Description |
|---|---|
| `route_id` | Unique route identifier |
| `route` | Route name |
| `service_type` | Service classification: Express or Standard |

---

## 🧹 Data Cleaning & Preparation

The following preparation steps were performed:

1. Loaded the raw delivery and route datasets.
2. Preserved the original raw delivery data.
3. Identified and removed the exact duplicate delivery record.
4. Reduced the delivery dataset from **13 records to 12 unique records**.
5. Joined route information using `route_id`.
6. Added `service_type` to the delivery-level dataset.
7. Calculated `delay_days` for each delivery record.
8. Validated that all delivery records matched a route.
9. Used the cleaned dataset consistently across Excel, SQL, Python, and Power BI.

---

## 📐 Metric Definitions

### Delay Days

```text
delay_days = MAX(actual_days - promised_days, 0)
```

Only positive delivery delays are counted.

### Delay Incidence Rate

```text
Delay Incidence Rate =
Number of delayed records / Total records
```

A delivery is considered delayed when:

```text
actual_days > promised_days
```

### Total Delay Days

The total delay is the sum of record-level `delay_days`
across the cleaned dataset.

---

## 🔄 Analysis Workflow

```text
Raw CSV Data
     │
     ▼
Data Cleaning
     │
     ├──────────────┐
     ▼              ▼
   Excel           SQL
     │              │
     └──────┬───────┘
            ▼
         Python
            │
            ▼
        Power BI
            │
            ▼
   Business Insights
```

---

## 📂 Repository Structure

```text
data-analysis-set-A-11960/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 📁 data/
│   └── 📁 raw/
│       ├── deliveries.csv
│       └── routes.csv
│
├── 📁 excel/
│   └── analysis.xlsx
│
├── 📁 sql/
│   ├── setup.sql
│   └── queries.sql
│
├── 📁 python/
│   └── analysis.py
│
├── 📁 powerbi/
│   └── dashboard.pbix
│
└── 📁 outputs/
    ├── clean_data.csv
    ├── python_summary.csv
    ├── python_chart.png
    ├── powerbi_dashboard.png
    │
    └── 📁 sql/
        ├── S2a_service_type_delay.csv
        ├── S2b_routes_delay_gt_8.csv
        └── S2c_top_2_hubs.csv
```
