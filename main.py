import pandas as pd
import streamlit as st
import altair as alt

st.title("📊 Insurance Data Dashboard")

# Show username if set in setting
if 'username' in st.session_state and st.session_state['username']:
    st.subheader(f"Welcome, {st.session_state['username']}!")

# File uploader
upload_file = st.file_uploader("Choose a CSV file", type=["csv"])

if upload_file is not None:
    # Load data
    data = pd.read_csv(upload_file)

    # Show table
    st.subheader("Data Preview")
    st.dataframe(data)

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Avg Age", f"{data['age'].mean():.1f}")
    with col2:
        st.metric("Avg BMI", f"{data['bmi'].mean():.1f}")
    with col3:
        st.metric("Total Children", f"{data['children'].sum():,}")
    with col4:
        st.metric("Avg Charges", f"${data['charges'].mean():,.0f}")

    st.subheader("Average Charges by Age")
    avg_charges_age = data.groupby('age')['charges'].mean()
    st.line_chart(avg_charges_age)
    
    # Chart - average charges by region
    st.subheader("Average Charges by Region")
    region_charges = data.groupby('region')['charges'].mean()
    st.bar_chart(region_charges)

else:
    st.info("Please upload a CSV file to see the dashboard.")
