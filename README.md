<div align="center">

🚚 Delivery Delay Analysis

📊 Data Analysis Practical Examination — Set A

An End-to-End Delivery Performance Analytics Project using Excel, SQL, Python & Power BI

<br>








<br>

👩‍💻 Student Information

Misari Dhorajiyia

🎓 Data Science & AI/ML Student
🆔 Student ID: 11960
📚 Practical Examination: Data Analysis — Set A
🚚 Project Domain: Logistics & Delivery Analytics

<br>






</div>

🧭 Table of Contents

📌 Project Overview

🎯 Business Objective

❓ Business Questions

🔎 What I Built

🔄 End-to-End Workflow

📊 Project Snapshot

📂 Dataset

🧹 Data Cleaning & Preparation

📐 Metric Definitions

📗 Excel Analysis

🗄️ SQL Analysis

🐍 Python Analysis

📊 Power BI Dashboard

💡 Key Findings

🎯 Business Recommendation

⚠️ Limitation

🔄 Cross-Tool Reconciliation

📁 Repository Structure

🛠️ Tools & Technologies

▶️ Setup & Execution

📦 Output Files

🎥 Practical Examination Video

📚 References

👤 Authorship

📌 Project Overview

Delivery Delay Analysis is an end-to-end data analysis project created for the Data Analysis Practical Examination — Set A.

The project analyses delivery performance across:

🚚 Routes

📍 Hubs

⚡ Service Types

📅 Months

⏱️ Promised vs Actual Delivery Days

The same business rules and cleaned dataset are analysed independently using Microsoft Excel, SQL, Python and Power BI.

The goal is not only to calculate delay values, but to demonstrate a complete data-analysis workflow:

Raw Data → Cleaning → Transformation → Analysis → Visualization → Business Insights

🎯 Business Objective

The main objective of this project is to identify delivery-delay patterns and understand which routes, hubs, service types and months contribute most to cumulative delivery delays.

The analysis is designed to answer practical operational questions and convert raw delivery records into clear, measurable business insights.

🚚 Why This Analysis Matters

Delivery delays can affect:

Customer satisfaction

Operational efficiency

Route planning

Service-level performance

Hub-level workload

Delivery reliability

By analysing delay patterns consistently across multiple tools, the project demonstrates how raw operational data can be transformed into decision-support information.

❓ Business Questions

Question 01

Which service type and route contribute the most cumulative delivery delay?

Question 02

Which hubs and months show the highest delivery delay, and where should operational attention be focused?

🔎 What I Built

📗 Excel — Data Preparation & Business Summary

I used Excel to perform the spreadsheet-based data preparation and analysis.

Implemented:

Preserved the original raw delivery records.

Created a route lookup table.

Removed the exact duplicate record.

Added service_type using XLOOKUP.

Calculated delay_days using an Excel formula.

Used SUMIFS for hub-level delay analysis.

Created a service-type/month PivotTable.

Created a column chart from the PivotTable.

Kept formulas and PivotTable analysis editable.

🗄️ SQL — Relational Data Analysis

I created a relational SQL structure and reproduced the business analysis from a clean database.

Implemented:

Created routes and deliveries tables.

Defined suitable data types.

Added primary keys.

Added a foreign-key relationship.

Loaded exactly 12 clean delivery records.

Calculated delay directly in SQL.

Analysed delay by service type.

Identified routes with delay greater than 8 days.

Identified the top two hubs by cumulative delay.

Performed a data-integrity diagnostic using LEFT JOIN.

Exported analytical query results as CSV files.

🐍 Python — Reproducible Data Analysis

Python was used for programmatic data cleaning, transformation, validation, analysis and visualization.

Implemented:

Loaded both raw CSV files using Pandas.

Applied suitable numeric data types.

Removed the exact duplicate.

Performed a left merge using route_id.

Asserted that exactly 12 records remained.

Validated that there were no unmatched service_type values.

Calculated delay_days using .clip(lower=0).

Created service-level delay summaries.

Calculated delay incidence rate.

Identified the route with the highest cumulative delay.

Calculated the route's share of overall delay.

Generated the monthly delay chart using Matplotlib.

Exported clean data and summary outputs.

📊 Power BI — Interactive Business Dashboard

