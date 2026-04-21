import sys
sys.path.append("src")
from grade_tracker import calculate_grade, rank_students, read_students

def test_calculate_grade_A():
    assert calculate_grade(92) == "A"

def test_calculate_grade_F():
    assert calculate_grade(45) == "F"

def test_calculate_grade_B():
    assert calculate_grade(85) == "B"

def test_rank_students():
    students = [
        {"name": "Arun", "marks": 78},
        {"name": "Dharun", "marks": 92}
    ]
    ranked = rank_students(students)
    assert ranked[0]["name"] == "Dharun"

def test_file_not_found():
    students = read_students("wrong.csv")
    assert students == []