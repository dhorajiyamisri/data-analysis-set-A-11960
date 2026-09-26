<div align="center">

# 🚚 Delivery Delay Analysis

### 📊 End-to-End Delivery Performance Analytics

**Data Analysis Practical Examination · Set A**

<p>
An end-to-end data analytics project focused on analyzing delivery delays,
identifying operational patterns, measuring delivery performance, and generating
actionable business insights using <b>Excel, SQL, Python, and Power BI</b>.
</p>

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-4169E1?style=for-the-badge\&logo=postgresql\&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Analysis-217346?style=for-the-badge\&logo=microsoft-excel\&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge\&logo=powerbi\&logoColor=black)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge\&logo=matplotlib\&logoColor=white)

</div>

---

> ## **"Quality is our Motto."**
>
> ### Practical Exam — Data Analysis (Set A)
>
> **Shaping "skills" for "scaling" higher ...!!!**
>
> **Red & White Skill Education**

---

# 👤 Student & Examination Information

| 📌 Detail         | 📋 Information                          |
| :---------------- | :-------------------------------------- |
| **Student Name**  | **Misari Dhorajiya**                    |
| **Student ID**    | **11960**                               |
| **Assigned Set**  | **Data Analysis Set A**                 |
| **Project Title** | **Delivery Delay Analysis**             |
| **Project Type**  | **Data Analysis Practical Examination** |
| **Domain**        | **Data Analytics & Logistics**          |

---
<img width="1312" height="1199" alt="image" src="https://github.com/user-attachments/assets/2c2c3796-11e9-4398-8d77-035a9630d59c" />

# 🎯 Business Objective

The objective of this project is to analyze delivery performance and identify
patterns associated with delivery delays.

The analysis combines **Excel, SQL, Python, and Power BI** to transform raw
delivery data into meaningful business insights.

The project focuses on:

* Measuring overall delivery performance
* Identifying delayed deliveries
* Calculating delay duration
* Comparing delivery performance across relevant categories
* Identifying operational patterns
* Creating interactive business dashboards
* Supporting data-driven operational decisions

---

# ❓ Business Questions

The analysis answers the following two primary business questions:

### Q1. What is the overall delivery delay performance?

This question evaluates:

* Total deliveries
* Delayed deliveries
* Average delay
* Delay incidence rate
* Delivery performance across relevant categories

### Q2. Which operational patterns are associated with higher delivery delays?

This question investigates delivery delays across available dimensions such as:

* Delivery routes / locations
* Service or delivery categories
* Time-based patterns
* Other relevant operational attributes available in the dataset

---

# 📂 Dataset

The project uses the delivery dataset provided for **Data Analysis Set A**.

### Dataset Files

| File                                       | Purpose                           |
| :----------------------------------------- | :-------------------------------- |
| `data/raw/delivery_data.csv`               | Raw delivery dataset              |
| `data/processed/cleaned_delivery_data.csv` | Cleaned dataset used for analysis |

> **Note:** Update the filenames above if the actual repository filenames are different.

---

# 📖 Data Dictionary

The following table documents the main variables used in the analysis.

| Column Name              | Data Type | Meaning                                             |
| :----------------------- | :-------- | :-------------------------------------------------- |
| `delivery_date`          | Date      | Date associated with the delivery                   |
| `expected_delivery_date` | Date      | Expected / scheduled delivery date                  |
| `actual_delivery_date`   | Date      | Actual delivery completion date                     |
| `route`                  | Text      | Delivery route or route identifier                  |
| `location`               | Text      | Delivery location / area                            |
| `delivery_status`        | Text      | Delivery status                                     |
| `delay_days`             | Numeric   | Number of days between actual and expected delivery |
| `service_type`           | Text      | Type/category of delivery service                   |

> **Important:** Replace this table with the **exact column names from the supplied CSV** before final submission.

---

# 🧹 Data Cleaning & Preparation

The following cleaning and preparation steps were performed before analysis:

### 1. Data Inspection

* Checked dataset dimensions
* Reviewed column names
* Checked data types
* Inspected duplicate records
* Checked missing values
* Reviewed categorical values

### 2. Date Cleaning

Date fields were converted into appropriate date formats to allow accurate
delivery-time calculations and time-based analysis.