Power BI was used to turn the cleaned data into an interactive dashboard.

Implemented:

Loaded both datasets.

Applied data types using Power Query.

Removed the duplicate record.

Created an active one-to-many relationship.

Created a dedicated Measures table.

Created DAX measures for delivery count, total delay and delay incidence.

Built KPI cards.

Created service-type delay analysis.

Created a monthly delay trend.

Added a hub slicer.

Tested filtering behaviour.

Reconciled the dashboard results with Excel, SQL and Python.

🔄 End-to-End Workflow

                    🚚 RAW DELIVERY DATA
                           │
                           ▼
                  📂 Load CSV Files
                           │
                           ▼
                 🧹 Data Cleaning
                           │
                    Remove Duplicate
                           │
                           ▼
                    🔗 Route Lookup
                           │
                           ▼
                 ⏱️ Calculate Delay
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          📗 Excel       🗄️ SQL       🐍 Python
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                    📊 Power BI
                           │
                           ▼
                   💡 Business Insights
                           │
                           ▼
                    🎯 Recommendation

📊 Project Snapshot

📊 Metric

Result

📦 Original Delivery Records

13

🧹 Duplicate Removed

1

✅ Clean Delivery Records

12

⏱️ Total Delay Days

34

🚨 Delayed Records

9

📈 Delay Incidence Rate

75.00%

🛣️ Highest Delay Route

R4 — Rural Feeder

⏱️ Highest Route Delay

14 days

📍 Highest Delay Hub

Mumbai

⏱️ Highest Hub Delay

15 days

📅 Highest Delay Month

March

⏱️ March Delay

17 days

📂 Dataset

The project uses two CSV datasets supplied as part of the practical examination.

1️⃣ deliveries.csv

This is the main fact table containing delivery-level records.

Column

Data Type

Description

record_id

Integer

Unique delivery record identifier

month

Text

Ordered month category: Jan, Feb, Mar

route_id

Text

Route lookup key

hub

Text

Delivery hub

promised_days

Numeric

Promised delivery duration

actual_days

Numeric

Actual delivery duration

2️⃣ routes.csv

This is the lookup table containing route and service information.

Column

Data Type

Description

route_id

Text

Unique route identifier

route

Text

Route name

service_type

Text

Express or Standard

🔗 Data Relationship

The route_id field is used to connect the two datasets.

routes.route_id
      │
      │ 1
      │
      ▼
deliveries.route_id
      *

A single route can appear in multiple delivery records.

🧹 Data Cleaning & Preparation

The original deliveries.csv contains 13 rows, including one intentional exact duplicate.

The duplicate is:

record_id = 12
month     = Mar
route_id  = R4
hub       = Mumbai
promised  = 6
actual    = 15

The duplicate is removed before analysis.

🧹 Cleaning Summary

Stage

Record Count

Raw delivery records

13

Exact duplicate

1

Final clean records

12

🔄 Cleaning Process

13 Raw Records
      │
      ▼
Identify Exact Duplicate
      │
      ▼
Remove Duplicate
      │
      ▼
12 Unique Records
      │
      ▼
Map service_type using route_id
      │
      ▼
Calculate delay_days
      │
      ▼
Ready for Analysis

The same 12 clean records are used consistently across the four analysis modules.

📐 Metric Definitions

⏱️ Delay Days

The project defines delivery delay as:

delay_days = MAX(actual_days - promised_days, 0)

This means:

If actual_days > promised_days → positive delay.

If actual_days = promised_days → delay is 0.

If actual_days < promised_days → delay is 0.

🚨 Delay Incidence Rate

Delay Incidence Rate =
Number of delayed records
-------------------------
Total clean records

A record is considered delayed when:

actual_days > promised_days

For this dataset:

9 delayed records
----------------- = 75.00%
12 total records

⏱️ Total Cumulative Delay

Total delay is the sum of record-level delay_days.

Total Delay Days = SUM(delay_days)

For this project:

Total cumulative delay = 34 days

This represents cumulative record-level delay, not the number of unique parcels currently requiring expedited delivery.

📗 Excel Analysis

📁 Workbook

excel/analysis.xlsx

The Excel workbook contains four required sheets.

Sheet

Purpose

Raw

