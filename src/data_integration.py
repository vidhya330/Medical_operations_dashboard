import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

patients = pd.read_csv(
    "data/processed/cleaned_patients.csv"
)

admissions = pd.read_csv(
    "data/processed/cleaned_admissions.csv"
)

treatments = pd.read_csv(
    "data/processed/cleaned_treatments.csv"
)

staff = pd.read_csv(
    "data/processed/cleaned_staff.csv"
)

beds = pd.read_csv(
    "data/processed/cleaned_beds.csv"
)

facilities = pd.read_csv(
    "data/processed/cleaned_facilities.csv"
)

# ==========================================
# 2. INTEGRATE PATIENTS AND ADMISSIONS
# ==========================================

patient_admissions = pd.merge(
    patients,
    admissions,
    on="patient_id",
    how="left"
)

# ==========================================
# 3. INTEGRATE TREATMENTS
# ==========================================

integrated_data = pd.merge(
    patient_admissions,
    treatments,
    on="patient_id",
    how="left",
    suffixes=("_admission", "_treatment")
)

# ==========================================
# 4. CREATE MONTH AND YEAR COLUMNS
# ==========================================

integrated_data["admission_date"] = pd.to_datetime(
    integrated_data["admission_date"]
)

integrated_data["admission_month"] = (
    integrated_data["admission_date"].dt.month
)

integrated_data["admission_year"] = (
    integrated_data["admission_date"].dt.year
)

# ==========================================
# 5. DISPLAY INTEGRATED DATA
# ==========================================

print("\nIntegrated Dataset Information")
print("--------------------------------")

print("Rows:", integrated_data.shape[0])
print("Columns:", integrated_data.shape[1])

print("\nColumns:")
print(integrated_data.columns.tolist())

print("\nFirst 5 Records:")
print(integrated_data.head())

# ==========================================
# 6. SAVE INTEGRATED DATA
# ==========================================

integrated_data.to_csv(
    "data/processed/integrated_healthcare_data.csv",
    index=False
)

print("\n========================================")
print("DATA INTEGRATION COMPLETED SUCCESSFULLY")
print("========================================")