import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    layout="wide"
)

st.title("BMI Calculator")

# User inputs
weight = st.number_input("Weight (kg)", min_value=0.0, value=70.0)
height = st.number_input("Height (cm)", min_value=0.0, value=170.0)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / ((height/100) ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")

        # Optional BMI category
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif bmi < 24.9:
            st.success("Category: Normal weight")
        elif bmi < 29.9:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")
    else:
        st.error("Height must be greater than 0")