Original 13-row delivery dataset

Lookup

Route and service lookup data

Clean

12-row cleaned and enriched dataset

Summary

KPIs, hub analysis, PivotTable and chart

🧹 Excel Cleaning

The Raw sheet preserves the original 13 records.

The Clean sheet contains the cleaned 12-record dataset.

The exact duplicate was removed from the Clean sheet.

🔎 Service Type Lookup

service_type is populated from the Lookup sheet using route_id.

Example logic:

=XLOOKUP(route_id,Lookup!route_id,Lookup!service_type)

⏱️ Excel Delay Calculation

The delay_days column uses:

=MAX(actual_days-promised_days,0)

This formula is applied to all clean records.

📍 Hub Summary

SUMIFS is used to calculate cumulative delay by hub.

Results

Hub

Total Delay Days

Chennai

5

Delhi

14

Mumbai

15

📊 PivotTable

The Summary sheet contains a PivotTable with:

Rows: service_type

Columns: month

Values: Sum of delay_days

PivotTable Result

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

Grand Total

8

9

17

34

📈 Excel Chart

The workbook also contains a column chart based on the PivotTable.

The chart compares service-type delay across the three months.

🗄️ SQL Analysis

📁 SQL Files

sql/setup.sql
sql/queries.sql

The SQL workflow is designed to run in this order:

1️⃣ setup.sql
      ↓
2️⃣ queries.sql

🏗️ Database Design

Two relational tables are created:

routes
├── route_id        PRIMARY KEY
├── route
└── service_type

deliveries
├── record_id       PRIMARY KEY
├── month
├── route_id        FOREIGN KEY
├── hub
├── promised_days
└── actual_days

Relationship:

routes.route_id  1 ───────── *  deliveries.route_id

🔹 S2a — Delay by Service Type

The query joins deliveries and routes and calculates:

MAX(actual_days - promised_days, 0)

Result

Service Type

Total Delay Days

Standard

22

Express

12

The result is ordered by total delay in descending order.

🔹 S2b — Routes with Significant Delay

The query uses:

GROUP BY
HAVING

to identify routes whose summed delay exceeds 8 days.

Result

Route

Total Delay Days

R4

14

R1

9

🔹 S2c — Top Two Hubs

The query identifies the top two hubs by cumulative delay.

Result

Hub

Total Delay Days

Mumbai

15

Delhi

14

🔎 SQL Data Integrity Diagnostic

A LEFT JOIN diagnostic was performed to check for delivery records whose route_id does not exist in the lookup table.

Result

Unmatched route IDs = 0

This confirms that every clean delivery record has a matching route.

📦 SQL Output Files

outputs/sql/
├── S2a_service_type_delay.csv
├── S2b_routes_delay_gt_8.csv
└── S2c_top_2_hubs.csv

🐍 Python Analysis

📁 Python File

python/analysis.py

Python provides a reproducible programmatic analysis pipeline.

🔄 Python Workflow

Load deliveries.csv
        +
Load routes.csv
        ↓
Set Numeric Data Types
        ↓
Remove Exact Duplicate
        ↓
Left Merge on route_id
        ↓
Assert 12 Rows
        ↓
Check Unmatched service_type
        ↓
Calculate delay_days
        ↓
Service Summary
        ↓
Route Analysis
        ↓
Monthly Visualization
        ↓
Export Results

🔗 Merge Validation

The delivery data is merged with the route lookup using:

df.merge(routes, on="route_id", how="left")

The analysis validates that:

Final rows = 12
Unmatched service_type = 0

This prevents accidental row loss or invalid route mappings.

⏱️ Delay Calculation

Python calculates delay using:

df["delay_days"] = (
    df["actual_days"] - df["promised_days"]
).clip(lower=0)

📊 Service-Level Analysis

Result

Service Type

Total Delay Days

Delay Incidence

Express

12

66.67%

Standard

22

83.33%

🛣️ Highest Delay Route

Python identifies:

Route: R4
Route Name: Rural Feeder
Total Delay: 14 days

Its contribution to overall delay is:

14 / 34 × 100 = 41.18%

📈 Monthly Delay Visualization

The monthly cumulative delay is:

Month

Delay Days

Jan

8

Feb

9

Mar

17

