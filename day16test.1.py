class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def introduce(self):
        print(f"Hi! I am {self.name}, {self.age} years old!")

    def is_pass(self):
        if self.marks >= 50:
            print("Pass!")
        else:
            print("Fail!")

student1 = Student("Dharun", 21, 95)
student2 = Student("Ram", 20, 45)

student1.introduce()
student1.is_pass()

student2.introduce()
student2.is_pass()