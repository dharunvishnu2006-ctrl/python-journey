import streamlit as st
import sys
sys.path.append("src")
from grade_tracker import read_students, calculate_grade, rank_students

st.title("student grade tracker")
st.subheader("upload your students CSV file")

uploaded_file = st.file_uploader("choose a CSV file", type="csv")

if uploaded_file is not None:
    with open("data/uploaded.csv","wb") as f:
        f.write(uploaded_file.getbuffer())

    students = read_students("data/uploaded.csv")
    ranked = rank_students(students)
    st.success(f"{len(ranked)} students loaded!")

    st.subheader("results")
    for s in ranked:
        grade = calculate_grade(s["marks"])
        st.write(f"Rank {s['rank']}:{s['name']} | Marks: {s['marks']} | Grade:{grade}")    