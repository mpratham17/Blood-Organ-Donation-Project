import streamlit as st
import pandas as pd

from db_connection import create_connection

# Database Connection
conn = create_connection()

# Query Files
query_files = {

    "All Donors":
    "backend/queries/all_donor.sql",

    "Average Donor Age":
    "backend/queries/average_donor_age.sql",

    "Blood Group Count":
    "backend/queries/blood_group_count.sql",

    "Citywise Donor Count":
    "backend/queries/citywise_donor_count.sql",

    "Donation Match Details":
    "backend/queries/donation_match_details.sql",

    "Donor Category":
    "backend/queries/donor_category_case.sql",

    "Donor Hospital Join":
    "backend/queries/donor_hospital_join.sql",

    "High Urgency Requests":
    "backend/queries/high_urgency_requests.sql",

    "Low Inventory":
    "backend/queries/low_inventory.sql",

    "Most Requested Blood":
    "backend/queries/most_requested_blood.sql",

    "O Positive Donors":
    "backend/queries/o_positive_donors.sql",

    "Organ Donor Nested Query":
    "backend/queries/organ_donor_nested_query.sql",

    "Organ Donors":
    "backend/queries/organ_donors.sql",

    "Organ Requests":
    "backend/queries/organ_requests.sql",

    "Total Requests Per Hospital":
    "backend/queries/total_requests_per_hospital.sql",

    "Blood Inventory Status":
    "backend/queries/blood_inventory.sql",
}

# Streamlit UI
st.title("Blood & Organ Donation Management System")

st.subheader("Donation Analytics Dashboard")

# Dropdown Menu
selected_query = st.selectbox(
    "Choose Report",
    list(query_files.keys())
)

# Read SQL File
with open(query_files[selected_query], "r") as file:
    query = file.read()

# Execute Query
df = pd.read_sql(query, conn)

# Display Result
st.dataframe(df)