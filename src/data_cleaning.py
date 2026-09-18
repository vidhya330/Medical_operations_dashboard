import pandas as pd
import os

# Create processed folder if it does not exist
os.makedirs("data/processed", exist_ok=True)

# ==========================================
# 1. LOAD RAW DATA
# ==========================================

patients = pd.read_csv("data/raw/patients.csv")
admissions = pd.read_csv("data/raw/admissions.csv")
treatments = pd.read_csv("data/raw/treatments.csv")
staff = pd.read_csv("data/raw/staff.csv")
beds = pd.read_csv("data/raw/beds.csv")
facilities = pd.read_csv("data/raw/facilities.csv")

# ==========================================
# 2. DATA QUALITY CHECK
# ==========================================

datasets = {
    "Patients": patients,
    "Admissions": admissions,
    "Treatments": treatments,
    "Staff": staff,
    "Beds": beds,
    "Facilities": facilities
}

print("\n========== DATA QUALITY REPORT ==========\n")

for name, df in datasets.items():

    print(f"\n{name}")
    print("-" * 40)

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

# ==========================================
# 3. CLEAN PATIENT DATA
# ==========================================

patients = patients.drop_duplicates()

patients["registration_date"] = pd.to_datetime(
    patients["registration_date"]
)

patients["gender"] = (
    patients["gender"]
    .str.strip()
    .str.title()
)

patients["city"] = (
    patients["city"]
    .str.strip()
    .str.title()
)

# ==========================================
# 4. CLEAN ADMISSION DATA
# ==========================================

admissions = admissions.drop_duplicates()

admissions["admission_date"] = pd.to_datetime(
    admissions["admission_date"]
)

admissions["discharge_date"] = pd.to_datetime(
    admissions["discharge_date"]
)

admissions["department"] = (
    admissions["department"]
    .str.strip()
    .str.title()
)

# Calculate Length of Stay
admissions["length_of_stay"] = (
    admissions["discharge_date"]
    - admissions["admission_date"]
).dt.days

# ==========================================
# 5. CLEAN TREATMENT DATA
# ==========================================

treatments = treatments.drop_duplicates()

treatments["treatment_date"] = pd.to_datetime(
    treatments["treatment_date"]
)

treatments["department"] = (
    treatments["department"]
    .str.strip()
    .str.title()
)

# ==========================================
# 6. CLEAN STAFF DATA
# ==========================================

staff = staff.drop_duplicates()

staff["department"] = (
    staff["department"]
    .str.strip()
    .str.title()
)

staff["staff_efficiency"] = (
    staff["shifts_worked"]
    / staff["shifts_assigned"]
) * 100

staff["staff_efficiency"] = (
    staff["staff_efficiency"]
    .round(2)
)

# ==========================================
# 7. CLEAN BEDS DATA
# ==========================================

beds = beds.drop_duplicates()

beds["department"] = (
    beds["department"]
    .str.strip()
    .str.title()
)

# ==========================================
# 8. CLEAN FACILITIES DATA
# ==========================================

facilities = facilities.drop_duplicates()

facilities["city"] = (
    facilities["city"]
    .str.strip()
    .str.title()
)

# ==========================================
# 9. SAVE CLEANED DATA
# ==========================================

patients.to_csv(
    "data/processed/cleaned_patients.csv",
    index=False
)

admissions.to_csv(
    "data/processed/cleaned_admissions.csv",
    index=False
)

treatments.to_csv(
    "data/processed/cleaned_treatments.csv",
    index=False
)

staff.to_csv(
    "data/processed/cleaned_staff.csv",
    index=False
)

beds.to_csv(
    "data/processed/cleaned_beds.csv",
    index=False
)

facilities.to_csv(
    "data/processed/cleaned_facilities.csv",
    index=False
)

print("\n========================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("========================================")