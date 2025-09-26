import pandas as pd
import streamlit as st

st.title("Simple CSV Viewer")

# File uploader
upload_file = st.file_uploader("Choose a CSV file", type="csv")

if upload_file is not None:
    # Read CSV
    data = pd.read_csv(upload_file)
    # Show table
    st.write(data)
else:
    st.info("Please upload a CSV file.")