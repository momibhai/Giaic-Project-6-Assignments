class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

p1 = Person("M.Ali")
print(f"Person Name: {p1.name}")

t1 = Teacher("Umair", "AI")
print(f"Teacher Name: {t1.name}")
print(f"Teacher Subject: {t1.subject}")
        