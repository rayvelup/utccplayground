import streamlit as st

st.title("Settings")

# Initialize session state if not exists
if 'username' not in st.session_state:
    st.session_state['username'] = ''

name = st.text_input("Enter your name")

if st.button("Set Name"):
    st.session_state['username'] = name
    st.success(f"Username set to: {st.session_state['username']}")