Python Chart



Figure: Monthly cumulative delivery delay.

📤 Python Outputs

outputs/
├── clean_data.csv
├── python_summary.csv
└── python_chart.png

📊 Power BI Dashboard

📁 Power BI File

powerbi/dashboard.pbix

The Power BI dashboard provides an interactive view of delivery performance.

🔄 Power Query Preparation

The Power Query workflow includes:

Load deliveries.csv.

Load routes.csv.

Set suitable data types.

Remove the exact duplicate.

Validate the final 12 delivery records.

Load the cleaned model.

🔗 Data Model

The model uses an active one-to-many relationship:

routes
   │
   │ 1
   │
   ▼
deliveries
   *

Filter direction:

routes → deliveries

🧮 DAX Measures

📦 Delivery Count

Delivery Count =
COUNTROWS(deliveries)

Expected result:

12

⏱️ Total Delay Days

Total Delay Days =
SUMX(
    deliveries,
    MAX(
        deliveries[actual_days] - deliveries[promised_days],
        0
    )
)

Expected result:

34

🚨 Delay Incidence Rate

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

Expected result:

75.00%

🖥️ Dashboard Components

The dashboard contains:

📦 KPI Cards

Delivery Count → 12

Total Delay Days → 34

Delay Incidence Rate → 75.00%

📊 Service Type Chart

Express  → 12 delay days
Standard → 22 delay days

📈 Monthly Trend

Jan → 8
Feb → 9
Mar → 17

🎛️ Hub Slicer

The interactive hub slicer allows the dashboard to be filtered by:

Chennai

Delhi

Mumbai

🖼️ Power BI Dashboard Preview



Figure: Interactive Delivery Delay Analysis dashboard.

💡 Key Findings

🚨 Finding 01 — High Delay Incidence

Out of 12 clean delivery records, 9 were delayed.

Therefore:

Delay Incidence Rate = 75.00%

🚚 Finding 02 — Standard Service

Standard service generated:

22 cumulative delay days

while Express service generated:

12 cumulative delay days

🛣️ Finding 03 — R4 is the Highest-Delay Route

R4 — Rural Feeder recorded:

14 delay days

This represents:

41.18% of the total 34 delay days

📍 Finding 04 — Mumbai Has the Highest Hub Delay

Hub-level results:

Mumbai  → 15 days
Delhi   → 14 days
Chennai →  5 days

Mumbai therefore has the highest cumulative delay in this dataset.

📅 Finding 05 — March Shows the Highest Delay

Monthly delay:

January  →  8 days
February →  9 days
March    → 17 days

March accounts for:

17 / 34 × 100 = 50.00%

of the total cumulative delay.

🎯 Business Recommendation

Based on the observed results, operational review should focus on:

1️⃣ R4 — Rural Feeder

R4 contributes the highest cumulative route delay.

A detailed review could investigate:

Route distance

Hub handling time

Delivery capacity

Operational bottlenecks

Scheduling constraints

2️⃣ March Operations

March records the highest monthly delay.

A month-level operational review can help identify whether the increase is related to:

Route workload

Capacity

Scheduling

Hub performance

Delivery volume patterns

3️⃣ Standard Service Monitoring

Standard service records higher cumulative delay and delay incidence than Express service in this dataset.

Regular service-level monitoring can help identify recurring performance gaps.

⚠️ Limitation

This analysis uses a synthetic dataset containing only 12 unique delivery records.

Therefore:

The dataset is small.

The results demonstrate the analytical workflow.

The results should not be interpreted as a real-world operational forecast.

Larger historical datasets would be required for reliable operational decision-making.

🔄 Cross-Tool Reconciliation

One of the key validation steps was comparing the total cumulative delay across all four analysis tools.

Analysis Tool

Total Delay Days

📗 Excel

34

🗄️ SQL

34

🐍 Python

34

📊 Power BI

34

✅ Final Reconciliation

Excel = SQL = Python = Power BI = 34 delay days

This confirms that the core cleaning and delay-calculation logic is consistent across the project.

📁 Repository Structure

