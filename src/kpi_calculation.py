import pandas as pd
import os

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

# ==========================================
# 2. TOTAL PATIENTS
# ==========================================

total_patients = patients["patient_id"].nunique()

# ==========================================
# 3. TOTAL ADMISSIONS
# ==========================================

total_admissions = admissions["admission_id"].nunique()

# ==========================================
# 4. TOTAL DISCHARGES
# ==========================================

total_discharges = admissions[
    admissions["discharge_date"].notna()
]["patient_id"].nunique()

# ==========================================
# 5. AVERAGE LENGTH OF STAY
# ==========================================

average_length_of_stay = (
    admissions["length_of_stay"].mean()
)

# ==========================================
# 6. BED UTILIZATION
# ==========================================

total_beds = len(beds)

occupied_beds = len(
    beds[beds["status"] == "Occupied"]
)

bed_utilization = (
    occupied_beds / total_beds
) * 100

# ==========================================
# 7. STAFF EFFICIENCY
# ==========================================

average_staff_efficiency = (
    staff["staff_efficiency"].mean()
)

# ==========================================
# 8. DEPARTMENT WORKLOAD
# ==========================================

department_workload = (
    admissions
    .groupby("department")
    .size()
    .reset_index(name="patient_count")
)

# ==========================================
# 9. TREATMENT DEMAND
# ==========================================

treatment_demand = (
    treatments
    .groupby("treatment_type")
    .size()
    .reset_index(name="treatment_count")
)

# ==========================================
# 10. CREATE KPI TABLE
# ==========================================

kpi_data = pd.DataFrame({
    "kpi_name": [
        "Total Patients",
        "Total Admissions",
        "Total Discharges",
        "Average Length of Stay",
        "Bed Utilization",
        "Average Staff Efficiency"
    ],

    "value": [
        total_patients,
        total_admissions,
        total_discharges,
        round(average_length_of_stay, 2),
        round(bed_utilization, 2),
        round(average_staff_efficiency, 2)
    ]
})

# ==========================================
# 11. DISPLAY RESULTS
# ==========================================

print("\n========== HEALTHCARE KPI REPORT ==========\n")

print(kpi_data)

print("\n========== DEPARTMENT WORKLOAD ==========\n")

print(department_workload)

print("\n========== TREATMENT DEMAND ==========\n")

print(treatment_demand)

# ==========================================
# 12. SAVE KPI OUTPUTS
# ==========================================

kpi_data.to_csv(
    "data/processed/operational_kpis.csv",
    index=False
)

department_workload.to_csv(
    "data/processed/department_workload.csv",
    index=False
)

treatment_demand.to_csv(
    "data/processed/treatment_demand.csv",
    index=False
)

print("\n========================================")
print("KPI CALCULATION COMPLETED SUCCESSFULLY")
print("========================================")