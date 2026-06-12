import streamlit as st

st.title("🏥 Health Dashboard")

col1, col2 = st.columns(2)

col1.metric("Patients", 100, "+10")
col2.metric("Doctors", 25, "+2")

if st.button("Show Stats"):
    st.write("Stats loaded!")