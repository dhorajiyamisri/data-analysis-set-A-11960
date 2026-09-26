<div align="center">

🚚 Delivery Delay Analytics

Data Analysis Practical Examination · Set A

An end-to-end analytics project built with Excel, PostgreSQL, Python & Power BI

<br/>








<br/>

Misari Dhorajiyia · Data Science & AI/ML Student · Student ID: 11960

</div>

📌 Executive Summary

This project analyses delivery performance and delay patterns across routes, hubs, service types and months.

The analysis follows a complete data workflow:

Raw Data → Data Cleaning → Transformation → SQL Analysis → Python Analysis → Dashboard → Business Insights

The same business definitions are maintained across Excel, SQL, Python and Power BI so that the final results can be independently validated.

Key numbers

Metric

Result

Raw delivery records

13

Duplicate records removed

1

Clean delivery records

12

Total delay days

34

Delayed records

9

Delay incidence

75.00%

Highest-delay route

R4 · Rural Feeder

Highest route delay

14 days

Highest-delay hub

Mumbai · 15 days

Highest-delay month

March · 17 days

🎯 Business Problem

Delivery operations need a simple way to understand where delays are accumulating and which operational segments require attention.

This project answers two practical questions:

Which service type and route contribute the most cumulative delivery delay?

Which hubs and months show the highest delay, and where should operational review be focused?

The objective is to turn delivery-level records into clear, reproducible and decision-oriented insights.

🔍 Analysis Scope

The project evaluates four dimensions:

                 DELIVERY PERFORMANCE
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
    SERVICE             ROUTE             HUB
   Express/             R1–R4          Chennai/
   Standard                              Delhi/
                                         Mumbai
                         │
                         ▼
                       MONTH
                    Jan / Feb / Mar

📊 Dashboard Preview

Place the final Power BI screenshot at outputs/powerbi_dashboard.png.



📈 Python Analysis

Place the generated Python chart at outputs/python_chart.png.



🧠 Data & Metric Logic

Dataset

The project uses two raw CSV files:

data/raw/
├── deliveries.csv
└── routes.csv

deliveries.csv

Column

Description

record_id

Delivery record identifier

month

Jan, Feb or Mar

route_id

Route lookup key

hub

Delivery hub

promised_days

Promised delivery duration

actual_days

Actual delivery duration

routes.csv

Column

Description

route_id

Route identifier

route

Route name

service_type

Express or Standard

🔗 Data Model

The route table is the lookup/master table and deliveries is the fact table.

routes
  │
  │  route_id
  │  1 : many
  ▼
deliveries

This relationship is implemented in SQL and Power BI and reproduced through a left merge in Python.

🧹 Data Cleaning

The raw delivery file contains 13 records, including one exact duplicate.

Raw records             13
          │
          ▼
Remove exact duplicate   1
          │
          ▼
Clean records            12

The original raw data is preserved separately from the cleaned dataset.

Validation

Expected clean rows      = 12
Actual clean rows        = 12
Unmatched route IDs      = 0

⏱️ Delay Definition

For every delivery:

delay_days = MAX(actual_days - promised_days, 0)

This prevents early/on-time deliveries from producing negative delay values.

Delay incidence

Delay Incidence Rate =
Delayed Records / Total Clean Records

A record is delayed when:

actual_days > promised_days

📗 Excel

Workbook

excel/analysis.xlsx

Sheets

Sheet

Purpose

Raw

Original 13-row delivery data

Lookup

Route/service lookup table

Clean

Cleaned 12-row analytical dataset

Summary

KPIs, summaries, PivotTable and chart

Key Excel operations

XLOOKUP for service_type

MAX() for delay_days

SUMIFS() for hub-level analysis

PivotTable for service type × month

Column chart for visual comparison

Service × Month Delay

Service Type

Jan

Feb

Mar

Total

Express

1

3

8

12

Standard

7

6

9

22

Total

8

9

17

34

🗄️ SQL

SQL files

sql/
├── setup.sql
└── queries.sql

The SQL workflow creates the relational model, loads the clean data and runs the required analytical queries.

Database structure

routes
-------
route_id        PRIMARY KEY
route
service_type

deliveries
----------
record_id       PRIMARY KEY
month
route_id        FOREIGN KEY
hub
promised_days
actual_days

Results

Service Type

Service Type

Total Delay

Standard

22 days

Express

12 days

Routes with delay > 8

Route

Total Delay

R4

14 days

R1

9 days

Top 2 hubs

Hub

Total Delay

Mumbai

15 days

Delhi

14 days

Data integrity check

A LEFT JOIN diagnostic was used to identify delivery records without a matching route.

Unmatched route IDs: 0

🐍 Python

Script

python/analysis.py

Libraries

pandas
matplotlib

Pipeline

Load CSVs
   ↓
Type conversion
   ↓
Remove exact duplicate
   ↓
Left merge on route_id
   ↓
Validate 12 rows
   ↓
Validate service_type
   ↓
Calculate delay_days
   ↓
Group & analyse
   ↓
Visualize
   ↓
Export outputs

Core transformation

df["delay_days"] = (
    df["actual_days"] - df["promised_days"]
).clip(lower=0)

Service summary

Service Type

Delay Days

Delay Incidence

Express

12

66.67%

Standard

22

83.33%

Highest-delay route

R4 — Rural Feeder

Total delay: 14 days

Share of overall delay: 41.18%

Monthly result

Month

Delay

Jan

8 days

Feb

9 days

Mar

17 days

📊 Power BI

File

powerbi/dashboard.pbix

Data Model

routes[route_id]
       │
       │ 1 → *
       ▼
deliveries[route_id]

The relationship is active and uses single-direction filtering from routes to deliveries.

🧮 DAX Measures