### 3. Missing Values

Missing values were identified and handled according to the nature of each
column.

### 4. Duplicate Records

Duplicate records were checked and removed where appropriate.

### 5. Data Type Correction

Columns containing dates and numerical values stored as text were converted
to appropriate data types.

### 6. Delay Feature Creation

A derived `delay_days` metric was created for delivery-delay analysis.

---

# 📐 Metric Definitions

## Delay Days

The number of days a delivery was late compared with its expected delivery date.

```text
delay_days = actual_delivery_date - expected_delivery_date
```

For reporting purposes, a delivery is considered **delayed when delay_days > 0**.

---

## Delay Incidence Rate

The percentage of deliveries that were delayed.

```text
Delay Incidence Rate (%) =
(Number of Delayed Deliveries / Total Deliveries) × 100
```

Where:

```text
Delayed Deliveries = COUNT(delay_days > 0)
```

and

```text
Total Deliveries = COUNT(all valid deliveries)
```

---

## Average Delay

```text
Average Delay =
SUM(delay_days for delayed deliveries)
/
Number of delayed deliveries
```

> The exact calculation should follow the metric definition used consistently
> across Excel, SQL, Python and Power BI.

---

# 🛠️ Tools & Versions

| Tool                 | Purpose                                   | Version                      |
| :------------------- | :---------------------------------------- | :--------------------------- |
| **Microsoft Excel**  | Data cleaning, calculations and reporting | TODO — add installed version |
| **Power BI Desktop** | Interactive dashboard and visualization   | TODO — add version           |
| **PostgreSQL**       | SQL analysis and aggregation              | TODO — add version           |
| **Python**           | Data analysis and visualization           | TODO — add version           |
| **Pandas**           | Data manipulation and analysis            | TODO                         |
| **NumPy**            | Numerical operations                      | TODO                         |
| **Matplotlib**       | Data visualization                        | TODO                         |
| **Seaborn**          | Statistical visualization                 | TODO                         |
| **OpenPyXL**         | Excel file handling                       | TODO                         |

---

# 📁 Project Folder Structure

```text
data-analysis-set-A-11960/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── delivery_data.csv
│   │
│   └── processed/
│       └── cleaned_delivery_data.csv
│
├── excel/
│   └── analysis.xlsx
│
├── sql/
│   ├── setup.sql
│   └── queries.sql
│
├── python/
│   └── analysis.py
│
├── outputs/
│   ├── charts/
│   └── summaries/
│
├── power_bi/
│   └── delivery_delay_dashboard.pbix
│
└── video/
    └── project_demo.mp4
```

> Update this structure if your actual GitHub folder names differ.

---

# 🗄️ SQL Setup & Query Execution

The SQL analysis is divided into two stages.

## Step 1 — Run `setup.sql`

The setup script creates the required database table and loads/prepares the
dataset for SQL analysis.

Example:

```sql
-- Run first
\i sql/setup.sql
```

Or open `setup.sql` in your PostgreSQL client and execute the complete script.

---

## Step 2 — Run `queries.sql`

After the setup is completed, execute:

```sql
-- Run second
\i sql/queries.sql
```

The query file contains analysis for:

* Total deliveries
* Delayed deliveries
* Delay incidence rate
* Average delay
* Category-wise delivery performance
* Route/location analysis
* Delay pattern analysis
* Business-question analysis

### Execution Order

```text
Raw CSV
   ↓
setup.sql
   ↓
Database Table
   ↓
queries.sql
   ↓
Analysis Results
```

**Important:** Always run `setup.sql` before `queries.sql`.

---

# 🐍 Python Environment Setup

## 1. Clone the Repository

```bash
git clone https://github.com/dhorajiyamisri/data-analysis-set-A-11960.git
```

## 2. Open the Project

