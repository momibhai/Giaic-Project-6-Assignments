class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Student Name is {self.name} and Marks Are: {self.marks}")


my_student = Student("Ali", 90)
my_student.display()