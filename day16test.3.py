class Student:
    def __init__(self):
        self.__marks = 0 
    
    def set_marks(self, marks):
        if 0 <= marks <= 100: 
            self.__marks = marks
            print("Marks set!")
        else:
            print("Invalid marks!")
    
    def get_marks(self):
        return self.__marks  

student = Student()
student.set_marks(95)  
print(student.get_marks()) 
student.set_marks(150)  