data-analysis-set-A-11960/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 📂 data/
│   └── 📂 raw/
│       ├── deliveries.csv
│       └── routes.csv
│
├── 📂 excel/
│   └── 📊 analysis.xlsx
│
├── 📂 sql/
│   ├── 🗄️ setup.sql
│   └── 🗄️ queries.sql
│
├── 📂 python/
│   └── 🐍 analysis.py
│
├── 📂 powerbi/
│   └── 📊 dashboard.pbix
│
└── 📂 outputs/
    ├── clean_data.csv
    ├── python_summary.csv
    ├── python_chart.png
    ├── powerbi_dashboard.png
    │
    └── 📂 sql/
        ├── S2a_service_type_delay.csv
        ├── S2b_routes_delay_gt_8.csv
        └── S2c_top_2_hubs.csv

🛠️ Tools & Technologies

Technology

Purpose

📗 Microsoft Excel

Data cleaning, formulas, PivotTable & chart

🗄️ PostgreSQL

Database creation & SQL analysis

🐍 Python

Programmatic data analysis

🐼 Pandas

Data manipulation & transformation

📈 Matplotlib

Data visualization

📊 Power BI

Interactive dashboard

🔧 Git

Version control

🌐 GitHub

Repository & project submission

⚙️ Data & File Requirements

The repository keeps the original raw files separate from generated analytical outputs.

Raw Data

data/raw/deliveries.csv
data/raw/routes.csv

Analysis Files

excel/analysis.xlsx
sql/setup.sql
sql/queries.sql
python/analysis.py
powerbi/dashboard.pbix

Outputs

outputs/

This separation makes the project easier to reproduce and review.

▶️ Setup & Execution

🗄️ SQL Setup

Open the SQL environment and execute:

1. sql/setup.sql
2. sql/queries.sql

setup.sql creates the database tables and loads the clean records.

queries.sql executes the required analytical queries.

🐍 Python Setup

From the repository root:

pip install -r requirements.txt

Run:

python python/analysis.py

The script generates:

outputs/clean_data.csv
outputs/python_summary.csv
outputs/python_chart.png

📗 Excel

Open:

excel/analysis.xlsx

The workbook contains:

Raw
Lookup
Clean
Summary

The formulas and PivotTable remain editable for examiner verification.

📊 Power BI

Open:

powerbi/dashboard.pbix

If the repository is moved to another computer, update the CSV source path in Power Query and refresh the model.

📦 Output Files

File

Purpose

clean_data.csv

Final 12-row merged dataset

python_summary.csv

Python service-level analysis

python_chart.png

Monthly delay visualization

powerbi_dashboard.png

Power BI dashboard preview

S2a_service_type_delay.csv

SQL service-type analysis

S2b_routes_delay_gt_8.csv

SQL high-delay route analysis

S2c_top_2_hubs.csv

SQL top-two hub analysis

🎥 Practical Examination Video

🎬 Video Link

[PASTE YOUR UNLISTED YOUTUBE / GOOGLE DRIVE VIDEO LINK HERE]

⏱️ Duration

[ENTER VIDEO DURATION — 5 to 10 MINUTES]

🎤 Video Coverage

The practical demonstration covers:

👋 Introduction and student information

🎯 Business objective

📂 Dataset structure

🧹 Duplicate identification and cleaning

📗 Excel XLOOKUP and delay calculation

📊 Excel PivotTable and chart

🗄️ SQL analytical query

🐍 Python merge and assertion

📈 Python visualization

📊 Power BI data model

🧮 DAX measures

🎛️ Power BI slicer

💡 Two key findings

🎯 Recommendation

⚠️ Limitation

📁 GitHub repository structure

📚 References

Red & White Skill Education — Data Analysis Practical Examination, Set A

Python Documentation

Pandas Documentation

Matplotlib Documentation

Microsoft Excel Documentation

Microsoft Power BI Documentation

PostgreSQL Documentation

👤 Authorship

All work in this repository is my own except where cited.

This repository contains the complete analysis workflow, source files and generated outputs for the Data Analysis Practical Examination — Set A.

<div align="center">

🚚 From Raw Data to Business Insight

📂 Data → 🧹 Cleaning → 🗄️ SQL → 🐍 Python → 📊 Power BI → 💡 Insights

<br>

⭐ Delivery Delay Analysis — Set A

Misari Dhorajiyia | Student ID 11960

<br>






</div>
