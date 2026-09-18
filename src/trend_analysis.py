import pandas as pd
import os

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

admissions = pd.read_csv(
    "data/processed/cleaned_admissions.csv"
)

treatments = pd.read_csv(
    "data/processed/cleaned_treatments.csv"
)

# Convert date columns
admissions["admission_date"] = pd.to_datetime(
    admissions["admission_date"]
)

admissions["discharge_date"] = pd.to_datetime(
    admissions["discharge_date"]
)

treatments["treatment_date"] = pd.to_datetime(
    treatments["treatment_date"]
)

# ==========================================
# 2. MONTHLY ADMISSION TREND
# ==========================================

monthly_admissions = (
    admissions
    .groupby(
        admissions["admission_date"].dt.to_period("M")
    )
    .size()
    .reset_index(name="admission_count")
)

monthly_admissions["month"] = (
    monthly_admissions["admission_date"]
    .astype(str)
)

monthly_admissions = monthly_admissions[
    ["month", "admission_count"]
]

# ==========================================
# 3. MONTHLY DISCHARGE TREND
# ==========================================

discharged = admissions[
    admissions["discharge_date"].notna()
].copy()

monthly_discharges = (
    discharged
    .groupby(
        discharged["discharge_date"].dt.to_period("M")
    )
    .size()
    .reset_index(name="discharge_count")
)

monthly_discharges["month"] = (
    monthly_discharges["discharge_date"]
    .astype(str)
)

monthly_discharges = monthly_discharges[
    ["month", "discharge_count"]
]

# ==========================================
# 4. MONTHLY TREATMENT DEMAND
# ==========================================

monthly_treatments = (
    treatments
    .groupby(
        treatments["treatment_date"].dt.to_period("M")
    )
    .size()
    .reset_index(name="treatment_count")
)

monthly_treatments["month"] = (
    monthly_treatments["treatment_date"]
    .astype(str)
)

monthly_treatments = monthly_treatments[
    ["month", "treatment_count"]
]

# ==========================================
# 5. DEPARTMENT WORKLOAD TREND
# ==========================================

department_monthly_workload = (
    admissions
    .groupby([
        admissions["admission_date"].dt.to_period("M"),
        "department"
    ])
    .size()
    .reset_index(name="patient_count")
)

department_monthly_workload["month"] = (
    department_monthly_workload["admission_date"]
    .astype(str)
)

department_monthly_workload = (
    department_monthly_workload[
        ["month", "department", "patient_count"]
    ]
)

# ==========================================
# 6. SAVE TREND DATASETS
# ==========================================

monthly_admissions.to_csv(
    "data/processed/monthly_admissions.csv",
    index=False
)

monthly_discharges.to_csv(
    "data/processed/monthly_discharges.csv",
    index=False
)

monthly_treatments.to_csv(
    "data/processed/monthly_treatments.csv",
    index=False
)

department_monthly_workload.to_csv(
    "data/processed/department_monthly_workload.csv",
    index=False
)

# ==========================================
# 7. DISPLAY RESULTS
# ==========================================

print("\n========== MONTHLY ADMISSIONS ==========")
print(monthly_admissions.head())

print("\n========== MONTHLY DISCHARGES ==========")
print(monthly_discharges.head())

print("\n========== MONTHLY TREATMENTS ==========")
print(monthly_treatments.head())

print("\n====== DEPARTMENT MONTHLY WORKLOAD ======")
print(department_monthly_workload.head())

print("\n========================================")
print("TREND ANALYSIS COMPLETED SUCCESSFULLY")
print("========================================")