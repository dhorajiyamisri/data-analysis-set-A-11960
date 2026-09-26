import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================
# 1. LOAD RAW DATA
# ============================================

deliveries = pd.read_csv("data/deliveries.csv")
routes = pd.read_csv("data/routes.csv")

print("============================================")
print("DATA LOADING")
print("============================================")

print("Deliveries rows:", len(deliveries))
print("Routes rows:", len(routes))


# ============================================
# 2. REMOVE EXACT DUPLICATE
# ============================================

deliveries_clean = deliveries.drop_duplicates().copy()

print("\n============================================")
print("DUPLICATE REMOVAL")
print("============================================")

print("Rows before duplicate removal:", len(deliveries))
print("Rows after duplicate removal:", len(deliveries_clean))


# ============================================
# 3. CLEAN COLUMN NAMES
# ============================================

deliveries_clean.columns = deliveries_clean.columns.str.strip()
routes.columns = routes.columns.str.strip()


# ============================================
# 4. CLEAN ROUTE IDs
# ============================================

deliveries_clean["route_id"] = (
    deliveries_clean["route_id"]
    .astype(str)
    .str.strip()
)

routes["route_id"] = (
    routes["route_id"]
    .astype(str)
    .str.strip()
)


# ============================================
# 5. MERGE WITH ROUTES
# ============================================

clean_data = deliveries_clean.merge(
    routes[["route_id", "service_type"]],
    on="route_id",
    how="left"
)

print("\n============================================")
print("MERGE")
print("============================================")

print("Rows after merge:", len(clean_data))


# ============================================
# 6. VALIDATION
# ============================================

assert len(clean_data) == 12

assert clean_data["service_type"].notna().all()

print("12-row validation: PASSED")
print("Route matching validation: PASSED")


# ============================================
# 7. CONVERT NUMERIC COLUMNS
# ============================================

clean_data["promised_days"] = pd.to_numeric(
    clean_data["promised_days"]
)

clean_data["actual_days"] = pd.to_numeric(
    clean_data["actual_days"]
)


# ============================================
# 8. CALCULATE DELAY DAYS
# ============================================

clean_data["delay_days"] = (
    clean_data["actual_days"]
    - clean_data["promised_days"]
).clip(lower=0)


print("\n============================================")
print("CLEAN DATA")
print("============================================")

print(clean_data)


# ============================================
# 9. SERVICE TYPE SUMMARY
# ============================================

service_summary = (
    clean_data
    .groupby("service_type")
    .agg(
        total_delay_days=("delay_days", "sum"),
        total_records=("record_id", "count"),
        delayed_records=(
            "delay_days",
            lambda x: (x > 0).sum()
        )
    )
    .reset_index()
)

service_summary["delay_incidence_rate"] = (
    service_summary["delayed_records"]
    / service_summary["total_records"]
)


print("\n============================================")
print("SERVICE TYPE SUMMARY")
print("============================================")

print(service_summary)


# ============================================
# 10. FIND TOP ROUTE
# ============================================

route_delay = (
    clean_data
    .groupby("route_id")["delay_days"]
    .sum()
    .sort_values(ascending=False)
)

top_route = route_delay.index[0]
top_route_delay = route_delay.iloc[0]

overall_delay = clean_data["delay_days"].sum()

top_route_share = (
    top_route_delay / overall_delay
)


print("\n============================================")
print("TOP ROUTE")
print("============================================")

print("Top route:", top_route)
print("Top route delay:", top_route_delay)
print(
    "Top route share:",
    round(top_route_share * 100, 2),
    "%"
)


# ============================================
# 11. MONTHLY DELAY
# ============================================

month_order = ["Jan", "Feb", "Mar"]

monthly_delay = (
    clean_data
    .groupby("month")["delay_days"]
    .sum()
    .reindex(month_order)
)


print("\n============================================")
print("MONTHLY DELAY")
print("============================================")

print(monthly_delay)


# ============================================
# 12. CREATE OUTPUT FOLDER
# ============================================

output_folder = Path("outputs")

output_folder.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================
# 13. SAVE CLEAN DATA
# ============================================

clean_data.to_csv(
    output_folder / "clean_data.csv",
    index=False
)

print("\n✅ clean_data.csv CREATED")


# ============================================
# 14. SAVE PYTHON SUMMARY
# ============================================

service_summary.to_csv(
    output_folder / "python_summary.csv",
    index=False
)

print("✅ python_summary.csv CREATED")


# ============================================
# 15. CREATE MONTHLY CHART
# ============================================

plt.figure(figsize=(8, 5))

plt.plot(
    month_order,
    monthly_delay.values,
    marker="o"
)

plt.title(
    "Monthly Delivery Delay Analysis"
)

plt.xlabel("Month")

plt.ylabel(
    "Total Delay Days"
)

plt.tight_layout()

plt.savefig(
    output_folder / "python_chart.png",
    dpi=300
)

plt.show()

print("✅ python_chart.png CREATED")


# ============================================
# 16. FINAL CHECK
# ============================================

print("\n============================================")
print("PYTHON ANALYSIS COMPLETED SUCCESSFULLY")
print("============================================")

print("Total delay days:", clean_data["delay_days"].sum())

print(
    "Output files:",
    "clean_data.csv,",
    "python_summary.csv,",
    "python_chart.png"
)