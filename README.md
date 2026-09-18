# 🏥 Hospital Management Dashboard

## Healthcare Operations Intelligence Dashboard with Decision Analytics

**Group 2 · Batch 2 · Team A**

The Hospital Management Dashboard is an interactive healthcare operations intelligence and decision-analytics solution developed in Microsoft Power BI. It transforms hospital operational data into a centralized analytical view covering patients, admissions, treatments, facilities, beds, workforce, and geographic performance.

The dashboard is designed to help users move from a high-level understanding of hospital operations to detailed operational analysis, identify meaningful patterns, compare departments and locations, and translate findings into management-oriented insights and recommendations.

\---

## 🔗 Live Dashboard

!\[Hospital\_Management\_Dashboard](./src/Hospital\_Management\_Dashboard.jpg)
[**View Live Power BI Dashboard →**](https://app.powerbi.com/view?r=eyJrIjoiZjNkM2M4MmItMjc0ZC00OTEyLWJhZDgtOTdlMDI5ODgzMTUyIiwidCI6IjNjYmNmZWY2LWUxZGEtNDEyNy04Nzg0LTAyZmQ1ZmJkMWZlNCJ9&pageName=ee3c1ea0d0b6e6b65902)

\---

## 🎯 Project Objectives

The primary objective of the project is to develop a centralized healthcare operations intelligence dashboard that converts hospital operational data into meaningful analytical information.

The project focuses on:

* Analyzing patient demographics, activity, and registration patterns.
* Monitoring admissions, discharges, and admission types.
* Understanding patient movement and length of stay.
* Analyzing treatment demand and treatment status.
* Examining facility distribution and reported bed capacity.
* Analyzing workforce distribution, shifts, and staff efficiency.
* Comparing healthcare activity and infrastructure across cities.
* Developing centralized KPIs and analytical measures using DAX.
* Enabling interactive filtering and drill-down analysis.
* Identifying operational patterns and areas requiring attention.
* Translating analytical findings into management-oriented recommendations.

\---

## 🗂️ Data \& Data Model

The project uses a healthcare operations dataset containing information related to patients, admissions, treatments, beds, staff, and facilities.

!\[Data\_Model](./src/Data\_Model.jpg)
The data model follows a Star Schema, with dimension tables providing descriptive context and fact tables containing operational records.

### Data Model Tables

|Table|Purpose|Key Fields|
|-|-|-|
|`Dim\_Patient`|Patient demographics, geography \& registration|`patient\_id`, `age`, `gender`, `city`, `registration\_date`|
|`Dim\_Facility`|Facility information \& reported capacity|`facility\_id`, `facility\_name`, `facility\_type`, `city`, `total\_beds`|
|`Dim\_Date`|Time-based analysis|`date`, `month`, `month\_number`, `year`|
|`Fact\_Admissions`|Admission, discharge \& LOS records|`admission\_id`, `patient\_id`, `admission\_type`, `admission\_date`, `discharge\_date`, `length\_of\_stay`|
|`Fact\_Treatments`|Treatment activity \& status|`treatment\_id`, `patient\_id`, `treatment\_type`, `treatment\_status`, `department`, `treatment\_date`|
|`Fact\_Beds`|Bed information \& status|`bed\_id`, `bed\_type`, `department`, `facility\_id`, `status`|
|`Fact\_Staff`|Workforce, shifts \& efficiency|`staff\_id`, `department`, `role`, `shifts\_assigned`, `shifts\_worked`, `staff\_efficiency`|
|`\_Measures`|Centralized DAX calculations|DAX measures|

### 🔗 Table Relationships

The model connects Patient information with admission and treatment activity, while Department supports analysis across admissions, treatments, beds, and staff. Facility connects facility, city, and capacity analysis, and the Date dimension provides consistent time-based analysis across relevant activities.

This structure allows different operational areas to be analyzed independently while maintaining consistent filtering and analytical context across the dashboard.

\---

## 🧹 Data Preparation

Python-based data preparation and analysis were used as part of the project workflow.

### Tools

* Python
* Pandas
* NumPy
* Jupyter Notebook

The preparation process supported data exploration, manipulation, and preparation for analytical modeling and visualization.

\---

## 📊 Dashboard Pages

The dashboard is designed as a continuous analytical journey across eight pages, each accessible from a consistent top navigation bar:

**Home · Patients · Admissions · Facilities · Staff · Treatments · Geographic · Insights**

### 1\. Executive Overview

This is the landing page that gives a quick summary of the entire hospital system before going into detail elsewhere.

**Key numbers:**

* Total Patients (2,000)
* Total Admissions (2,000)
* Total Treatments (2,000)
* Total Staff (2,000)
* Total Facilities (2,000)
* Total Beds (517,396)

**Visualizations:**

* Shows admissions ranked by department, with General Medicine at the top and Orthopedics at the bottom.
* Tracks monthly admissions, which stay steady from January to June and then drop noticeably for the rest of the year.
* Displays patient locations across the eight covered cities on a map.
* Shows the gender split of patients: Male 34.8%, Female 33.1%, Other 32.1%.

**Filters:** Department, Gender, City, and Admission Date.

\---

### 2\. Patient Analytics Dashboard

This page focuses on patient demographics - who the patients are and where they come from.

**Key numbers:**

* Total Patients (2,000)
* Average Age (43.79)
* Male Patients (696)
* Female Patients (662)
* Cities Covered (8)

**Visualizations:**

* Groups patients by age range, with the 65+ group being the largest and the 36–50 group the smallest.
* Ranks the top cities by patient count, led by Jhansi, Agra, and Bhopal.
* Shows the gender breakdown again for quick reference.
* Displays the detailed age spread of all patients.
* Tracks monthly patient registrations, which are steady through June and then decline.

**Filters:** Gender, City, and Registration Date.

\---

### 3\. Admissions Analytics Dashboard

This page looks at how patients are admitted and how long they stay.

**Key numbers:**

* Total Admissions (1,882)
* Average Length of Stay (7.58 days)
* Emergency Admissions (612)
* Routine Admissions (624)
* Discharged Admissions (1,882)

**Visualizations:**

* Ranks departments by number of admissions.
* Shows admission types - Referral, Routine, and Emergency - in almost equal shares.
* Shows how many patients stay for how many days, with a good number of patients staying longer than average.
* Tracks the monthly admission trend, which follows the same rise-then-drop pattern seen on other pages.
* Compares admission type across each department.

**Filters:** Admission Type, Department, Admission Date, and Discharge Date.

\---

### 4\. Facilities Analytics Dashboard

This page covers hospital infrastructure - facilities, beds, and capacity.

**Key numbers:**

* Total Facilities (2,000)
* Total Beds (517,396)
* Cities Covered (8)
* Average Beds per Facility (258.70)
* Maximum Facility Beds (499)

**Visualizations:**

* Compares facility counts by type: Clinic, Hospital, Specialty Center, and Diagnostic Center.
* Shows total bed capacity by facility type, with Hospitals and Clinics holding the most beds.
* Lists the top ten facilities with the highest bed capacity.
* Shows how facilities are spread across the eight cities, fairly evenly.

**Filters:** Facility Type, City, and Facility Name.

\---

### 5\. Staff Analytics Dashboard

This page covers the hospital workforce and how efficiently staff are working.

**Key numbers:**

* Total Staff (2,000)
* Total Shifts Worked (37,185)
* Total Shifts Assigned (44,062)
* Departments Covered (8)
* Average Staff Efficiency (84.34%)

**Visualizations:**

* Ranks staff count by department, with Pediatrics having the most staff.
* Shows staff split by role - Support Staff, Doctor, Administrator, Technician, and Nurse - in nearly equal shares.
* Compares shifts worked versus shifts assigned for each department, showing that every department works fewer shifts than assigned.
* Shows staff efficiency by role and by department, which stay close to each other with little difference.

**Filters:** Department and Role.

\---

### 6\. Treatment Analytics Dashboard

This page tracks treatments given to patients and their outcomes.

**Key numbers:**

* Total Treatment (2,000)
* Pending Treatments (396)
* Cancelled Treatments (103)
* Completed Treatments (1,501)
* Treatment Types (5)

**Visualizations:**

* Compares the five treatment types - Consultation, Surgery, Medication, Diagnostics, and Therapy — which are fairly balanced.
* Shows treatment status: 75.05% Completed, 19.8% Pending, and 5.15% Cancelled.
* Tracks monthly treatment activity over the reporting period.
* Ranks departments by treatment count, with Neurology at the top.
* Compares treatment type across each department.

**Filters:** Treatment Status, Treatment Type, Department, and Date.

\---

### 7\. Geographic Performance

This page compares hospital activity across all eight cities.

**Key numbers:**

* Count of City (8)
* Total Facilities (2K)
* Total Beds (517K)
* Total Patients (2K)

**Visualizations:**

* Ranks bed capacity by city, with Agra having the highest capacity.
* Ranks patient count by city, with Jhansi having the most patients.
* Tracks admissions by city, following a similar order to patient count.
* Shows patient distribution on a map, with marker size based on patient volume.

**Filters:** City, Department, and Date.

\---

### 8\. Insights \& Recommendations

A synthesis page pairing findings with actions, organized in two columns:

|Findings|Recommendations|
|-|-|
|*Bed Utilization* (63.9% occupancy, capacity available for additional demand)|**Optimize Bed Allocation** (monitor utilization by city/department/bed type, allocate toward higher-demand areas)|
|*Patient Stay* (average length of stay 7.58 days)|**Improve Patient Flow** (monitor high-workload/longer-stay departments, strengthen discharge planning)|
|*Workforce Performance* (84.34% staff efficiency)|**Balance Staff Workload** (use efficiency and workload data to refine shift allocation)|
|*Treatment Completion* (75.1% completion rate)|**Improve Treatment Completion** (track pending/cancelled treatments by department and type)|

#### Management Action Plan

A closing *Management Action Plan* band condenses these into three action areas:

* **Capacity:** Align bed utilization with admission demand.
* **Workforce:** Review efficiency and workload for shift planning.
* **Treatment:** Monitor pending/cancelled treatments and prioritize low-completion areas.

\---

## 🛠️ Technology Stack

|Technology / Tool|Purpose|
|-|-|
|Microsoft Power BI|Dashboard development, data modeling and interactive visualization|
|DAX|KPI calculations, analytical measures and business logic|
|Python|Data preparation and analysis|
|Pandas|Data manipulation and preparation|
|NumPy|Numerical processing|
|Jupyter Notebook|Data exploration and preparation|
|Git|Version control|
|GitHub|Repository management, collaboration and documentation|

\---

## ✅ Project Development \& Milestones

### ✅ Milestone 1 - Healthcare Data Integration \& Operational Analytics

**Weeks 1-2 · Completed**

* Healthcare operational datasets collected and preprocessed.
* Key healthcare performance indicators defined.
* Analytical foundation established.
* Integrated datasets prepared for downstream analysis.

### ✅ Milestone 2 - Patient Flow \& Service Demand Intelligence

**Weeks 3-4 · Completed**

* Patient-flow analytics implemented.
* Admission and discharge activity analyzed.
* Treatment demand analyzed.
* Departmental workload examined.
* Operational bottlenecks and high-demand service areas identified.

### ✅ Milestone 3 - Resource Utilization \& Capacity Intelligence

**Weeks 5-6 · Completed**

* Bed utilization calculated.
* Staffing efficiency analyzed.
* Operational capacity monitored.
* Resource KPI dashboards implemented.
* Performance scorecards developed.
* Operational capacity intelligence generated.

### ✅ Milestone 4 - Geographic Healthcare Intelligence \& Executive Dashboard

**Weeks 7-8 · Completed**

* Geographic patient-distribution visualizations developed.
* Healthcare service coverage analyzed.
* Operational intelligence modules integrated.
* Executive reporting developed.
* Complete healthcare operations intelligence platform deployed.

The project documentation defines these four milestones across the complete eight-week development timeline.

\---

## 📁 Repository Structure

```text
medical-operations-dashboard-team-a-batch-2/
├── data/                                    # Datasets (monthly\_admissions.csv, etc.)
├── notebooks/                               # Exploratory Data Analysis (Module 1)
├── src/                                     # Source code (incl. Data Model image)
├── Defect\_Tracker Template\_v0.1 (1).xlsx
├── Hospital\_Management\_Dashboard by harshada...
├── Hospital\_Management\_Dashboard.pbix        # Power BI dashboard file
├── LICENSE                                   # MIT License
├── README.md
└── Unit\_Test\_Plan\_v0.1 (1).xlsx
```

\---

## 🔍 Data Quality \& Limitations

The dashboard is an operational analytics and decision-support solution based on the available project dataset.

* The analysis reflects the records available within the project's defined reporting period.
* Metrics such as bed capacity, staff efficiency, treatment completion, and admissions represent values in the underlying dataset.
* Reported facility and bed capacity should not automatically be interpreted as real-time physical availability.
* Cross-functional comparisons depend on the relationships and analytical logic established in the Power BI data model.
* The dashboard currently covers 8 cities represented in the dataset.
* The dashboard provides analytical evidence and operational indicators; it is not intended to replace clinical judgment, hospital policies, or validated real-time operational systems.

\---

## 🚀 Future Enhancements

### 🔄 Automated Data Refresh

Connect the dashboard to live or scheduled healthcare data sources to reduce manual data preparation.

### 📈 Predictive Analytics

Potential extensions include:

* Admission demand forecasting
* Bed occupancy forecasting
* Treatment demand forecasting
* Workforce requirement planning
* Patient length-of-stay prediction

### 🛏️ Advanced Capacity Intelligence

* Real-time bed availability
* Department-level capacity thresholds
* Bed-type utilization
* Maintenance availability
* Capacity forecasting
* Demand-versus-capacity alerts

### 👨‍⚕️ Workforce Planning

* Shift-demand forecasting
* Staffing requirement estimation
* Absence and attendance analysis
* Workload-to-staff ratios
* Workforce capacity alerts

### 🌍 Expanded Geographic Intelligence

* Additional geographic indicators
* Service accessibility analysis
* Location-level benchmarking

### 🚨 Operational Alerts

Potential threshold-based alerts for:

* High bed utilization
* Increasing length of stay
* Low treatment completion
* High pending-treatment volumes
* Staffing gaps
* Capacity constraints

### 🔐 Enterprise Deployment

Potential future deployment could include:

* Role-based access
* Secure data pipelines
* Centralized governance
* Hospital information-system integration

\---

## 🏁 Project Completion/Outcome

The Hospital Management Dashboard provides an integrated view of key hospital operations through a structured and interactive analytical solution.

The completed project brings together multiple operational perspectives into a single workflow:

**Understand Hospital Activity → Analyze Operational Patterns → Compare Departments \& Locations → Identify Findings → Support Management Decisions**

The final solution enables users to monitor hospital activity, analyze patients and admissions, understand treatment and facility performance, evaluate workforce efficiency, compare geographic operations, and translate analytical findings into management-oriented actions.

**🏥 Built With**

Power BI · DAX · Python · Pandas · NumPy · Jupyter Notebook · Git · GitHub

**🔗 Live Dashboard**

[View Live Power BI Dashboard →](https://app.powerbi.com/view?r=eyJrIjoiZjNkM2M4MmItMjc0ZC00OTEyLWJhZDgtOTdlMDI5ODgzMTUyIiwidCI6IjNjYmNmZWY2LWUxZGEtNDEyNy04Nzg0LTAyZmQ1ZmJkMWZlNCJ9&pageName=ee3c1ea0d0b6e6b65902)