```bash
cd data-analysis-set-A-11960
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run Python Analysis

```bash
python python/analysis.py
```

The analysis generates the required summary outputs and visualizations inside
the `outputs/` directory.

---

# 📊 Excel Sheet Guide

The Excel workbook is used for calculations, validation and reporting.

| Sheet            | Purpose                           |
| :--------------- | :-------------------------------- |
| **Raw_Data**     | Original dataset                  |
| **Cleaned_Data** | Cleaned and prepared dataset      |
| **Calculations** | Delivery and delay calculations   |
| **Summary**      | Key metrics and aggregate results |
| **Analysis**     | Business-question analysis        |
| **Charts**       | Excel-based visualizations        |

> Rename this table to match the **actual sheet names in your workbook**.

---

# 📈 Power BI Dashboard

The Power BI dashboard provides an interactive view of delivery performance.

### Main dashboard areas

* Total Deliveries
* Delayed Deliveries
* Delay Incidence Rate
* Average Delay
* Delivery Trend
* Category / Route Performance
* Delay Distribution
* Interactive filters

---

# 🔄 Power BI Data-Source Refresh

After cloning the repository, the local CSV path may be different from the
original computer.

To update the source:

### Step 1

Open:

```text
power_bi/delivery_delay_dashboard.pbix
```

### Step 2

Go to:

```text
Home → Transform Data → Data Source Settings
```

### Step 3

Select the CSV source and choose:

```text
Change Source
```

### Step 4

Select the cloned repository's CSV file:

```text
data/raw/delivery_data.csv
```

or the actual cleaned CSV used by the dashboard.

### Step 5

Click:

```text
Close & Apply
```

### Step 6

Click:

```text
Refresh
```

The dashboard should now use the local dataset from the cloned repository.

---

# 🔍 Key Findings

The following findings are based on the completed analysis.

### Finding 1 — Overall Delay Performance

**TODO:** Insert your actual numeric finding.

Example format:

> **Finding 1:** The analysis identified **XX delayed deliveries out of XX
> total deliveries**, resulting in a delay incidence rate of **XX.XX%**.

### Finding 2 — Operational Delay Pattern

**TODO:** Insert your actual numeric finding.

Example format:

> **Finding 2:** **[Category / Route / Location]** recorded the highest delay
> incidence rate of **XX.XX%**, indicating a potential operational bottleneck.

---

# 💡 Business Recommendation

Based on the analysis:

> **Recommendation:** Management should focus on the operational category /
> route / location with the highest delay incidence and monitor its delivery
> performance regularly. A Power BI-based monitoring process can be used to
> track delay incidence rate and average delay over time so that recurring
> bottlenecks can be identified and addressed earlier.

---

# 🔁 Cross-Tool Reconciliation

To ensure consistency, one common aggregate metric was compared across all
four analytical tools.

### Reconciliation Metric

**Total Deliveries**

| Tool         | Result |
| :----------- | -----: |
| **Excel**    |   TODO |
| **SQL**      |   TODO |
| **Python**   |   TODO |
| **Power BI** |   TODO |

### Reconciliation Result

```text
Excel   = TODO
SQL     = TODO
Python  = TODO
Power BI = TODO
```

### Rounding Note

Small differences, if any, may occur because of:

* Decimal rounding
* Different display precision
* Filtering context
* Data-type conversion

The underlying records and calculation logic should remain consistent across
all four tools.

---

# 🎥 Working Video

A working demonstration video is included / linked below.

### Video

**URL:** TODO — paste YouTube / Google Drive / GitHub video URL

**Duration:** TODO minutes : TODO seconds

The demonstration should cover:

1. Dataset
2. Excel analysis
3. SQL execution
4. Python analysis
5. Power BI dashboard
6. Key findings
7. Final recommendation

---

# 📚 References

The project primarily uses the assigned dataset and standard analytical tools.

External resources used for technical reference, if any:

* Python documentation
* Pandas documentation
* PostgreSQL documentation
* Microsoft Excel documentation
* Microsoft Power BI documentation

Any external code, snippets, datasets or resources used in the project are
credited here.

---

# ✍️ Authorship Declaration

> **All work in this repository is my own except where cited.**

---

# 👩‍💻 Author

### **Misari Dhorajiya**

**Data Science / AI-ML Learner**

📌 Data Analytics · Python · SQL · Excel · Power BI

🔗 GitHub:
https://github.com/dhorajiyamisri

---

<div align="center">

### 🚚 Delivery Delay Analysis

**Data Analysis Practical Examination — Set A**

**Misari Dhorajiya · Student ID 11960**

⭐ Thank you for reviewing this project!

</div>
