import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import mysql.connector

def create_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="BloodOrganDonation"
    )

    return conn

#########    DONOR REGISTRATION      #########
def insert_donor(name, age, gender, blood_group,
                 city, phone, organ_donor,
                 organ_type, donation_date):
    conn = create_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO donor
    (donor_name,
     age,
     gender,
     blood_group,
     city,
     phone,
     organ_donor,
     organ_type,
     last_donation_date)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    values = (
        name,
        age,
        gender,
        blood_group,
        city,
        phone,
        organ_donor,
        organ_type,
        donation_date
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# Fetch Donor
def fetch_donors():
    conn = create_connection()
    query = "SELECT * FROM donor"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# =========================
# PATIENT REQUEST FUNCTIONS
# =========================

def insert_patient_request(
    hospital_id,
    patient_name,
    blood_required,
    organ_required,
    required_units,
    urgency_level,
    request_date
):
    conn = create_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO patient_request
    (
        hospital_id,
        patient_name,
        blood_required,
        organ_required,
        required_units,
        urgency_level,
        request_date
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    values = (
        hospital_id,
        patient_name,
        blood_required,
        organ_required,
        required_units,
        urgency_level,
        request_date
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def fetch_patient_requests():
    conn = create_connection()
    query = "SELECT * FROM patient_request"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def run_query(query):
    conn = create_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# =========================
# DONATE BLOOD FUNCTIONS
# =========================

def fetch_active_requests():

    conn = create_connection()

    query = """
    SELECT request_id,
           patient_name,
           blood_required,
           required_units,
           urgency_level
    FROM patient_request
    WHERE blood_required IS NOT NULL;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def insert_donation_record(
    donor_id,
    hospital_id,
    donation_type,
    donation_units,
    donation_date
):

    try:

        conn = create_connection()

        cursor = conn.cursor()

        query = """
        INSERT INTO donation_record
        (
            donor_id,
            hospital_id,
            donation_type,
            donation_units,
            donation_date
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        values = (
            donor_id,
            hospital_id,
            donation_type,
            donation_units,
            donation_date
        )

        cursor.execute(query, values)

        conn.commit()

        cursor.close()
        conn.close()

        return True, "Donation submitted successfully!"

    except mysql.connector.Error as err:

        return False, err.msg

# Page Configuration
st.set_page_config(
    page_title="DBMS Dashboard",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    [data-testid="stSidebar"] {
        background-color: #003B7A;
    }
    
    [data-testid="stAppViewContainer"] {
        padding-top: 0 !important;
        margin: 0 !important;
    }
    
    .sidebar-title {
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 20px 10px;
        text-align: center;
        margin-bottom: 20px;
        border-bottom: 2px solid rgba(255,255,255,0.2);
    }
    
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .metric-label {
        font-size: 14px;
        color: #666;
        text-transform: uppercase;
        font-weight: 600;
    }
    
    .section-title {
        color: #003B7A;
        font-size: 20px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 20px;
        border-bottom: 3px solid #CE1126;
        padding-bottom: 10px;
    }
    
    .notification-item {
        padding: 15px;
        border-left: 4px solid #CE1126;
        background-color: #f8f9fa;
        margin-bottom: 10px;
        border-radius: 4px;
    }
    
    .notification-title {
        color: #003B7A;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .notification-time {
        color: #999;
        font-size: 12px;
    }
    
    .red-card {
        background-color: #CE1126;
        color: white;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .red-card-value {
        font-size: 48px;
        font-weight: bold;
        margin: 20px 0;
    }
    
    .red-card-label {
        font-size: 14px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page tracking
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# Sidebar Navigation
pages = ["Dashboard", "Donors", "Hospital", "Patient Requests", "Donation Centre" , "Donation Match" , "Blood Inventory"]

with st.sidebar:
    st.markdown('<div class="sidebar-title">🩸 DBMS Project<br><span style="font-size: 12px;">Blood & Organ Donation System</span></div>', unsafe_allow_html=True)
    st.markdown("")
    
    for page_name in pages:
        is_active = st.session_state.current_page == page_name
        
        # Show red circle for active button
        button_text = f"🔴 {page_name}" if is_active else page_name
        
        if st.button(
            button_text,
            key=page_name,
            use_container_width=True,
        ):
            st.session_state.current_page = page_name
            st.rerun()

page = st.session_state.current_page

# Dashboard Page
if page == "Dashboard":
    st.markdown('<h1 style="color: #CE1126;">DASHBOARD</h1>', unsafe_allow_html=True)
    st.divider()
    
    # =========================
    # DASHBOARD METRICS
    # =========================

    conn = create_connection()

    cursor = conn.cursor()

    # Total Donors
    cursor.execute("""
    SELECT COUNT(*)
    FROM donor;
    """)

    total_donors = cursor.fetchone()[0]

    # Blood Donors
    cursor.execute("""
    SELECT COUNT(*)
    FROM donor
    WHERE organ_donor = FALSE;
    """)

    blood_donors = cursor.fetchone()[0]

    # Organ Donors
    cursor.execute("""
    SELECT COUNT(*)
    FROM donor
    WHERE organ_donor = TRUE;
    """)

    organ_donors = cursor.fetchone()[0]

    # Emergency Requests
    cursor.execute("""
    SELECT COUNT(*)
    FROM patient_request
    WHERE urgency_level = 'high';
    """)

    emergency_requests = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    # DISPLAY METRICS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Donors",
            total_donors
        )

    with col2:
        st.metric(
            "Blood Donors",
            blood_donors
        )

    with col3:
        st.metric(
            "Organ Donors",
            organ_donors
        )

    with col4:
        st.metric(
            "Emergency Requests",
            emergency_requests
        )
    
    # Charts Row
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="section-title">📊 Blood Bank Total Record</div>', unsafe_allow_html=True)
        
        query = """
        SELECT donation_date,
            COUNT(*) AS total_donations
        FROM donation_record
        GROUP BY donation_date
        ORDER BY donation_date;
        """

        chart_df = run_query(query)

        days = pd.to_datetime(
            chart_df["donation_date"]
        ).dt.strftime('%d-%b')        
        values = chart_df["total_donations"]
        
        # Create line chart
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(days, values, marker='o', color='#CE1126', linewidth=2, markersize=8)
        max_value = max(values)
        ax.set_ylim(0, max_value + 2)
        ax.fill_between(days, values, alpha=0.2, color='#CE1126')
        ax.grid(axis='y', alpha=0.3)
        ax.set_ylabel('Units', fontsize=10)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    with col2:

        conn = create_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM patient_request;
        """)

        active_requests = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        st.markdown(
            '<div class="section-title">📋 Active Requests</div>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="red-card">
            <div style="font-size: 32px;">📋</div>
            <div class="red-card-value">{active_requests}</div>
            <div class="red-card-label">Requests</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Bottom Row - Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-title">🏥 Top Requested Blood Group</div>', unsafe_allow_html=True)
        
        query = """
        SELECT blood_required,
               COUNT(*) AS total_requests
        FROM patient_request
        WHERE blood_required IS NOT NULL
        GROUP BY blood_required;
        """

        chart_df = run_query(query)

        groups = chart_df["blood_required"]
        values = chart_df["total_requests"]
        
        # Create bar chart
        fig, ax = plt.subplots(figsize=(8, 4))
        bars = ax.bar(
            groups,
            values,
            alpha=0.8,
            edgecolor='black',
            linewidth=1.5
        )
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontweight='bold')
        
        ax.set_ylabel('Units Requested', fontsize=10)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        st.pyplot(fig)
    
    with col2:
        st.markdown('<div class="section-title">🔔 Recent Notification</div>', unsafe_allow_html=True)
        
        query = """
        SELECT donor_name,
            blood_group,
            city
        FROM donor
        ORDER BY donor_id DESC
        LIMIT 4;
        """

        notif_df = run_query(query)

        for _, row in notif_df.iterrows():

            st.markdown(f"""
            <div class="notification-item">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <div class="notification-title">
                            👤 New donor {row['donor_name']} registered
                        </div>
                        <div class="notification-time">
                            {row['blood_group']} • {row['city']}
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Donors Page
elif page == "Donors":
    st.markdown('<h1 style="color: #CE1126;">Donors Management</h1>', unsafe_allow_html=True)
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Active Donors", value="8,425", delta="+125")
    
    with col2:
        st.metric(label="Inactive Donors", value="4,115", delta="-45")
    
    with col3:
        st.metric(label="Total Donors", value="12,540", delta="+80")
    
    st.subheader("Donor Registration")

    with st.container():

        col1, col2 = st.columns(2)

        # LEFT COLUMN
        with col1:

            name = st.text_input("Full Name")

            phone = st.text_input("Phone Number")

            city = st.text_input("City")

            gender = st.selectbox(
                "Gender",
                ["Male", "Female", "Other"]
            )

        # RIGHT COLUMN
        with col2:

            blood_group = st.selectbox(
                "Blood Group",
                ["O+", "O-", "A+", "A-",
                "B+", "B-", "AB+", "AB-"]
            )

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=65
            )

            organ_donor = st.checkbox(
                "Organ Donor"
            )

           # Show organ dropdown ONLY if checkbox selected
            if organ_donor:

                organ_type = st.selectbox(
                    "Organ Type",
                    [
                        "Kidney",
                        "Liver",
                        "Heart",
                        "Lungs",
                        "Pancreas",
                        "Intestine",
                        "Cornea",
                        "Bone Marrow",
                        "Skin",
                        "Blood"
                    ]
                )

            else:
                organ_type = "Not Applicable"
        
            donation_date = st.date_input(
                "Last Donation Date"
            )

        submitted = st.button(
            "Register Donor",
            use_container_width=True
        )

        if submitted:

            if not organ_donor:
                organ_type = None

            insert_donor(
                name,
                age,
                gender,
                blood_group,
                city,
                phone,
                organ_donor,
                organ_type,
                donation_date
            )

            st.success(
                f"✅ Donor {name} registered successfully!"
            )
            st.rerun()

        st.divider()
        st.subheader("Registered Donors")
        donor_df = fetch_donors()
        st.dataframe(
            donor_df,
            use_container_width=True
        )

# Hospital Page
elif page == "Hospital":

    st.markdown(
        '<h1 style="color: #CE1126;">Hospital Management</h1>',
        unsafe_allow_html=True
    )

    st.divider()

    # =========================
    # METRICS
    # =========================

    conn = create_connection()

    cursor = conn.cursor()

    # Total Hospitals
    cursor.execute(
        "SELECT COUNT(*) FROM hospital"
    )

    total_hospitals = cursor.fetchone()[0]

    # Total Requests
    cursor.execute(
        "SELECT COUNT(*) FROM patient_request"
    )

    total_requests = cursor.fetchone()[0]

    # Most Active Hospital
    cursor.execute("""
    SELECT h.hospital_name,
           COUNT(pr.request_id) AS total_requests
    FROM hospital h
    JOIN patient_request pr
    ON h.hospital_id = pr.hospital_id
    GROUP BY h.hospital_name
    ORDER BY total_requests DESC
    LIMIT 1;
    """)

    result = cursor.fetchone()

    most_active_hospital = result[0]

    cursor.close()
    conn.close()

    # DISPLAY METRICS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Hospitals",
            total_hospitals
        )

    with col2:
        st.metric(
            "Total Requests",
            total_requests
        )

    with col3:
        st.metric(
            "Most Active Hospital",
            most_active_hospital
        )

    st.divider()

    # =========================
    # HOSPITAL TABLE
    # =========================

    st.subheader("Registered Hospitals")

    query = """
    SELECT *
    FROM hospital;
    """

    hospital_df = run_query(query)

    st.dataframe(
        hospital_df,
        use_container_width=True
    )

    st.divider()

    # =========================
    # REQUESTS PER HOSPITAL
    # =========================

    st.subheader("Total Requests Per Hospital")

    query = """
    SELECT h.hospital_name,
           COUNT(pr.request_id) AS total_requests
    FROM hospital h
    JOIN patient_request pr
    ON h.hospital_id = pr.hospital_id
    GROUP BY h.hospital_name;
    """

    request_df = run_query(query)

    st.dataframe(
        request_df,
        use_container_width=True
    )

    st.divider()

    # =========================
    # HOSPITAL + PATIENT DETAILS
    # =========================

    st.subheader("Hospital Patient Requests")

    query = """
    SELECT h.hospital_name,
           pr.patient_name,
           pr.urgency_level,
           pr.request_date
    FROM hospital h
    JOIN patient_request pr
    ON h.hospital_id = pr.hospital_id;
    """

    details_df = run_query(query)

    st.dataframe(
        details_df,
        use_container_width=True
    )

# Patient Requests Page
elif page == "Patient Requests":

    st.markdown(
        '<h1 style="color: #CE1126;">Patient Requests Management</h1>',
        unsafe_allow_html=True
    )

    st.divider()

    # =========================
    # REQUEST FORM
    # =========================

    st.subheader("Create Patient Request")

    with st.container():

        col1, col2 = st.columns(2)

        # LEFT COLUMN
        with col1:

            patient_name = st.text_input(
                "Patient Name"
            )

            hospital_id = st.number_input(
                "Hospital ID",
                min_value=1,
                step=1
            )

            request_type = st.selectbox(
                "Request Type",
                ["Blood", "Organ"]
            )

            required_units = st.number_input(
                "Required Units",
                min_value=1,
                max_value=10
            )

        # RIGHT COLUMN
        with col2:

            urgency_level = st.selectbox(
                "Urgency Level",
                ["low", "mid", "high"]
            )

            request_date = st.date_input(
                "Request Date"
            )

            # BLOOD REQUEST
            if request_type == "Blood":

                blood_required = st.selectbox(
                    "Blood Group Required",
                    [
                        "O+", "O-", "A+", "A-",
                        "B+", "B-", "AB+", "AB-"
                    ]
                )

                organ_required = None

            # ORGAN REQUEST
            else:

                organ_required = st.selectbox(
                    "Organ Required",
                    [
                        "Kidney",
                        "Liver",
                        "Heart",
                        "Lungs",
                        "Pancreas"
                    ]
                )

                blood_required = None

        submitted = st.button(
            "Create Request",
            use_container_width=True
        )

        if submitted:

            insert_patient_request(
                hospital_id,
                patient_name,
                blood_required,
                organ_required,
                required_units,
                urgency_level,
                request_date
            )

            st.success(
                f"✅ Request created for {patient_name}"
            )

    # =========================
    # REQUEST TABLE
    # =========================

    st.divider()

    st.subheader("Patient Requests")

    request_df = fetch_patient_requests()

    st.dataframe(
        request_df,
        use_container_width=True
    )

    # =========================
    # SQL QUERY TABS
    # =========================

    st.divider()

    tab1, tab2, tab3 = st.tabs([
        "High Urgency",
        "Most Requested Blood",
        "Organ Requests"
    ])

    # =========================
    # HIGH URGENCY QUERY
    # =========================

    with tab1:

        query = '''
        SELECT patient_name,
               blood_required,
               organ_required,
               request_date
        FROM patient_request
        WHERE urgency_level = 'high';
        '''

        df = run_query(query)

        st.dataframe(
            df,
            use_container_width=True
        )

    # =========================
    # MOST REQUESTED BLOOD
    # =========================

    with tab2:

        query = '''
        SELECT blood_required,
               COUNT(*) AS total_requests
        FROM patient_request
        WHERE blood_required IS NOT NULL
        GROUP BY blood_required
        ORDER BY total_requests DESC;
        '''

        df = run_query(query)

        st.dataframe(
            df,
            use_container_width=True
        )

    # =========================
    # ORGAN REQUESTS
    # =========================

    with tab3:

        query = '''
        SELECT patient_name,
               organ_required,
               urgency_level
        FROM patient_request
        WHERE organ_required IS NOT NULL;
        '''

        df = run_query(query)

        st.dataframe(
            df,
            use_container_width=True
        )

# Donate Blood Page
elif page == "Donation Centre":

    st.markdown(
        '<h1 style="color: #CE1126;">Donation Centre</h1>',
        unsafe_allow_html=True
    )

    st.divider()

    # =========================
    # ACTIVE REQUESTS
    # =========================

    st.subheader("Active Blood Requests")

    request_df = fetch_active_requests()

    st.dataframe(
        request_df,
        use_container_width=True
    )

    st.divider()

    # =========================
    # DONATION FORM
    # =========================

    st.subheader("Apply To Donate")

    col1, col2 = st.columns(2)

    with col1:

        donor_id = st.number_input(
            "Donor ID",
            min_value=1,
            step=1
        )

        donation_units = st.number_input(
            "Donation Units",
            min_value=1,
            max_value=10
        )

    with col2:

        hospital_id = st.number_input(
            "Hospital ID",
            min_value=1,
            step=1
        )

        donation_type = st.selectbox(
            "Donation Type",
            ["blood", "organ"]
        )

        donation_date = st.date_input(
            "Donation Date"
        )

    submitted = st.button(
        "Donate Blood",
        use_container_width=True
    )

    if submitted:

        success, message = insert_donation_record(
            donor_id,
            hospital_id,
            donation_type,
            donation_units,
            donation_date
        )

        if success:

            st.success(f"✅ {message}")

        else:

            st.error(f"❌ {message}")

# Donation Match Page
elif page == "Donation Match":

    st.markdown(
        '<h1 style="color: #CE1126;">Donation Match Management</h1>',
        unsafe_allow_html=True
    )

    st.divider()

    # =========================
    # METRICS
    # =========================

    conn = create_connection()

    cursor = conn.cursor()

    # Total Matches
    cursor.execute(
        "SELECT COUNT(*) FROM donation_match"
    )

    total_matches = cursor.fetchone()[0]

    # Total Donation Records
    cursor.execute(
        "SELECT COUNT(*) FROM donation_record"
    )

    total_records = cursor.fetchone()[0]

    # Organ Donations
    cursor.execute("""
    SELECT COUNT(*)
    FROM donation_record
    WHERE donation_type = 'organ';
    """)

    organ_donations = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    # =========================
    # DISPLAY METRICS
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Matches",
            total_matches
        )

    with col2:
        st.metric(
            "Donation Records",
            total_records
        )

    with col3:
        st.metric(
            "Organ Donations",
            organ_donations
        )

    st.divider()

    # =========================
    # DONATION MATCH TABLE
    # =========================

    st.subheader("Donation Match Table")

    query = """
    SELECT *
    FROM donation_match;
    """

    match_df = run_query(query)

    st.dataframe(
        match_df,
        use_container_width=True
    )

    st.divider()

    # =========================
    # DONATION RECORD TABLE
    # =========================

    st.subheader("Donation Records")

    query = """
    SELECT *
    FROM donation_record;
    """

    donation_df = run_query(query)

    st.dataframe(
        donation_df,
        use_container_width=True
    )

    st.divider()

    # =========================
    # ADVANCED JOIN QUERY
    # =========================

    st.subheader("Patient ↔ Donor Match Details")

    query = """
    SELECT pr.patient_name,
           d.donor_name,
           dm.match_date
    FROM donation_match dm
    JOIN patient_request pr
    ON dm.request_id = pr.request_id
    JOIN donation_record dr
    ON dm.donation_id = dr.donation_id
    JOIN donor d
    ON dr.donor_id = d.donor_id;
    """

    details_df = run_query(query)

    st.dataframe(
        details_df,
        use_container_width=True
    )

    st.divider()

    # =========================
    # DONOR HOSPITAL DETAILS
    # =========================

    st.subheader("Donor Hospital Records")

    query = """
    SELECT d.donor_name,
           h.hospital_name,
           dr.donation_type,
           dr.donation_date
    FROM donation_record dr
    JOIN donor d
    ON dr.donor_id = d.donor_id
    JOIN hospital h
    ON dr.hospital_id = h.hospital_id;
    """

    donor_hospital_df = run_query(query)

    st.dataframe(
        donor_hospital_df,
        use_container_width=True
    )

# Blood Inventory Page
elif page == "Blood Inventory":

    st.markdown(
        '<h1 style="color: #CE1126;">Blood Inventory Management</h1>',
        unsafe_allow_html=True
    )

    st.divider()

    # =========================
    # BLOOD INVENTORY TABLE
    # =========================

    st.subheader("Hospital Blood Inventory")

    query = """
    SELECT h.hospital_name,
           b.blood_group,
           b.available_units
    FROM blood_inventory b
    JOIN hospital h
    ON b.hospital_id = h.hospital_id
    ORDER BY h.hospital_name, b.blood_group;
    """

    inventory_df = run_query(query)

    st.dataframe(
        inventory_df,
        use_container_width=True
    )

    st.divider()

    # =========================
    # BLOOD INVENTORY CHART
    # =========================

    st.subheader("Blood Inventory Distribution")

    blood_groups = inventory_df["blood_group"]
    units = inventory_df["available_units"]

    fig, ax = plt.subplots(figsize=(10, 5))

    bars = ax.bar(
        blood_groups,
        units
    )

    # VALUE LABELS
    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f'{int(height)}',
            ha='center',
            va='bottom',
            fontweight='bold'
        )

    ax.set_ylabel("Available Units")
    ax.set_xlabel("Blood Group")

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    st.pyplot(fig)

# Footer
st.divider()
st.markdown(
    '<p style="text-align: center; color: #666; font-size: 12px;">DBMS Project © 2026 | Blood & Organ Donation System</p>',
    unsafe_allow_html=True
)