import streamlit as st
import pandas as pd

st.sidebar.title("AAROGYA Controls")
city = st.sidebar.selectbox("City",["Chennai", "Mumbai", "Delhi"])

st.title("AAROGYA Health Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Total Patients", 150, "+10")
col2.metric("Avg BMI", 24.5, "-0.5")
col3.metric("Avg BP", 120, "+2")

file = st.file_uploader("Upload Patient CSV")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    st.write(f"Total rows: {len(df)}")