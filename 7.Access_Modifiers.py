class Employee:
    def __init__(self):
        self.name = "Ali"            # Public
        self._salary = 50000         # Protected
        self.__ssn = "123-45-6789"   # Private

emp = Employee()

print("Public:", emp.name)

print("Protected:", emp._salary) 

try:
    print("Private:", emp.__ssn) 
except AttributeError as e:
    print("Private:", e)
