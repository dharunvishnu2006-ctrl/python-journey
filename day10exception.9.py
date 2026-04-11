class ValidationError(Exception):
    pass
class AgeError(ValidationError):
    pass
class MarksError(ValidationError):
    pass
def validate_age(age):
    if age < 0 or age > 120:
        raise AgeError("Age must be between 0 and 120!")
    return True
def validate_marks(marks):
    if marks < 0 or marks > 100:
        raise MarksError("Marks must be 0 and 100!")
    return True
def get_student_info():
    try:
        name = input("Enter name:")
        age = int(input("Enter age:"))
        marks = float(input("Enter marks:"))

        validate_age(age)
        validate_marks(marks)
        print(f"\nstudent:{name}")
        print(f"age:{age}")
        print(f"marks:{marks}")
        print("All Valid!")


    except AgeError as e:
        print("Age Error:",e)
    except MarksError as e:
        print("Marks Error:",e) 
    except ValueError:
        print("please enter valid numbers!")
get_student_info()        