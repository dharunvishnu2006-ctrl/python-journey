import streamlit as st

st.title("AAROGYA Stats")

col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", 500, "+50")
col2.metric("Recovered", 450, "+45")
col3.metric("Critical", 50, "-5")

st.sidebar.title("Filter")
state = st.sidebar.selectbox("State", 
        ["Tamil Nadu", "Kerala", "Karnataka"])

st.write(f"Showing data for: {state}")