Delivery Count

Delivery Count =
COUNTROWS(deliveries)

Total Delay Days

Total Delay Days =
SUMX(
    deliveries,
    MAX(
        deliveries[actual_days] - deliveries[promised_days],
        0
    )
)

Delay Incidence Rate

Delay Incidence Rate =
DIVIDE(
    COUNTROWS(
        FILTER(
            deliveries,
            deliveries[actual_days] > deliveries[promised_days]
        )
    ),
    COUNTROWS(deliveries),
    0
)

Dashboard KPIs

Delivery Count          12
Total Delay Days        34
Delay Incidence Rate    75.00%

Interactive elements

KPI cards

Service-type delay chart

Monthly delay trend

Hub slicer

Route/service relationship model

💡 Key Insights

01 · 75% of deliveries were delayed

9 out of 12 clean delivery records exceeded their promised delivery time.

Delay incidence = 75.00%

02 · Standard service accumulated more delay

Standard service generated:

22 delay days

compared with:

12 delay days for Express.

Standard also had a higher delay incidence:

Standard → 83.33%
Express  → 66.67%

03 · R4 is the largest route-level contributor

R4 — Rural Feeder — generated:

14 of 34 total delay days

That is approximately:

41.18% of cumulative delay

04 · Mumbai has the highest hub-level delay

Mumbai    15 days
Delhi     14 days
Chennai    5 days

05 · March accounts for half of total delay

January    8 days
February   9 days
March     17 days

March contributed:

50.00% of total cumulative delay

🎯 Business Recommendation

Based on the observed dataset, operational review can be prioritised around:

🛣️ R4 — Rural Feeder

Investigate the reasons behind its high cumulative delay, such as route conditions, handling time, scheduling or capacity.

📅 March operations

Review the operational conditions associated with the March increase before assuming the pattern is persistent.

📦 Standard service

Monitor Standard-service performance because it shows both higher cumulative delay and higher delay incidence in this dataset.

Note: These are analytical recommendations based on the supplied synthetic dataset, not predictions about future operational performance.

⚠️ Limitation

This project uses a small synthetic dataset with 12 unique delivery records.

Therefore, the results demonstrate the analytical methodology and reproducibility of the workflow, but should not be treated as statistically representative of a real logistics operation.

A production analysis would benefit from:

Larger historical datasets

Delivery volume

Distance and geography

Weather information

Capacity/utilisation

Traffic conditions

Actual timestamps

Customer/service-level information

🔄 Cross-Tool Validation

A core objective of this project was to maintain the same business logic across all analysis environments.

Tool

Total Delay

📗 Excel

34

🗄️ SQL

34

🐍 Python

34

📊 Power BI

34

✅ Reconciliation

Excel ─────┐
SQL ───────┤
Python ────┼──► 34 Total Delay Days
Power BI ──┘

The matching aggregate provides a simple cross-tool validation of the cleaning and delay calculation logic.

📁 Repository Structure

data-analysis-set-A-11960/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── raw/
│       ├── deliveries.csv
│       └── routes.csv
│
├── excel/
│   └── analysis.xlsx
│
├── sql/
│   ├── setup.sql
│   ├── queries.sql
│   └── results/
│       ├── S2a_service_type_delay.csv
│       ├── S2b_routes_delay_gt_8.csv
│       └── S2c_top_2_hubs.csv
│
├── python/
│   └── analysis.py
│
├── powerbi/
│   └── dashboard.pbix
│
└── outputs/
    ├── clean_data.csv
    ├── python_summary.csv
    ├── python_chart.png
    └── powerbi_dashboard.png

⚙️ Reproducibility

Python

From the repository root:

pip install -r requirements.txt
python python/analysis.py

Generated files:

outputs/clean_data.csv
outputs/python_summary.csv
outputs/python_chart.png

SQL

Run in order:

1. sql/setup.sql
2. sql/queries.sql

The setup script creates the database objects and loads the clean records.

Excel

Open:

excel/analysis.xlsx

The workbook contains the raw, lookup, clean and summary analysis.

Power BI

Open:

powerbi/dashboard.pbix

If the repository is moved to another machine, update the documented CSV source path and refresh the model.

📦 Deliverables

Deliverable

Location

Excel workbook

excel/analysis.xlsx

SQL setup

sql/setup.sql

SQL analysis

sql/queries.sql

Python analysis

python/analysis.py

Power BI dashboard

powerbi/dashboard.pbix

Clean dataset

outputs/clean_data.csv

Python summary

outputs/python_summary.csv

Python chart

outputs/python_chart.png

Power BI screenshot

outputs/powerbi_dashboard.png

🎥 Practical Demonstration

Video: PASTE_YOUR_UNLISTED_YOUTUBE_OR_GOOGLE_DRIVE_LINK_HERE

Duration: PASTE_DURATION_HERE

The demonstration should cover:

Project introduction

Dataset structure

Duplicate cleaning

Excel analysis

SQL query

Python merge and validation

Python visualization

Power BI model

DAX measures

Dashboard interaction

Key findings

Recommendation

Limitation

Repository structure

📚 References

Red & White Skill Education — Data Analysis Practical Examination, Set A

Microsoft Excel documentation

PostgreSQL documentation

Python documentation

Pandas documentation

Matplotlib documentation

Microsoft Power BI documentation

👤 Author

<div align="center">

Misari Dhorajiyia

Data Science & AI/ML Student

Student ID · 11960

Data Analysis Practical Examination · Set A

<br/>

All work in this repository is my own except where cited.

</div>

<div align="center">

🚚 Delivery Delay Analytics

Raw Data → Clean Data → Analysis → Validation → Insights

<br/>

Built with Excel · SQL · Python · Power BI

</div>
