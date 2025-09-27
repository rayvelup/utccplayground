import streamlit as st

st.set_page_config(page_title="Insurance Charge Estimator", layout="wide")
st.title("Insurance Charge Estimator")

# User inputs
age = st.number_input("Age", min_value=0, value=30)
weight = st.number_input("Weight (kg)", min_value=0.0, value=70.0)
height = st.number_input("Height (cm)", min_value=0.0, value=170.0)
children = st.number_input("Number of Children", min_value=0, value=0)
smoker = st.selectbox("Smoker", options=["no", "yes"])

if st.button("Estimate Charges"):
    if height > 0:
        bmi = weight / ((height / 100) ** 2)
    
        # Manual formula
        base = 2000
        age_factor = 50
        bmi_factor = 30
        children_factor = 300
        smoker_charge = 10000 if smoker == "yes" else 0

        charge = base + (age_factor * age) + (bmi_factor * bmi) + (children_factor * children) + smoker_charge
        st.success(f"Estimated Insurance Charge: ${charge:.2f}")
    else:
        st.error("Height must be greater than 0")