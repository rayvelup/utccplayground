import pandas as pd
import streamlit as st
import altair as alt

st.title("📊 Insurance Data Dashboard")

# Show username if set
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

    # Chart selector
    chart_option = st.selectbox(
        "Select chart type for Charges vs Age",
        ["Original", "Option 1: Average per Age", "Option 2: Scatter Plot", "Option 3: Age Groups"]
    )

    # Chart rendering
    if chart_option == "Original":
        st.subheader("Charges by Age (Original Data)")
        st.line_chart(data[['age', 'charges']].set_index('age'))

    elif chart_option == "Option 1: Average per Age":
        st.subheader("Average Charges by Age")
        avg_charges_age = data.groupby('age')['charges'].mean()
        st.line_chart(avg_charges_age)

    elif chart_option == "Option 2: Scatter Plot":
        st.subheader("Charges vs Age (Scatter Plot)")
        scatter = alt.Chart(data).mark_circle(size=60).encode(
            x='age',
            y='charges',
            color='smoker',  # color by smoker
            tooltip=['age', 'charges', 'sex', 'smoker', 'region']
        ).interactive()
        st.altair_chart(scatter, use_container_width=True)

    elif chart_option == "Option 3: Age Groups":
        st.subheader("Average Charges by Age Group")
        data['age_group'] = pd.cut(data['age'],
                                   bins=[0,20,30,40,50,60,70],
                                   labels=['<20','20s','30s','40s','50s','60s+'])
        avg_by_group = data.groupby('age_group')['charges'].mean()
        st.bar_chart(avg_by_group)

    # Chart - average charges by region
    st.subheader("Average Charges by Region")
    region_charges = data.groupby('region')['charges'].mean()
    st.bar_chart(region_charges)

else:
    st.info("Please upload a CSV file to see the dashboard.")
