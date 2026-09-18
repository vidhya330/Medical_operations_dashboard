
import pandas as pd

# ==========================================
# 1. LOAD PROCESSED DATA
# ==========================================

monthly_admissions = pd.read_csv(
    "data/processed/monthly_admissions.csv"
)

department_workload = pd.read_csv(
    "data/processed/department_workload.csv"
)

treatment_demand = pd.read_csv(
    "data/processed/treatment_demand.csv"
)

beds = pd.read_csv(
    "data/processed/cleaned_beds.csv"
)

staff = pd.read_csv(
    "data/processed/cleaned_staff.csv"
)

# ==========================================
# 2. HIGHEST ADMISSION MONTH
# ==========================================

highest_admission = monthly_admissions.loc[
    monthly_admissions["admission_count"].idxmax()
]

# ==========================================
# 3. LOWEST ADMISSION MONTH
# ==========================================

lowest_admission = monthly_admissions.loc[
    monthly_admissions["admission_count"].idxmin()
]

# ==========================================
# 4. HIGHEST WORKLOAD DEPARTMENT
# ==========================================

highest_workload = department_workload.loc[
    department_workload["patient_count"].idxmax()
]

# ==========================================
# 5. MOST DEMANDED TREATMENT
# ==========================================

most_demanded_treatment = treatment_demand.loc[
    treatment_demand["treatment_count"].idxmax()
]

# ==========================================
# 6. BED UTILIZATION STATUS
# ==========================================

total_beds = len(beds)

occupied_beds = len(
    beds[beds["status"] == "Occupied"]
)

bed_utilization = (
    occupied_beds / total_beds
) * 100

# Define bed utilization status
if bed_utilization >= 85:
    bed_status = "High Utilization"
elif bed_utilization >= 60:
    bed_status = "Moderate Utilization"
else:
    bed_status = "Low Utilization"

# ==========================================
# 7. STAFF EFFICIENCY STATUS
# ==========================================

average_staff_efficiency = (
    staff["staff_efficiency"].mean()
)

# Define staff efficiency status
if average_staff_efficiency >= 90:
    staff_status = "Excellent Efficiency"
elif average_staff_efficiency >= 75:
    staff_status = "Good Efficiency"
else:
    staff_status = "Needs Improvement"

# ==========================================
# 8. DISPLAY OPERATIONAL INSIGHTS
# ==========================================

print("\n==========================================")
print("      HEALTHCARE OPERATIONAL INSIGHTS")
print("==========================================")

print("\n1. HIGHEST ADMISSION MONTH")
print("------------------------------------------")
print(
    "Month:",
    highest_admission["month"]
)
print(
    "Admissions:",
    highest_admission["admission_count"]
)

print("\n2. LOWEST ADMISSION MONTH")
print("------------------------------------------")
print(
    "Month:",
    lowest_admission["month"]
)
print(
    "Admissions:",
    lowest_admission["admission_count"]
)

print("\n3. HIGHEST WORKLOAD DEPARTMENT")
print("------------------------------------------")
print(
    "Department:",
    highest_workload["department"]
)
print(
    "Patients:",
    highest_workload["patient_count"]
)

print("\n4. MOST DEMANDED TREATMENT")
print("------------------------------------------")
print(
    "Treatment:",
    most_demanded_treatment["treatment_type"]
)
print(
    "Demand:",
    most_demanded_treatment["treatment_count"]
)

print("\n5. BED UTILIZATION STATUS")
print("------------------------------------------")
print(
    "Utilization:",
    round(bed_utilization, 2),
    "%"
)
print(
    "Status:",
    bed_status
)

print("\n6. STAFF EFFICIENCY STATUS")
print("------------------------------------------")
print(
    "Average Efficiency:",
    round(average_staff_efficiency, 2),
    "%"
)
print(
    "Status:",
    staff_status
)

print("\n==========================================")
print("OPERATIONAL INSIGHTS GENERATED SUCCESSFULLY")
print("==========================================")
