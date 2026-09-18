import pandas as pd
import numpy as np
import random
import os

# -----------------------------
# SETTINGS
# -----------------------------

NUM_ROWS = 2000
random.seed(42)
np.random.seed(42)

os.makedirs("data/raw", exist_ok=True)

# -----------------------------
# COMMON VALUES
# -----------------------------

departments = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "General Medicine",
    "Pediatrics",
    "Emergency",
    "Dermatology",
    "Oncology"
]

cities = [
    "Morena",
    "Gwalior",
    "Agra",
    "Delhi",
    "Bhopal",
    "Jaipur",
    "Indore",
    "Jhansi"
]

genders = ["Male", "Female", "Other"]

# =====================================================
# 1. PATIENTS DATASET
# =====================================================

patients = pd.DataFrame({
    "patient_id": [f"P{str(i).zfill(5)}" for i in range(1, NUM_ROWS + 1)],
    "age": np.random.randint(1, 90, NUM_ROWS),
    "gender": np.random.choice(genders, NUM_ROWS),
    "city": np.random.choice(cities, NUM_ROWS),
    "registration_date": pd.to_datetime(
        np.random.choice(
            pd.date_range("2025-01-01", "2026-06-30"),
            NUM_ROWS
        )
    )
})

patients.to_csv(
    "data/raw/patients.csv",
    index=False
)

# =====================================================
# 2. ADMISSIONS DATASET
# =====================================================

admission_dates = pd.to_datetime(
    np.random.choice(
        pd.date_range("2025-01-01", "2026-06-30"),
        NUM_ROWS
    )
)

length_of_stay = np.random.randint(1, 15, NUM_ROWS)

discharge_dates = (
    admission_dates
    + pd.to_timedelta(length_of_stay, unit="D")
)

admissions = pd.DataFrame({
    "admission_id": [
        f"A{str(i).zfill(5)}"
        for i in range(1, NUM_ROWS + 1)
    ],

    "patient_id": np.random.choice(
        patients["patient_id"],
        NUM_ROWS
    ),

    "department": np.random.choice(
        departments,
        NUM_ROWS
    ),

    "admission_date": admission_dates,

    "discharge_date": discharge_dates,

    "admission_type": np.random.choice(
        ["Emergency", "Routine", "Referral"],
        NUM_ROWS
    )
})

admissions.to_csv(
    "data/raw/admissions.csv",
    index=False
)

# =====================================================
# 3. TREATMENTS DATASET
# =====================================================

treatments = pd.DataFrame({
    "treatment_id": [
        f"T{str(i).zfill(5)}"
        for i in range(1, NUM_ROWS + 1)
    ],

    "patient_id": np.random.choice(
        patients["patient_id"],
        NUM_ROWS
    ),

    "department": np.random.choice(
        departments,
        NUM_ROWS
    ),

    "treatment_type": np.random.choice(
        [
            "Consultation",
            "Diagnostics",
            "Surgery",
            "Medication",
            "Therapy"
        ],
        NUM_ROWS
    ),

    "treatment_date": pd.to_datetime(
        np.random.choice(
            pd.date_range("2025-01-01", "2026-06-30"),
            NUM_ROWS
        )
    ),

    "treatment_status": np.random.choice(
        ["Completed", "Pending", "Cancelled"],
        NUM_ROWS,
        p=[0.75, 0.20, 0.05]
    )
})

treatments.to_csv(
    "data/raw/treatments.csv",
    index=False
)

# =====================================================
# 4. STAFF DATASET
# =====================================================

roles = [
    "Doctor",
    "Nurse",
    "Technician",
    "Administrator",
    "Support Staff"
]

shifts_assigned = np.random.randint(
    15,
    30,
    NUM_ROWS
)

shifts_worked = np.array([
    random.randint(
        int(assigned * 0.7),
        assigned
    )
    for assigned in shifts_assigned
])

staff = pd.DataFrame({
    "staff_id": [
        f"S{str(i).zfill(5)}"
        for i in range(1, NUM_ROWS + 1)
    ],

    "department": np.random.choice(
        departments,
        NUM_ROWS
    ),

    "role": np.random.choice(
        roles,
        NUM_ROWS
    ),

    "shifts_assigned": shifts_assigned,

    "shifts_worked": shifts_worked
})

staff["staff_efficiency"] = (
    staff["shifts_worked"]
    / staff["shifts_assigned"]
    * 100
).round(2)

staff.to_csv(
    "data/raw/staff.csv",
    index=False
)

# =====================================================
# 5. FACILITIES DATASET
# =====================================================

facility_types = [
    "Hospital",
    "Clinic",
    "Diagnostic Center",
    "Specialty Center"
]

facilities = pd.DataFrame({
    "facility_id": [
        f"F{str(i).zfill(5)}"
        for i in range(1, NUM_ROWS + 1)
    ],

    "facility_name": [
        f"Healthcare Facility {i}"
        for i in range(1, NUM_ROWS + 1)
    ],

    "city": np.random.choice(
        cities,
        NUM_ROWS
    ),

    "facility_type": np.random.choice(
        facility_types,
        NUM_ROWS
    ),

    "total_beds": np.random.randint(
        20,
        500,
        NUM_ROWS
    )
})

facilities.to_csv(
    "data/raw/facilities.csv",
    index=False
)

# =====================================================
# 6. BEDS DATASET
# =====================================================

beds = pd.DataFrame({
    "bed_id": [
        f"B{str(i).zfill(5)}"
        for i in range(1, NUM_ROWS + 1)
    ],

    "facility_id": np.random.choice(
        facilities["facility_id"],
        NUM_ROWS
    ),

    "department": np.random.choice(
        departments,
        NUM_ROWS
    ),

    "bed_type": np.random.choice(
        ["General", "ICU", "Emergency", "Private"],
        NUM_ROWS
    ),

    "status": np.random.choice(
        ["Occupied", "Available", "Maintenance"],
        NUM_ROWS,
        p=[0.65, 0.30, 0.05]
    )
})

beds.to_csv(
    "data/raw/beds.csv",
    index=False
)

# =====================================================
# FINAL VERIFICATION
# =====================================================

print("All datasets generated successfully!")

print("\nDataset Row Counts:")
print("Patients:", len(patients))
print("Admissions:", len(admissions))
print("Treatments:", len(treatments))
print("Staff:", len(staff))
print("Facilities:", len(facilities))
print("Beds:", len(beds))