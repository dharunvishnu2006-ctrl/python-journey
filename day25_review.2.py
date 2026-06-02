import streamlit as st

st.title("Doctor Dashboard")

specialization = st.sidebar.selectbox(
    "Specialization",
    ["Cardiology", "Neurology", "Orthopedic"]
)

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Doctors", 25, "+3")

with col2:
    st.metric("Patients Today", 150, "-10")

if st.button("Show Report"):
    st.write("Report Generated!")