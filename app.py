import streamlit as st
import sys
import tempfile
sys.path.append("src")
from grade_tracker import read_students, calculate_grade, rank_students

st.title("Student Grade Tracker")
st.subheader("Upload your students CSV file")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(uploaded_file.getbuffer())
        tmp_path = tmp.name

    students = read_students(tmp_path)
    ranked = rank_students(students)
    st.success(f"{len(ranked)} students loaded!")

    st.subheader("Results")
    for s in ranked:
        grade = calculate_grade(s["marks"])
        st.write(f"Rank {s['rank']}: {s['name']} | Marks: {s['marks']} | Grade: {grade}")