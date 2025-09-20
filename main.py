import pandas as pd
import streamlit as st 

data = pd.read_csv("product.csv")


st.title("dashboard")
st.write("this application is about displaying product sales")

if 'username' in st.session_state:
    st.write("hello!"(st.session_state['Username']))
else: 
    st.info("please register something")


Upload_file = st.file_uploader("choose a csvfile",type="csv")

if Upload_file is None:
    st.write("please upload csv file")

else:
    data - pd.read_sv(Upload_file)
    print(data)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.metric("sales", "1,500","12%")
    with col2:
        st.metric("revenue", "3,000","20%")
    with col3:
        st.metric("user", "100","-12%")
    st.line_chart(data['sales'])    
    
    if st.button("show table"):
        st.header("sales table")
        st.subheader("this is a sales table")
        st.write(data)        